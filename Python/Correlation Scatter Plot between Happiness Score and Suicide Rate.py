import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_method.Suicide_df import suicide_df
from Data_method.WHR2021_df import WHR2021_df

# Correlation Scatter Plot between Happiness Score and Suicide Rate

# Merge the dataframes on 'Country or Area'
merged_df = pd.merge(WHR2021_df, suicide_df, left_on='Country or Area', right_on='Countries, territories and areas', how='inner')

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='Ladder score', y='Value', hue='Country or Area', palette='viridis')
plt.title('Correlation between Happiness Score and Suicide Rate (2019)')
plt.xlabel('Happiness Score')
plt.ylabel('Suicide Rate')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()