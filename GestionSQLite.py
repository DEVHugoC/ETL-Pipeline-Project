import sqlite3

def create_connection(db_name):     
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        print(f"Conexión exitosa a {db_name}")
    except sqlite3.Error as e:
        print(f"Error al conectar: {e}")
    return connection

def close_connection(connection):    
    if connection:
        connection.close()
        print("Conexión cerrada.")
    
def preparar_tabla_para_insertar_datos(connection: sqlite3.Connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            RUC_PROVEEDOR TEXT,
            PROVEEDOR TEXT,
            RUC_ENTIDAD TEXT,
            ENTIDAD TEXT,
            TIPO_PROCEDIMIENTO TEXT,
            ORDEN_ELECTRÓNICA TEXT,
            ESTADO_ORDEN_ELECTRÓNICA TEXT,
            FECHA_FORMALIZACIÓN TEXT,
            DIA INTEGER,
            MES INTEGER,
            AÑO INTEGER,
            nombreMes TEXT,
            TOTAL REAL,
            ACUERDO_MARCO TEXT
        )
    """)
    cursor.execute(f"DELETE FROM {table_name}")
    connection.commit()
    print(f"Se preparó la tabla {table_name} para insertar los datos")

def insertar_datos_desde_dataframe(connection: sqlite3.Connection, table_name: str, df_datos):
    cursor = connection.cursor()   
    for _, record in df_datos.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (
                RUC_PROVEEDOR, PROVEEDOR, RUC_ENTIDAD, ENTIDAD, TIPO_PROCEDIMIENTO, 
                ORDEN_ELECTRÓNICA, ESTADO_ORDEN_ELECTRÓNICA, FECHA_FORMALIZACIÓN, 
                DIA, MES, AÑO, nombreMes, TOTAL, ACUERDO_MARCO
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            record['RUC_PROVEEDOR'],
            record['PROVEEDOR'],
            record['RUC_ENTIDAD'],
            record['ENTIDAD'],
            record['TIPO_PROCEDIMIENTO'],
            record['ORDEN_ELECTRÓNICA'],
            record['ESTADO_ORDEN_ELECTRÓNICA'],
            record['FECHA_FORMALIZACIÓN'],
            record['DIA'],
            record['MES'],
            record['AÑO'],
            record['nombreMes'],            
            record['TOTAL'],
            record['ACUERDO_MARCO']
        ))
    connection.commit()
    print("Datos insertados correctamente.")