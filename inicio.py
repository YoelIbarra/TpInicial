import re
from tkinter import *
from tkinter import ttk
import db_config as db

coneccion = db.conexion_db()
db.create_tablas(coneccion)

root = Tk()
root.title('TP Inicial')

la_titulo_datos = Label(root, text="Ingresar datos nuevos")
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
treeview.column("referencia", width=100, minwidth=100, anchor='w')
treeview.column("fecha", width=100, minwidth=100, anchor='w')
treeview.heading("#0", text="Id")
treeview.heading("tipo", text="Tipo")
treeview.heading("modelo", text="Modelo")
treeview.heading("referencia", text="Referencia")
treeview.heading("fecha", text="Fecha")

treeview.grid(column=1, row=5, columnspan=4)


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


def alta_en_treeview(id_registro):
    registro = db.get_registro_by_id(id_registro)
    treeview.insert(
        "",
        "end",
        text=registro[0][0],  # id
        values=(
            registro[0][1],  # tipo
            registro[0][2],  # modelo
            registro[0][3],  # referencia
            registro[0][4]  # fecha_insert
        )
    )


def validar(entrada, label, f_validacion):
    return f_validacion(entrada, label)


def v_no_tiene_numeros(entrada, label):
    resultado = re.match(re.compile("^[a-zA-Z]+$"), entrada)
    if(resultado):
        label['text'] = 'Ingreso exitoso'
    else:
        label['text'] = 'No puede ingresar números'
    return resultado


def v_no_es_vacio(entrada, label):
    resultado = bool(entrada)
    if(resultado):
        label['text'] = 'Ingreso exitoso'
    else:
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
        id_registro_ingresado = db.insert_producto(
            var_tipo.get(),
            var_modelo.get(),
            var_ref.get()
        )
        alta_en_treeview(id_registro_ingresado)
        mensaje['text'] = "Ingreso de Dispositivo exitoso"
    else:
        mensaje['text'] = "Error en los datos ingresados, intente nuevamente"


def baja():
    global mensaje
    focused = treeview.focus()
    id_a_eliminar = treeview.item(focused)['text']
    db.delete_producto(id_a_eliminar)
    actualizar_treeview()
    mensaje['text'] = "Se dio de baja el registro: " + str(id_a_eliminar)


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
        actualizar_treeview()
        mensaje['text'] = "Actualización de Dispositivo exitosa"
        + str(id_a_modificar) + " exitosa"
    else:
        mensaje['text'] = "Error en los datos ingresados, intente nuevamente"


bu_alta = Button(root, text="Alta", command=alta)
bu_baja = Button(root, text="Baja", command=baja)
bu_modificar = Button(root, text="Modificar", command=modificar)

bu_alta.grid(row=4, column=6, sticky="e")
bu_baja.grid(row=5, column=6, sticky="e")
bu_modificar.grid(row=7, column=6, sticky="e")

actualizar_treeview()

root.mainloop()
