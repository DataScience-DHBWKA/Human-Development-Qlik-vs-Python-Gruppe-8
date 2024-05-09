import os
import sys

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from Filtered_data import result_df
from python_param import output_file_path_filtered_data as output_file_path

# Exporting data to CSV file
result_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")