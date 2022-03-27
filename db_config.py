import sqlite3


def conexion_db():
    conexion = sqlite3.connect('proyecto.db')
    return conexion


# Tabla
def create_tablas(conexion):
    create_query = """
                    CREATE TABLE IF NOT EXISTS producto(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo varchar(50) NOT NULL,
                        modelo varchar(50) NOT NULL,
                        referencia varchar(255) NOT NULL,
                        fecha_insert DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                    """
    cursor = conexion.cursor()
    cursor.execute(create_query)
    conexion.commit()
    conexion.close()


def get_registros():
    query = """
            SELECT * FROM producto
            """
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados


# Inserts
def insert_producto(tipo, modelo, referencia):
    data = (tipo, modelo, referencia)
    query = """
            INSERT INTO producto
            (tipo,modelo,referencia)
            VALUES (?,?,?)
            """
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query, data)

    conexion.commit()
    conexion.close()


# Updates
# Posible error: a la hora de mandar el id ya debe ir como un entero
# al momento de ingresar a la función
def update_producto(tipo, modelo, referencia, id):
    data = (tipo, modelo, referencia, id)
    query = """
            UPDATE producto
            SET     tipo = ?,
                    modelo = ?,
                    referencia = ?
            WHERE id = ?
            """

    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query, data)

    conexion.commit()
    conexion.close()


# Delete
# Posible error: a la hora de mandar el id ya debe ir como un entero
# al momento de ingresar a la función
def delete_producto(id_producto):
    data = (id_producto,)
    query = """
            DELETE FROM producto
            WHERE id = ?;
            """

    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute(query, data)

    conexion.commit()
    conexion.close()


# if(conexion) conexion.close()
