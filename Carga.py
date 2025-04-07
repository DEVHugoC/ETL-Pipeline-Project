import GestionSQLite as gs

base_datos = 'bd_Ordenes_de_Compra.db'
tabla = 'Ordenes'

def carga(df_datos):
    conexion = gs.create_connection(base_datos)
    if conexion:
        if df_datos is not None:
            gs.preparar_tabla_para_insertar_datos(conexion, tabla)
            gs.insertar_datos_desde_dataframe(conexion, tabla, df_datos)       
        gs.close_connection