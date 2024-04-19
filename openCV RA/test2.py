import tkinter
import tkinter.messagebox

ventana=tkinter.Tk()
ventana.geometry("500x500")
ventana.title('Aplicacion de prueba')
#para poner texto
label1= tkinter.Label(ventana, text= "Esto es una prueba")
label1.pack(side=tkinter.TOP)

#para poner botones
def saludo():   # funcion que ejecutara el boton saludo
    tkinter.Label(ventana, text='Buenas noches presidente').pack()
def salir(): # funcion que ejecutara el boton salir
    ventana.destroy()
# creacion boton saludo
boton=tkinter.Button(ventana, text='Imprimir Saludo',command=saludo,fg='red')
boton.pack()
boton.place(x=200,y=200)
# creacion boton salir
boton2=tkinter.Button(ventana, text='Cerrar aplicacion',command=salir,fg='red')
boton2.pack()
boton2.place(x=200,y=400)

# ventana de mensaje
tkinter.messagebox.showinfo('Mensaje1','Este mensaje no hace nada')
respuesta=tkinter.messagebox.askquestion('Pregunta 1','ya le diste like??')
if respuesta=='yes':
    tkinter.messagebox.showinfo('','gracias el like')
else:
    tkinter.messagebox.showinfo('','pues que esperas??')

# listbox
lista=tkinter.Listbox(ventana)
lista.insert(1,'opcion1')
lista.pack()



# esto siempre tiene que ir al final de todo el programa
ventana.mainloop()