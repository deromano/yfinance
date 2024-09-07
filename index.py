import yfinance as yf
import pandas as pd
from datetime import datetime

# Definir el símbolo de la acción y el rango de fechas
simbolo = "AAPL"
fecha_inicio = "2020-01-01"
fecha_fin = datetime.now().strftime("%Y-%m-%d")

# Descargar los datos
aapl = yf.Ticker(simbolo)
df = aapl.history(start=fecha_inicio, end=fecha_fin)

# Guardar los datos en un archivo CSV
nombre_archivo = f"{simbolo}cotizaciones{fecha_inicio}a{fecha_fin}.csv"
df.to_csv(nombre_archivo)

print(f"Los datos se han guardado en {nombre_archivo}")

# Mostrar las primeras filas de los datos
print(df.head())