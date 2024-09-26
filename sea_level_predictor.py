import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_csv('epa-sea-level.csv')
df

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Datos observados', color='blue')
plt.show()

slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_all = pd.Series([i for i in range(1880, 2051)])
sea_levels_all = intercept_all + slope_all * years_all
plt.plot(years_all, sea_levels_all, 'r', label='Línea de ajuste (1880-2050)', linewidth=2)
plt.show()

df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent = pd.Series([i for i in range(2000, 2051)])
sea_levels_recent = intercept_recent + slope_recent * years_recent
plt.plot(years_recent, sea_levels_recent, 'g', label='Línea de ajuste (2000-2050)', linewidth=2)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Datos observados')
plt.xlabel('Año')
plt.ylabel('Nivel del mar ajustado de CSIRO (inches)')
plt.title('Datos del Nivel del Mar (1880 - Presente)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Datos observados')
plt.plot(years_all, sea_levels_all, 'r', label='Línea de ajuste (1880-2050)', linewidth=2)

plt.xlabel('Año')
plt.ylabel('Nivel del mar ajustado de CSIRO (inches)')
plt.title('Nivel del Mar con Línea de Ajuste (1880 - 2050)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Datos observados')
plt.plot(years_all, sea_levels_all, 'r', label='Línea de ajuste (1880-2050)', linewidth=2)
plt.plot(years_recent, sea_levels_recent, 'g', label='Línea de ajuste (2000-2050)', linewidth=2)

plt.xlabel('Año')
plt.ylabel('Nivel del mar ajustado de CSIRO (inches)')
plt.title('Nivel del Mar con Líneas de Ajuste (1880-2050 y 2000-2050)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()







