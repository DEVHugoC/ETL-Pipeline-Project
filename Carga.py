
import GestionSQLite as gs

base_datos = 'bd_Ordenes_de_Compra.db'
tabla = 'Ordenes'

#Funcion que realiza la carga de los registros en una base de datos
def carga(df_datos):

    #Creamos una conexion a la base de datos
    conexion = gs.create_connection(base_datos)

    #Verificamos que la conexion se ha realizado
    if conexion:

        #Verificamos que el dataframe no se encuentre vacio
        if df_datos is not None:

            #Creamos la tabla en la base de datos
            gs.preparar_tabla_para_insertar_datos(conexion, tabla)

            #Insertamos los registros en la tabla creada
            gs.insertar_datos_desde_dataframe(conexion, tabla, df_datos)
        
        #Cerramos la conexion a la base de datos
        gs.close_connection