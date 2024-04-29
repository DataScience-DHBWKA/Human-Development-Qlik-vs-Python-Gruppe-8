import seaborn as sns
import matplotlib.pyplot as plt
from Filtered_data import result_df

# Display the number of rows and columns in the DataFrame
num_rows, num_cols = result_df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

sns.heatmap(result_df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()