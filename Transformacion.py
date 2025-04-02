
import pandas as pd

#Funcion que realiza la transformacion de los datos
def transformacion(df_datos):
    
    # Convertir los identificadores a tipo string 
    df_datos['RUC_PROVEEDOR'] = df_datos['RUC_PROVEEDOR'].astype('string')
    df_datos['RUC_ENTIDAD'] = df_datos['RUC_ENTIDAD'].astype('string')
    
    # Limpiar la columna de fecha reemplazando múltiples espacios por uno solo y quitar espacios en blanco
    df_datos['FECHA_FORMALIZACIÓN'] = df_datos['FECHA_FORMALIZACIÓN'].str.replace(r'\s+', ' ', regex=True).str.strip()
    
    # Convertir FECHA_FORMALIZACIÓN a datetime sin forzar un formato fijo, permitiendo que pandas infiera el correcto
    df_datos['FECHA_FORMALIZACIÓN'] = pd.to_datetime(df_datos['FECHA_FORMALIZACIÓN'],infer_datetime_format=True,errors='coerce') 
       
    # Crear nuevas columnas para día, mes y año
    df_datos['DIA'] = df_datos['FECHA_FORMALIZACIÓN'].dt.day
    df_datos['MES'] = df_datos['FECHA_FORMALIZACIÓN'].dt.month
    df_datos['AÑO'] = df_datos['FECHA_FORMALIZACIÓN'].dt.year

    # Reordenar las columnas para que FECHA_FORMALIZACIÓN, DIA, MES y AÑO estén juntos
    cols = df_datos.columns.tolist()
    for col in ['DIA', 'MES', 'AÑO']:
        if col in cols:
            cols.remove(col)
    fecha_index = cols.index('FECHA_FORMALIZACIÓN')
    nuevo_orden = cols[:fecha_index+1] + ['DIA', 'MES', 'AÑO'] + cols[fecha_index+1:]
    df_datos = df_datos[nuevo_orden]

    # Eliminamos las columnas vacías e irrelevantes
    columnas_a_eliminar = [
        'DESCRIPCIÓN_ESTADO', 'DESCRIPCIÓN_CESIÓN_DERECHOS',  # Vacías
        'FECHA_PROCESO', 'ORDEN_ELECTRÓNICA_GENERADA', 'ORDEN_DIGITALIZADA',
        'DOCUMENTO_ESTADO_OCAM', 'SUB_TOTAL', 'IGV', 'FECHA_ÚLTIMO_ESTADO'  # Irrelevantes
    ]
    df_datos = df_datos.drop(columns=columnas_a_eliminar, errors='ignore')
    
    # Convertir FECHA_FORMALIZACIÓN a string para la carga en SQLite
    df_datos['FECHA_FORMALIZACIÓN'] = df_datos['FECHA_FORMALIZACIÓN'].dt.strftime('%d/%m/%Y %H:%M:%S')
    
    return df_datos