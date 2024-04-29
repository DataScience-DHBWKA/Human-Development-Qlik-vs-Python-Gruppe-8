import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Filtered_data import result_df
import geopandas as gpd

# Filter data for the year
result_df_year = result_df[result_df['Year'] == "2021"]

# Load world map shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge world map with data
world = world.merge(result_df, how='left', left_on='name', right_on='Country or Area')

# Plot the geographical heatmap
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.plot(column='GDP_per_capita_constant_dollar_2017', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('GDP per Capita (Constant 2017 $) - Geographical Heatmap')
plt.show()