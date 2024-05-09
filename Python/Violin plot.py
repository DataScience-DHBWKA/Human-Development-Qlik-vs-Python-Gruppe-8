import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from Filtered_data import result_df

# Select relevant columns
columns_to_include = ['GDP_per_capita_constant_dollar_2017', 'infant_mortality_rate', 'life_expectancy', 'total_population']

# Create a violin plot
plt.figure(figsize=(10, 8))
sns.violinplot(data=result_df[columns_to_include], inner="points")
plt.title('Violin Plot of Key Variables')
plt.show()