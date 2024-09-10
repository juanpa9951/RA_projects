"""ZLP-Manager-Script: toggle projection elements group-wise
"""

def Laser_remote_v0:

    import sys
    import time
    import zlp
    from thriftpy2.thrift import TException

    service_ip = "localhost"
    service_port = 9090

    projection_time_sec = 2
    if len(sys.argv) >= 4:
        projection_time_sec = float(sys.argv[3])

    try:
        client = zlp.ZlpClient()
        client.connect(service_ip, service_port)

        # Fetch all top-level groups

        group_infos = client.getGeoTreeElementInfos(
            '', zlp.api.GeoTreeElementType.group)
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

        current_group_idx = 0
        previous_group_idx = len(top_level_groups) - 1

        while True:
            active_layer_name=top_level_groups[current_group_idx]
            print(f"\n ACTIVE LAYER: {active_layer_name}")

            ##### ACA ESTA EL TEMA, SE DEBE CREAR UN GRUPO CON EL TEXTO ADENTRO, EL NOMBRE DEL GRUPO ES IGUAL AL TEXTO, Y LUEGO ACTIVAR EL GRUPO
            #####  ESTE COMANDO HACE CREACION DEL GRUPO CON EL TEXTO ADENTRO
            text_element = zlp.api.TextElement(position=zlp.api.Point3d(1200, 500),
                                               text=active_layer_name,
                                               name=f"N-{active_layer_name}/text group/{active_layer_name}",
                                               height=150,
                                               coordinateSystems=["Table 5"])
            client.setTextElement(text_element)

            set_active_state(top_level_groups[previous_group_idx], False)
            set_active_state(top_level_groups[current_group_idx], True)

            set_active_state(f"N-{active_layer_name}", True)

            client.updateProjection()
            #time.sleep(projection_time_sec)
            ans=input("\n SIGUIENTE?   y/n")
            if ans=="n":
                break

            set_active_state(f"N-{active_layer_name}", False)


            previous_group_idx = current_group_idx
            current_group_idx = (current_group_idx + 1) % len(top_level_groups)

    except TException as exception:
        print(f"An error has occurred: {exception.message}")


def Laser_remote_v1(coordinates_name,x_name_offset,y_name_offset, letter_size):
    import sys
    import time
    import zlp
    from thriftpy2.thrift import TException


    service_ip = "localhost"
    service_port = 9090

    if len(sys.argv) >= 4:
        projection_time_sec = float(sys.argv[3])

    try:
        client = zlp.ZlpClient()
        client.connect(service_ip, service_port)

        # Fetch all top-level groups

        group_infos = client.getGeoTreeElementInfos(
            '', zlp.api.GeoTreeElementType.group)
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

        current_group_idx = 0
        previous_group_idx = len(top_level_groups) - 1

        while True:
            active_layer_name = top_level_groups[current_group_idx]
            print(f"\n ACTIVE LAYER: {active_layer_name}")

            ##### ACA ESTA EL TEMA, SE DEBE CREAR UN GRUPO CON EL TEXTO ADENTRO, EL NOMBRE DEL GRUPO ES IGUAL AL TEXTO, Y LUEGO ACTIVAR EL GRUPO
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
            # time.sleep(projection_time_sec)
            ans = input("\n SIGUIENTE?   y/n")
            if ans == "n":
                break

            set_active_state(f"N-{active_layer_name}", False)

            previous_group_idx = current_group_idx
            current_group_idx = (current_group_idx + 1) % len(top_level_groups)

    except TException as exception:
        print(f"An error has occurred: {exception.message}")