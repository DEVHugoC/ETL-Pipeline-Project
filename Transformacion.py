import pandas as pd

def transformacion(df_datos):
    
    df_datos['RUC_PROVEEDOR'] = df_datos['RUC_PROVEEDOR'].astype('string')
    df_datos['RUC_ENTIDAD'] = df_datos['RUC_ENTIDAD'].astype('string')
    
    df_datos['FECHA_FORMALIZACIÓN'] = df_datos['FECHA_FORMALIZACIÓN'].str.replace(r'\s+', ' ', regex=True).str.strip()
    df_datos['FECHA_FORMALIZACIÓN'] = pd.to_datetime(df_datos['FECHA_FORMALIZACIÓN'],infer_datetime_format=True,errors='coerce') 
       
    df_datos['DIA'] = df_datos['FECHA_FORMALIZACIÓN'].dt.day
    df_datos['MES'] = df_datos['FECHA_FORMALIZACIÓN'].dt.month
    df_datos['AÑO'] = df_datos['FECHA_FORMALIZACIÓN'].dt.year

    meses = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
        9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    df_datos['nombreMes'] = df_datos['MES'].map(meses)

    orden_meses = list(meses.values())
    df_datos['nombreMes'] = pd.Categorical(df_datos['nombreMes'], categories=orden_meses, ordered=True)

    cols = df_datos.columns.tolist()
    for col in ['DIA', 'MES', 'AÑO', 'nombreMes']:
        if col in cols:
            cols.remove(col)
    fecha_index = cols.index('FECHA_FORMALIZACIÓN')
    nuevo_orden = cols[:fecha_index+1] + ['DIA', 'MES', 'AÑO', 'nombreMes'] + cols[fecha_index+1:]
    df_datos = df_datos[nuevo_orden]

    columnas_a_eliminar = [
        'DESCRIPCIÓN_ESTADO', 'DESCRIPCIÓN_CESIÓN_DERECHOS',  
        'FECHA_PROCESO', 'ORDEN_ELECTRÓNICA_GENERADA', 'ORDEN_DIGITALIZADA',
        'DOCUMENTO_ESTADO_OCAM', 'SUB_TOTAL', 'IGV', 'FECHA_ÚLTIMO_ESTADO'  
    ]
    df_datos = df_datos.drop(columns=columnas_a_eliminar, errors='ignore')
    
    df_datos['FECHA_FORMALIZACIÓN'] = df_datos['FECHA_FORMALIZACIÓN'].dt.strftime('%d/%m/%Y %H:%M:%S')
    
    return df_datos

