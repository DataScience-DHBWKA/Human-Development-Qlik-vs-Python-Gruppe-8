import matplotlib.pyplot as plt
import seaborn as sns
from Data_method.Natural_disasters_df import natural_disasters_df

# Stacked Bar Chart
natural_disasters_stacked = natural_disasters_df.groupby(['Year', 'Disaster Type']).size().unstack(fill_value=0)

# Plot stacked bar chart
natural_disasters_stacked.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Distribution of Natural Disaster Types Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Disasters')
plt.xticks(rotation=45)
plt.legend(title='Disaster Type')
plt.tight_layout()
plt.show()