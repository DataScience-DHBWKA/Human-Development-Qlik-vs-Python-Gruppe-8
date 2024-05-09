import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from python_param import folder_path
from Data_method.Process_csv_files import process_csv_files

# Call the function with the folder path
result_df = process_csv_files(folder_path)

# Display the number of rows and columns in the DataFrame
num_rows, num_cols = result_df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

# Create a heatmap to visualize missing values in the DataFrame
sns.heatmap(result_df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()