import pyodbc

def connect_to_db():
    server = 'DESKTOP-HT4NA4R'  # Cambia esto por el nombre de tu servidor
    database = 'BdRest'  # Cambia esto por el nombre de tu base de datos
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print("Error al conectar:", e)
        return None
