import warnings
from datetime import datetime

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

#Importamos los archivos para el uso de las funciones
import Extraccion as ex
import Transformacion as tr
import Carga as ca
import Visualizacion  

#Inicio del proceso
tiempo = datetime.now()
print('Inicio del proceso ETL: ', tiempo)

#Extraemos los datos
data_extraida = ex.extraccion()

#Transformamos los datos
data_transformada = tr.transformacion(data_extraida)

#Cargamos los datos a la base de datos
ca.carga(data_transformada)

#Fin del proceso
tiempo = datetime.now()
print('Fin del proceso ETL: ', tiempo)

# Ejecutar la visualización
Visualizacion.visualize_data()