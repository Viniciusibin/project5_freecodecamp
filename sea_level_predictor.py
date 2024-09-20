import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importar os dados
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Criar o gráfico de dispersão (scatter plot)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Linha de melhor ajuste para todos os dados
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept + slope * years_extended, color='red', label='Best fit line 1880-2050')

    # 4. Linha de melhor ajuste a partir do ano 2000
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = pd.Series(range(2000, 2051))
    plt.plot(years_extended_2000, intercept_2000 + slope_2000 * years_extended_2000, color='green', label='Best fit line 2000-2050')

    # 5. Personalizar o gráfico
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # 6. Salvar a figura
    plt.savefig('sea_level_plot.png')

    return plt.gca()
