import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import Button
import tkinter.font as tkFont
# import re
# import datetime as date


class View():

    def __init__(self, controller):

        # Attributes
        self.controller = controller
        self.root = tk.Tk()

        self._init_root()

    def show_view(self):
        self.root.mainloop()

    def _init_root(self):

        self.root.geometry("750x350")
        self.root.title('Aplicación para Reparaciones')

        self.root.label_titulo_datos = Label(
            self.root,
            text="Ingresar datos del dispositivo",
            font=tkFont.Font(family="Lucida Grande", size=15))
        self.root.label_tipo = Label(self.root, text="Tipo")
        self.root.label_modelo = Label(self.root, text="Modelo")
        self.root.label_referencia = Label(self.root, text="Referencia")

        self.root.label_mensaje = Label(self.root)
        self.root.label_mensaje.grid(row=8, column=1)

        self.root.label_mensaje_tipo = Label(self.root)
        self.root.label_mensaje_tipo.grid(row=2, column=1)

        self.root.label_mensaje_modelo = Label(self.root)
        self.root.label_mensaje_modelo.grid(row=2, column=3)

        self.root.label_mensaje_ref = Label(self.root)
        self.root.label_mensaje_ref.grid(row=2, column=5)

        self.root.label_titulo_datos.grid(row=0, columnspan=100)
        self.root.label_tipo.grid(row=1, column=0, sticky="e")
        self.root.label_modelo.grid(row=1, column=2, sticky="e")
        self.root.label_referencia.grid(row=1, column=4, sticky="e")

        self.root.var_tipo = StringVar()
        self.root.var_modelo = StringVar()
        self.root.var_ref = StringVar()

        self.root.en_tipo = Entry(
                            self.root,
                            textvariable=self.root.var_tipo,
                            width=25)

        self.root.en_modelo = Entry(
                            self.root,
                            textvariable=self.root.var_modelo,
                            width=25)

        self.root.en_referencia = Entry(
                                self.root,
                                textvariable=self.root.var_ref,
                                width=25)

        self.root.en_tipo.grid(row=1, column=1)
        self.root.en_modelo.grid(row=1, column=3)
        self.root.en_referencia.grid(row=1, column=5)

        self.root.treeview = ttk.Treeview(self.root)
        self.root.treeview["columns"] = (
                                        "tipo",
                                        "modelo",
                                        "referencia",
                                        "fecha")

        self.root.treeview.column("#0", width=50, minwidth=50, anchor='w')
        self.root.treeview.column("tipo", width=80, minwidth=80, anchor='w')
        self.root.treeview.column("modelo", width=80, minwidth=80, anchor='w')

        self.root.treeview.column(
                                "referencia",
                                width=150,
                                minwidth=100,
                                anchor='w')

        self.root.treeview.column("fecha", width=150, minwidth=100, anchor='w')
        self.root.treeview.heading("#0", text="Id")
        self.root.treeview.heading("tipo", text="Tipo")
        self.root.treeview.heading("modelo", text="Modelo")
        self.root.treeview.heading("referencia", text="Referencia")
        self.root.treeview.heading("fecha", text="Fecha")

        self.root.treeview.grid(column=1, row=5, columnspan=4)

        self.root.bu_alta = Button(
                                self.root,
                                text="Alta",
                                bg='light blue',
                                height=1,
                                width=10)

        self.root.bu_alta.place(x=600, y=80)
        self.root.bu_baja = Button(
                                self.root,
                                text="Baja",
                                bg='light blue',
                                height=1,
                                width=10)

        self.root.bu_baja.place(x=600, y=160)
        self.root.bu_modificar = Button(
                                    self.root,
                                    text="Modificar",
                                    bg='light blue',
                                    height=1,
                                    width=10)

        self.root.bu_modificar.place(x=600, y=240)


# def on_tree_row_clicked(event):
#     global var_tipo, var_modelo, var_ref

#     focused = treeview.focus()
#     valores = treeview.item(focused)['values']

#     var_tipo.set(valores[0])
#     var_modelo.set(valores[1])
#     var_ref.set(valores[2])


# def resetear_inputs():
#     global var_tipo, var_modelo, var_ref

#     var_tipo.set('')
#     var_modelo.set('')
#     var_ref.set('')


# treeview.bind("<ButtonRelease-1>", on_tree_row_clicked)


# def actualizar_treeview():
#     resultados = db.get_registros()
#     for item in treeview.get_children():
#         treeview.delete(item)
#     for resultado in resultados:
#         treeview.insert(
#             "",
#             "end",
#             text=resultado[0],  # id
#             values=(
#                 resultado[1],  # tipo
#                 resultado[2],  # modelo
#                 resultado[3],  # referencia
#                 resultado[4]  # fecha_insert
#             )
#         )


# def validar(entrada, label, f_validacion):
#     return f_validacion(entrada, label)


# def v_no_tiene_numeros(entrada, label):
#     resultado = re.match(re.compile("^[a-zA-Z]+$"), entrada)
#     if(not resultado):
#         label['text'] = 'No puede ingresar números'
#     return resultado


# def v_no_es_vacio(entrada, label):
#     resultado = bool(entrada)
#     if(not resultado):
#         label['text'] = 'No puede estar vacío'
#     return resultado


# def alta():
#     global mensaje
#     global la_mensaje_tipo
#     global la_mensaje_modelo
#     global la_mensaje_ref

#     valida_tipo = validar(var_tipo.get(), la_mensaje_tipo, v_no_tiene_numeros)
#     valida_modelo = validar(var_modelo.get(), la_mensaje_modelo, v_no_es_vacio)
#     valida_ref = validar(var_ref.get(), la_mensaje_ref, v_no_es_vacio)
#     if (valida_tipo and valida_modelo and valida_ref):
#         fecha_ingeso = date.datetime.now()
#         id_registro_ingresado = db.insert_producto(
#             var_tipo.get(),
#             var_modelo.get(),
#             var_ref.get(),
#             fecha_ingeso
#         )
#         treeview.insert(
#             "",
#             "end",
#             text=id_registro_ingresado,
#             values=(
#                 var_tipo.get(),
#                 var_modelo.get(),
#                 var_ref.get(),
#                 fecha_ingeso
#             )
#         )
#         mensaje['text'] = "Ingreso de Dispositivo exitoso"
#         resetear_inputs()
#     else:
#         mensaje['text'] = "Error en los datos ingresados, intente nuevamente"


# def baja():
#     global mensaje
#     focused = treeview.focus()
#     id_a_eliminar = treeview.item(focused)['text']
#     db.delete_producto(id_a_eliminar)
#     treeview.delete(focused)
#     mensaje['text'] = "Se dio de baja el registro: " + str(id_a_eliminar)
#     resetear_inputs()


# def modificar_en_treeview(item_a_modificar):
#     # para no actualizar la fecha cuando se modifica el registro
#     fecha_existente = treeview.item(item_a_modificar)['values'][3]
#     nuevo_registro = (
#         var_tipo.get(),
#         var_modelo.get(),
#         var_ref.get(),
#         fecha_existente
#     )
#     treeview.item(item_a_modificar, values=nuevo_registro)


# def modificar():
#     global mensaje
#     global la_mensaje_tipo
#     global la_mensaje_modelo
#     global la_mensaje_ref

#     focused = treeview.focus()
#     id_a_modificar = treeview.item(focused)['text']

#     valida_tipo = validar(var_tipo.get(), la_mensaje_tipo, v_no_tiene_numeros)
#     valida_modelo = validar(var_modelo.get(), la_mensaje_modelo, v_no_es_vacio)
#     valida_ref = validar(var_ref.get(), la_mensaje_ref, v_no_es_vacio)

#     if (valida_tipo and valida_modelo and valida_ref):
#         db.update_producto(
#             var_tipo.get(),
#             var_modelo.get(),
#             var_ref.get(),
#             id_a_modificar
#         )
#         modificar_en_treeview(focused)
#         mensaje['text'] = "Actualización del Dispositivo " + str(id_a_modificar) + " exitosa"
#     else:
#         mensaje['text'] = "Error en los datos ingresados, intente nuevamente"


# actualizar_treeview()
