from tkinter import *
from tkinter import ttk

root = Tk()

la_titulo_datos = Label(root, text="Ingresar datos nuevos")
la_tipo = Label(root, text="Tipo")
la_modelo = Label(root, text="Modelo")
la_referencia = Label(root, text="Referencia")


la_titulo_datos.grid(row=0, columnspan=100)
la_tipo.grid(row=1, column=0, sticky="e")
la_modelo.grid(row=1, column=2, sticky="e")
la_referencia.grid(row=1, column=4, sticky="e")

var_tipo = StringVar()
var_modelo = StringVar()
var_referencia = StringVar()

en_tipo = Entry(root, textvariable=var_tipo, width=25)
en_modelo = Entry(root, textvariable=var_modelo, width=25)
en_referencia = Entry(root, textvariable=var_referencia, width=25)

en_tipo.grid(row=1, column=1)
en_modelo.grid(row=1, column=3)
en_referencia.grid(row=1, column=5)


treeview = ttk.Treeview(root)
treeview["columns"] = ("modelo", "referencia")
treeview.column("#0", width=50, minwidth=50, anchor='w')
treeview.column("modelo", width=80, minwidth=80, anchor='w')
treeview.column("referencia", width=100, minwidth=100, anchor='w')
treeview.heading("#0", text="Tipo")
treeview.heading("modelo", text="Modelo")
treeview.heading("referencia", text="Referencia")

treeview.grid(column=0, row=4, columnspan=3)


def alta():
    treeview.insert(
        "",
        "end",
        text=var_tipo.get(),
        values=(
            var_modelo.get(),
            var_referencia.get()
        )
    )


def baja():
    item = treeview.focus()
    treeview.delete(item)


def modificar():
    item = treeview.focus()
    treeview.item(
        item,
        text=var_tipo.get(),
        values=(
            var_modelo.get(),
            var_referencia.get()
        )
    )


bu_alta = Button(root, text="Alta", command=alta)
bu_baja = Button(root, text="Baja", command=baja)
bu_modificar = Button(root, text="Modificar", command=modificar)

bu_alta.grid(row=2, column=6, sticky="e")
bu_baja.grid(row=4, column=6, sticky="e")
bu_modificar.grid(row=6, column=6, sticky="e")

root.mainloop()
