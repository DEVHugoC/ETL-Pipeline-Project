import Extraccion as ex
import Transformacion as tr
import Carga as ca
import Visualizacion  
import warnings
from datetime import datetime

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

tiempo = datetime.now()
print('Inicio del proceso ETL: ', tiempo)
data_extraida = ex.extraccion()
data_transformada = tr.transformacion(data_extraida)
ca.carga(data_transformada)
tiempo = datetime.now()
print('Fin del proceso ETL: ', tiempo)

# Visualizacion.visualize_data()