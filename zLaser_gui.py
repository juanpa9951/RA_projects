import tkinter as tk

import sys
import zlp
from thriftpy2.thrift import TException
import time
import keyboard
import pyautogui

service_ip = "localhost"
service_port = 9090
coordinates_name = "Table 1"
x_name_offset = 1000
y_name_offset = 500
letter_size = 30

def on_pgdown_pressed(event):
    global active_layer_name,active_layer_name,current_group_idx,previous_group_idx,client,group_infos,top_level_groups
    print("Page Down key was pressed!")
    set_active_state(f"N-{active_layer_name}", False)
    client.removeGeoTreeElement(f"N-{active_layer_name}")

    previous_group_idx = current_group_idx
    current_group_idx = (current_group_idx + 1) % len(top_level_groups)
    active_layer_name = top_level_groups[current_group_idx]
    print(f"\n ACTIVE LAYER: {active_layer_name}")

    #####  ESTE COMANDO HACE CREACION DEL GRUPO CON EL TEXTO ADENTRO
    text_element = zlp.api.TextElement(position=zlp.api.Point3d(x_name_offset, y_name_offset),
                                       text=active_layer_name,
                                       name=f"N-{active_layer_name}/text group/{active_layer_name}",
                                       height=letter_size,
                                       coordinateSystems=[coordinates_name])
    client.setTextElement(text_element)

    set_active_state(top_level_groups[previous_group_idx], False)
    set_active_state(top_level_groups[current_group_idx], True)

    set_active_state(f"N-{active_layer_name}", True)
    counter_label.config(text=f"Counter: {active_layer_name}")
    client.updateProjection()

def on_pgup_pressed(event):
    global active_layer_name, active_layer_name, current_group_idx, previous_group_idx, client, group_infos, top_level_groups
    print("Page Up key was pressed!")
    set_active_state(f"N-{active_layer_name}", False)
    client.removeGeoTreeElement(f"N-{active_layer_name}")

    previous_group_idx = current_group_idx
    current_group_idx = (current_group_idx - 1) % len(top_level_groups)
    active_layer_name = top_level_groups[current_group_idx]
    print(f"\n ACTIVE LAYER: {active_layer_name}")

    #####  ESTE COMANDO HACE CREACION DEL GRUPO CON EL TEXTO ADENTRO
    text_element = zlp.api.TextElement(position=zlp.api.Point3d(x_name_offset, y_name_offset),
                                       text=active_layer_name,
                                       name=f"N-{active_layer_name}/text group/{active_layer_name}",
                                       height=letter_size,
                                       coordinateSystems=[coordinates_name])
    client.setTextElement(text_element)

    set_active_state(top_level_groups[previous_group_idx], False)
    set_active_state(top_level_groups[current_group_idx], True)

    set_active_state(f"N-{active_layer_name}", True)
    counter_label.config(text=f"Counter: {active_layer_name}")
    client.updateProjection()


##### BEGIN EXECUTION OF CODE

if len(sys.argv) >= 4:
    projection_time_sec = float(sys.argv[3])

try:
    client = zlp.ZlpClient()
    client.connect(service_ip, service_port)

    # Fetch all top-level groups

    group_infos = client.getGeoTreeElementInfos('', zlp.api.GeoTreeElementType.group)
    top_level_groups = []
    for group_info in group_infos:
        if '/' not in group_info.name:
            top_level_groups.append(group_info.name)

    if not top_level_groups:
        print("There are no groups in the projection.")
        sys.exit()


    def set_active_state(group_name, active):
        group = client.getGeoTreeElement(group_name)
        group.activated = active
        client.updateGeoTreeElement(group)

        element_infos = client.getGeoTreeElementInfos(
            group_name, zlp.api.GeoTreeElementType.element)

        for info in element_infos:
            element = client.getGeoTreeElement(info.name)
            element.activated = active
            client.updateGeoTreeElement(element)


    # Deactivate entire projection

    for group in top_level_groups:
        set_active_state(group, False)

    # Toggle groups

    top_level_groups = [string for string in top_level_groups if not string.startswith("N-")]

    current_group_idx = 0
    previous_group_idx = len(top_level_groups) - 1

    active_layer_name = top_level_groups[current_group_idx]
    print(f"\n ACTIVE LAYER: {active_layer_name}")

    #####  ESTE COMANDO HACE CREACION DEL GRUPO CON EL TEXTO ADENTRO
    text_element = zlp.api.TextElement(position=zlp.api.Point3d(x_name_offset, y_name_offset),
                                       text=active_layer_name,
                                       name=f"N-{active_layer_name}/text group/{active_layer_name}",
                                       height=letter_size,
                                       coordinateSystems=[coordinates_name])
    client.setTextElement(text_element)

    set_active_state(top_level_groups[previous_group_idx], False)
    set_active_state(top_level_groups[current_group_idx], True)

    set_active_state(f"N-{active_layer_name}", True)

    client.updateProjection()

except TException as exception:
    print(f"An error has occurred: {exception.message}")



# Create the main application window
root = tk.Tk()
root.title("ZLASER REMOTE APP")
root.geometry("300x200")

# Add a label to the GUI
label = tk.Label(root, text="READY TO USE REMOTE", font=("Helvetica", 16), fg="blue")
label.pack(pady=20)

counter_label = tk.Label(root, text=f"LAYER: {active_layer_name}", font=("Helvetica", 16))
counter_label.pack(pady=20)


# Bind the Page Down key to the function
root.bind("<Next>", on_pgdown_pressed)

# Bind the Page Up key to the function
root.bind("<Prior>", on_pgup_pressed)

# Run the application
root.mainloop()
