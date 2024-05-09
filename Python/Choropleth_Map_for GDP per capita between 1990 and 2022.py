import os
import sys
import plotly.express as px

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from Filtered_data import result_df

# Filter data between 1990 and 2022
filtered_result_df = result_df[(result_df['Year'] >= 1990) & (result_df['Year'] <= 2022)]

# Choropleth Map for GDP per capita between 1990 and 2022
# Create a choropleth map using Plotly Express
fig = px.choropleth(filtered_result_df, 
                    locations="Country or Area", 
                    locationmode='country names',
                    color="GDP_per_capita_constant_dollar_2017", 
                    hover_name="Country or Area", 
                    animation_frame="Year", 
                    title="Global Distribution of GDP per capita (1980-2022)")
fig.update_geos(projection_type="natural earth")
fig.show()
