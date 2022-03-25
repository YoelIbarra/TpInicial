import sqlite3

conexion = sqlite3.connect('proyecto.db');

#Tabla
create_query =  """
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