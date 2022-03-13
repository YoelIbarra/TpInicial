from tkinter import *


root = Tk()

la_titulo_datos = Label(root,text="Ingresar datos nuevos")
la_tipo = Label(root,text="Tipo")
la_modelo = Label(root,text="Modelo")
la_referencia = Label(root,text="Referencia")


la_titulo_datos.grid(row=0,columnspan=100)
la_tipo.grid(row=1,column=0,sticky="e")
la_modelo.grid(row=1,column=2,sticky="e")
la_referencia.grid(row=1,column=4,sticky="e")

en_tipo = Entry(root)
en_modelo = Entry(root)
en_referencia= Entry(root)

en_tipo.grid(row=1,column=1)
en_modelo.grid(row=1,column=3)
en_referencia.grid(row=1,column=5)


bu_alta = Button(root,text="Alta")
bu_baja = Button(root,text="Baja")
bu_modificar = Button(root,text="Modificar")

bu_alta.grid(row=2,column=6, sticky="e")
bu_baja.grid(row=3,column=6, sticky="e")
bu_modificar.grid(row=4,column=6, sticky="e")

root.mainloop()