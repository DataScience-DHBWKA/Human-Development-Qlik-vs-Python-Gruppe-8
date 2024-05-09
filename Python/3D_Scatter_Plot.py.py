import os
import sys
import matplotlib.pyplot as plt

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from Filtered_data import result_df
from mpl_toolkits.mplot3d import Axes3D

# Select relevant columns
columns_to_include = ['GDP_per_capita_constant_dollar_2017', 'infant_mortality_rate', 'life_expectancy']

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d') # Adding a 3D subplot to the figure
ax.scatter(result_df[columns_to_include[0]], result_df[columns_to_include[1]], result_df[columns_to_include[2]], c='blue', marker='o')
ax.set_xlabel(columns_to_include[0])
ax.set_ylabel(columns_to_include[1])
ax.set_zlabel(columns_to_include[2])
ax.set_title('3D Scatter Plot of GDP per capita x infant mortality x life expectancy')
plt.show()