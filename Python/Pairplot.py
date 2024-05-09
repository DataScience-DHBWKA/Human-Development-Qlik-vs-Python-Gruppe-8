import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from Filtered_data import result_df

# Columns to include in the pairplot
columns_to_include = ['Country or Area', 'Year', 'GDP_per_capita_constant_dollar_2017','infant_mortality_rate',
                      'life_expectancy','refugees_origin','school_life_expextancy_ISCED_1-8','suicide_rates',
                      'total_fertility_rate','total_population']  

# pairplot
sns.pairplot(result_df[columns_to_include])
plt.suptitle('Pairplot des données', y=1.02) 
plt.show()