import re
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import db_config as db
import datetime as date

coneccion = db.conexion_db()
db.create_tablas(coneccion)

root = Tk()
root.geometry("750x350")
root.title('Aplicación para Reparaciones')

la_titulo_datos = Label(root, text="Ingresar datos del dispositivo", font= tkFont.Font(family="Lucida Grande", size=15))
la_tipo = Label(root, text="Tipo")
la_modelo = Label(root, text="Modelo")
la_referencia = Label(root, text="Referencia")

mensaje = Label(root)
mensaje.grid(row=8, column=1)

la_mensaje_tipo = Label(root)
la_mensaje_tipo.grid(row=2, column=1)

la_mensaje_modelo = Label(root)
la_mensaje_modelo.grid(row=2, column=3)

la_mensaje_ref = Label(root)
la_mensaje_ref.grid(row=2, column=5)


la_titulo_datos.grid(row=0, columnspan=100)
la_tipo.grid(row=1, column=0, sticky="e")
la_modelo.grid(row=1, column=2, sticky="e")
la_referencia.grid(row=1, column=4, sticky="e")

var_tipo = StringVar()
var_modelo = StringVar()
var_ref = StringVar()

en_tipo = Entry(root, textvariable=var_tipo, width=25)
en_modelo = Entry(root, textvariable=var_modelo, width=25)
en_referencia = Entry(root, textvariable=var_ref, width=25)

en_tipo.grid(row=1, column=1)
en_modelo.grid(row=1, column=3)
en_referencia.grid(row=1, column=5)


treeview = ttk.Treeview(root)
treeview["columns"] = ("tipo", "modelo", "referencia", "fecha")
treeview.column("#0", width=50, minwidth=50, anchor='w')
treeview.column("tipo", width=80, minwidth=80, anchor='w')
treeview.column("modelo", width=80, minwidth=80, anchor='w')
treeview.column("referencia", width=150, minwidth=100, anchor='w')
treeview.column("fecha", width=150, minwidth=100, anchor='w')
treeview.heading("#0", text="Id")
treeview.heading("tipo", text="Tipo")
treeview.heading("modelo", text="Modelo")
treeview.heading("referencia", text="Referencia")
treeview.heading("fecha", text="Fecha")

treeview.grid(column=1, row=5, columnspan=4)


def on_tree_row_clicked(event):
    global var_tipo, var_modelo, var_ref

    focused = treeview.focus()
    valores = treeview.item(focused)['values']

    var_tipo.set(valores[0])
    var_modelo.set(valores[1])
    var_ref.set(valores[2])


def resetear_inputs():
    global var_tipo, var_modelo, var_ref

    var_tipo.set('')
    var_modelo.set('')
    var_ref.set('')


treeview.bind("<ButtonRelease-1>", on_tree_row_clicked)


def actualizar_treeview():
    resultados = db.get_registros()
    for item in treeview.get_children():
        treeview.delete(item)
    for resultado in resultados:
        treeview.insert(
            "",
            "end",
            text=resultado[0],  # id
            values=(
                resultado[1],  # tipo
                resultado[2],  # modelo
                resultado[3],  # referencia
                resultado[4]  # fecha_insert
            )
        )


def validar(entrada, label, f_validacion):
    return f_validacion(entrada, label)


def v_no_tiene_numeros(entrada, label):
    resultado = re.match(re.compile("^[a-zA-Z]+$"), entrada)
    if(not resultado):
        label['text'] = 'No puede ingresar números'
    return resultado


def v_no_es_vacio(entrada, label):
    resultado = bool(entrada)
    if(not resultado):
        label['text'] = 'No puede estar vacío'
    return resultado


def alta():
    global mensaje
    global la_mensaje_tipo
    global la_mensaje_modelo
    global la_mensaje_ref

    valida_tipo = validar(var_tipo.get(), la_mensaje_tipo, v_no_tiene_numeros)
    valida_modelo = validar(var_modelo.get(), la_mensaje_modelo, v_no_es_vacio)
    valida_ref = validar(var_ref.get(), la_mensaje_ref, v_no_es_vacio)
    if (valida_tipo and valida_modelo and valida_ref):
        fecha_ingeso = date.datetime.now()
        id_registro_ingresado = db.insert_producto(
            var_tipo.get(),
            var_modelo.get(),
            var_ref.get(),
            fecha_ingeso
        )
        treeview.insert(
            "",
            "end",
            text=id_registro_ingresado,
            values=(
                var_tipo.get(),
                var_modelo.get(),
                var_ref.get(),
                fecha_ingeso
            )
        )
        mensaje['text'] = "Ingreso de Dispositivo exitoso"
        resetear_inputs()
    else:
        mensaje['text'] = "Error en los datos ingresados, intente nuevamente"


def baja():
    global mensaje
    focused = treeview.focus()
    id_a_eliminar = treeview.item(focused)['text']
    db.delete_producto(id_a_eliminar)
    treeview.delete(focused)
    mensaje['text'] = "Se dio de baja el registro: " + str(id_a_eliminar)
    resetear_inputs()


def modificar_en_treeview(item_a_modificar):
    # para no actualizar la fecha cuando se modifica el registro
    fecha_existente = treeview.item(item_a_modificar)['values'][3]
    nuevo_registro = (
        var_tipo.get(),
        var_modelo.get(),
        var_ref.get(),
        fecha_existente
    )
    treeview.item(item_a_modificar, values=nuevo_registro)


def modificar():
    global mensaje
    global la_mensaje_tipo
    global la_mensaje_modelo
    global la_mensaje_ref

    focused = treeview.focus()
    id_a_modificar = treeview.item(focused)['text']

    valida_tipo = validar(var_tipo.get(), la_mensaje_tipo, v_no_tiene_numeros)
    valida_modelo = validar(var_modelo.get(), la_mensaje_modelo, v_no_es_vacio)
    valida_ref = validar(var_ref.get(), la_mensaje_ref, v_no_es_vacio)

    if (valida_tipo and valida_modelo and valida_ref):
        db.update_producto(
            var_tipo.get(),
            var_modelo.get(),
            var_ref.get(),
            id_a_modificar
        )
        modificar_en_treeview(focused)
        mensaje['text'] = "Actualización del Dispositivo " + str(id_a_modificar) + " exitosa"
    else:
        mensaje['text'] = "Error en los datos ingresados, intente nuevamente"


bu_alta = Button(root, text="Alta", command=alta, bg='light blue', height=1, width=10)
bu_alta.place(x=600, y=80)
bu_baja = Button(root, text="Baja", command=baja, bg='light blue', height=1, width=10)
bu_baja.place(x=600, y=160)
bu_modificar = Button(root, text="Modificar", command=modificar, bg='light blue', height=1, width=10)
bu_modificar.place(x=600, y=240)

actualizar_treeview()

root.mainloop()
