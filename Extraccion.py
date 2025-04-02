
import pandas as pd
import glob 
import pathlib 

#Funcion que extrae la informacion de un archivo csv
def extraccion_desde_csv(direccion_archivo_csv):
    dataframe = pd.read_csv(direccion_archivo_csv, encoding='latin1', sep=';') 
    return dataframe

#Funcion que extrae la informacion de un archivo json
def extraccion_desde_json(direccion_archivo_json):
    dataframe = pd.read_json(direccion_archivo_json, lines=True)
    return dataframe

#Funcion que extrae la informacion de un archivo XML
def extraccion_desde_xml(direccion_archivo_xml):
    dataframe = pd.read_xml(direccion_archivo_xml)
    return dataframe


#Funcion que extrae los datos de todos los archivos
def extraccion():

    df_datos_extraidos = pd.DataFrame(columns=['FECHA_PROCESO', 'RUC_PROVEEDOR', 'PROVEEDOR', 'RUC_ENTIDAD', 'ENTIDAD', 'TIPO_PROCEDIMIENTO', 
                                               'ORDEN_ELECTRÓNICA', 'ORDEN_ELECTRÓNICA_GENERADA', 'ESTADO_ORDEN_ELECTRÓNICA', 'DOCUMENTO_ESTADO_OCAM', 
                                               'FECHA_FORMALIZACIÓN', 'FECHA_ÚLTIMO_ESTADO', 'SUB_TOTAL', 'IGV', 'TOTAL', 'ORDEN_DIGITALIZADA', 
                                               'DESCRIPCIÓN_ESTADO', 'DESCRIPCIÓN_CESIÓN_DERECHOS', 'ACUERDO_MARCO'])

    carpeta_datos = pathlib.Path(__file__).parent / "ARCHIVOS"

    for archivos_csv in glob.glob(f'{carpeta_datos}/*.csv'): 
        df_datos_extraidos = pd.concat([df_datos_extraidos, extraccion_desde_csv(archivos_csv)], axis=0, ignore_index=True)

    for archivos_json in glob.glob(f'{carpeta_datos}/*.json'):
        df_datos_extraidos = pd.concat([df_datos_extraidos, extraccion_desde_json(archivos_json)], axis=0, ignore_index=True)

    for archivos_xml in glob.glob(f'{carpeta_datos}/*.xml'):
        df_datos_extraidos = pd.concat([df_datos_extraidos, extraccion_desde_xml(archivos_xml)], axis=0, ignore_index=True)

    return df_datos_extraidos

