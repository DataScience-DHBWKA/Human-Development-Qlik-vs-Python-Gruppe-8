import os
import sys
import matplotlib.pyplot as plt

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from Data_method.Natural_disasters_df import natural_disasters_df

# Group the data by year and disaster type and count occurrences
natural_disasters_stacked = natural_disasters_df.groupby(['Year', 'Disaster Type']).size().unstack(fill_value=0)

# Plotting the stacked bar chart using DataFrame's plot method
natural_disasters_stacked.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Distribution of Natural Disaster Types Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Disasters')
plt.xticks(rotation=45)
plt.legend(title='Disaster Type')
plt.tight_layout()
plt.show()