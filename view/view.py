import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import Button
from utils.validator import Validator
import tkinter.font as tkFont
import datetime as date


class View():

    def __init__(self, controller):

        # Attributes
        self.controller = controller
        self.root = tk.Tk()
        self.validator = Validator()
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
                                command=self._create_product,
                                height=1,
                                width=10)

        self.root.bu_alta.place(x=600, y=80)
        self.root.bu_baja = Button(
                                self.root,
                                text="Baja",
                                bg='light blue',
                                command=self._delete_product,
                                height=1,
                                width=10)

        self.root.bu_baja.place(x=600, y=160)
        self.root.bu_modificar = Button(
                                    self.root,
                                    text="Modificar",
                                    bg='light blue',
                                    command=self._edit_product,
                                    height=1,
                                    width=10)

        self.root.bu_modificar.place(x=600, y=240)
        self.root.treeview.bind("<ButtonRelease-1>", self._on_tree_row_clicked)
        self._update_treeview()

    def _on_tree_row_clicked(self, event):
        focused = self.root.treeview.focus()
        valores = self.root.treeview.item(focused)['values']

        self.root.var_tipo.set(valores[0])
        self.root.var_modelo.set(valores[1])
        self.root.var_ref.set(valores[2])

    def _resetear_inputs(self):
        self.root.var_tipo.set('')
        self.root.var_modelo.set('')
        self.root.var_ref.set('')

    def _resetear_labels(self):
        self.root.label_mensaje_tipo['text'] = ''
        self.root.label_mensaje_modelo['text'] = ''
        self.root.label_mensaje_ref['text'] = ''

    def _update_treeview(self):
        resultados = self.controller.get_registers()
        for item in self.root.treeview.get_children():
            self.root.treeview.delete(item)
        for resultado in resultados:
            self.root.treeview.insert(
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

    def _create_product(self):
        valida_tipo = self.validator.has_numbers_validation(
                        self.root.var_tipo.get(),
                        self.root.label_mensaje_tipo)
        valida_modelo = self.validator.empty_field_validation(
                        self.root.var_modelo.get(),
                        self.root.label_mensaje_modelo)
        valida_ref = self.validator.empty_field_validation(
                        self.root.var_ref.get(),
                        self.root.label_mensaje_ref)
        if (valida_tipo and valida_modelo and valida_ref):
            fecha_ingeso = date.datetime.now()
            id_registro_ingresado = self.controller.insert_product(
                self.root.var_tipo.get(),
                self.root.var_modelo.get(),
                self.root.var_ref.get(),
                fecha_ingeso
            )
            self.root.treeview.insert(
                "",
                "end",
                text=id_registro_ingresado,
                values=(
                    self.root.var_tipo.get(),
                    self.root.var_modelo.get(),
                    self.root.var_ref.get(),
                    fecha_ingeso
                )
            )
            self.root.label_mensaje['text'] = "Ingreso de Dispositivo exitoso"
            self._resetear_inputs()
            self._resetear_labels()
        else:
            self.root.label_mensaje['text'] = "Error en los datos ingresados, intente nuevamente"

    def _delete_product(self):
        focused = self.root.treeview.focus()
        id_a_eliminar = self.root.treeview.item(focused)['text']
        self.controller.delete_product(id_a_eliminar)
        self.root.treeview.delete(focused)
        self.root.label_mensaje['text'] = "Se dio de baja el registro: " + str(id_a_eliminar)
        self._resetear_inputs()

    def _modificar_en_treeview(self, item_a_modificar):
        # para no actualizar la fecha cuando se modifica el registro
        fecha_existente = self.root.treeview.item(item_a_modificar)['values'][3]
        nuevo_registro = (
            self.root.var_tipo.get(),
            self.root.var_modelo.get(),
            self.root.var_ref.get(),
            fecha_existente
        )
        self.root.treeview.item(item_a_modificar, values=nuevo_registro)

    def _edit_product(self):
        focused = self.root.treeview.focus()
        id_a_modificar = self.root.treeview.item(focused)['text']

        valida_tipo = self.validator.has_numbers_validation(
                        self.root.var_tipo.get(),
                        self.root.label_mensaje_tipo)
        valida_modelo = self.validator.empty_field_validation(
                        self.root.var_modelo.get(),
                        self.root.label_mensaje_modelo)
        valida_ref = self.validator.empty_field_validation(
                        self.root.var_ref.get(),
                        self.root.label_mensaje_ref)

        if (valida_tipo and valida_modelo and valida_ref):
            self.controller.update_product(
                self.root.var_tipo.get(),
                self.root.var_modelo.get(),
                self.root.var_ref.get(),
                id_a_modificar
            )
            self._modificar_en_treeview(focused)
            self.root.label_mensaje['text'] = "Actualización del Dispositivo " + str(id_a_modificar) + " exitosa"
        else:
            self.root.label_mensaje['text'] = "Error en los datos ingresados, intente nuevamente."
