from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
from io import open

ruta = ''

def nuevo_archivo():
    global ruta
    mensaje_estado.set("Nuevo archivo")
    ruta = ''
    editor.delete(1.0,END)
    root.title("Mi editor")

def guardar_archivo():
    global ruta
    mensaje_estado.set("Guardar archivo")
    if ruta != "":
        contenido = editor.get(1.0,'end-1c')
        fichero = open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje_estado.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje_estado.set("Guardar como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero",mode='w',defaultextension='.txt')
    #fichero = FileDialog.asksaveasfile(title="Guardar archivo",mode='w',defaultextension='.txt')
    if fichero is not None:
        ruta = fichero.name
        contenido = editor.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje_estado.set("Fichero guardado correctamente")
    else:
        mensaje_estado.set("Guardado cancelado")
        ruta = ""

def abrir_archivo():
    global ruta
    mensaje_estado.set("Abrir archivo")
    ruta = FileDialog.askopenfilename(initialdir=".",
                    filetype=( ("Archivos de texto",'*.txt'), ),
                    title="Elige un archivo")
    print(ruta)
    if ruta != "":
        fichero = open(ruta,'r')
        cadena = fichero.read()
        editor.delete(1.0,END)
        editor.insert('insert',cadena)
        fichero.close()
        root.title(ruta + "Mi editor")


root = Tk()

root.title("Editor de texto")
root.iconbitmap('Apple.ico')
root.resizable(1,1)

menu = Menu(root)
root.config(menu=menu)



#Marco que engloba todo
marco = Frame(root,width=480,height=640)
marco.pack()


#Barra de menu
barra_menu = Menu(root)
root.config(menu=barra_menu)

menu_archivo = Menu(barra_menu,tearoff=0)
menu_archivo.add_command(label="Nuevo",command=nuevo_archivo)
menu_archivo.add_command(label="Abrir",command=abrir_archivo)
menu_archivo.add_command(label="Guardar",command=guardar_archivo)
menu_archivo.add_command(label="Guardar como",command=guardar_como)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir",command=root.quit)

barra_menu.add_cascade(label="Archivo",menu=menu_archivo)

#Campo de texto
editor = Text(marco)
editor.place(x=0,y=0,height=620)
editor.config(width=38,font=("Lucida Sans Unicode",14),padx=10,pady=5)
#editor.pack(fill="both",expand=1)



#Etiqueta para el estado del archivo
mensaje_estado = StringVar()
mensaje_estado.set("Editor de texto")
estado = Label(marco,textvar=mensaje_estado,font=("Verdana Bold",12))
estado.place(x=0,y=620)





root.mainloop()