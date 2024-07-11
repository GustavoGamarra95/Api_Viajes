import sqlite3


# Función para mostrar las tablas de la base de datos
def show_tables(conn):
    try:
        cursor = conn.cursor()
        # Consulta SQL para obtener los nombres de las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Imprimir los nombres de las tablas
        if tables:
            print("Tablas en la base de datos:")
            for table in tables:
                print(table[0])
        else:
            print("No se encontraron tablas en la base de datos.")

    except sqlite3.Error as e:
        print(f"Error al mostrar las tablas: {e}")


# Conexión a la base de datos
def connect_to_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conectado a la base de datos: {db_file}")
        return conn

    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


# Ejemplo de uso
if __name__ == "__main__":
    db_file = "storage.db"  # Reemplaza con la ruta a tu archivo de base de datos
    conn = connect_to_database(db_file)

    if conn:
        show_tables(conn)
        conn.close()
        print("las tablas existen.")
