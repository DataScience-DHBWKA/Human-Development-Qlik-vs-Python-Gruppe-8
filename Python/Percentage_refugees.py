import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

# Load filtered data for the period from 1975 to 2021
from Filtered_data import result_df

# Filter data for the period from 1975 to 2021
result_df_period = result_df[(result_df['Year'] >= 1975) & (result_df['Year'] <= 2021)]

# Calculate the total number of refugees for each year
total_refugees_per_year = result_df_period.groupby('Year')['refugees_origin'].sum()

# Estimated world population for each year (Source: United Nations)
world_population_per_year = {
    1975: 4.07e9, 1976: 4.13e9, 1977: 4.19e9, 1978: 4.25e9, 1979: 4.31e9,
    1980: 4.37e9, 1981: 4.43e9, 1982: 4.49e9, 1983: 4.55e9, 1984: 4.61e9,
    1985: 4.67e9, 1986: 4.73e9, 1987: 4.79e9, 1988: 4.85e9, 1989: 4.92e9,
    1990: 5.01e9, 1991: 5.11e9, 1992: 5.21e9, 1993: 5.31e9, 1994: 5.41e9,
    1995: 5.51e9, 1996: 5.61e9, 1997: 5.71e9, 1998: 5.81e9, 1999: 5.91e9,
    2000: 6.01e9, 2001: 6.11e9, 2002: 6.21e9, 2003: 6.31e9, 2004: 6.41e9,
    2005: 6.51e9, 2006: 6.61e9, 2007: 6.71e9, 2008: 6.81e9, 2009: 6.91e9,
    2010: 7.01e9, 2011: 7.11e9, 2012: 7.21e9, 2013: 7.31e9, 2014: 7.4e9,
    2015: 7.48e9, 2016: 7.55e9, 2017: 7.62e9, 2018: 7.68e9, 2019: 7.74e9,
    2020: 7.79e9, 2021: 7.84e9
}

# Calculate the percentage of refugees compared to the world population for each year
percentage_refugees_per_year = (total_refugees_per_year / pd.Series(world_population_per_year)) * 100

# Smooth the data using spline interpolation
x_smooth = np.linspace(percentage_refugees_per_year.index.min(), percentage_refugees_per_year.index.max(), 300)
y_smooth = make_interp_spline(percentage_refugees_per_year.index, percentage_refugees_per_year.values)(x_smooth)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x_smooth, y_smooth, linestyle='-', color='blue')

# Add data labels
for year, percentage in zip(percentage_refugees_per_year.index, percentage_refugees_per_year.values):
    plt.text(year, percentage, f'{percentage:.2f}', ha='center', va='bottom', fontsize=8)

plt.title('Percentage of World Population That Are Refugees (1975-2021)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Refugees to World Population', fontsize=12)
plt.grid(True)
plt.xticks(range(1975, 2022, 2))
plt.tight_layout()

plt.show()