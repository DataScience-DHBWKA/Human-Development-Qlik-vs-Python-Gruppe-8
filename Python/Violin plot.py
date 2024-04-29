import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Filtered_data import result_df

# Select relevant columns
columns_to_include = ['GDP_per_capita_constant_dollar_2017', 'infant_mortality_rate', 'life_expectancy', 'total_population']

# Create a violin plot
plt.figure(figsize=(10, 8))
sns.violinplot(data=result_df[columns_to_include], inner="points")
plt.title('Violin Plot of Key Variables')
plt.show()