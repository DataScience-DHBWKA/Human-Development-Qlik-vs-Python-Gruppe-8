import sys
import os

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from Data_method.Natural_disasters_df import natural_disasters_df
from python_param import output_file_path_Natural_disasters_df as output_file_path

# Exporting data to CSV file
natural_disasters_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")