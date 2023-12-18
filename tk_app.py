import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def enter_data():
    accepted = accept_var.get()

    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
        tkinter.messagebox.showwarning(title= "Confirmacion", message="Solicitud ingresada con exito")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("REWAIR ESPANA INGRESO DE DATOS")

frame = tkinter.Frame(window)
frame.pack()


# imagenes
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Imagen fondo
image1 = Image.open(resource_path("fondo2.jpg"))
image1=image1.resize((500, 200), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
#label1.place(x=100, y=100)
label1.pack()


# espacios del formulario
user_info_frame =tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="Nombre Completo")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Codigo de empleado")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Area")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Produccion", "Calidad", "Ingenieria"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Cantidad solicitada")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Elemento")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Botas", "Gafas", "Chaleco", "Camisa", "Pantalon", "Orejeras", "Tangas"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# mas espacios
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Empleado directo")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Empleado directo",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text= "# Cantidad historica solicitada")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Antiguedad ")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# checkbox
terms_frame = tkinter.LabelFrame(frame, text="Acepta politica privacidad")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "Acepto la politica",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="INGRESAR DATOS", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()