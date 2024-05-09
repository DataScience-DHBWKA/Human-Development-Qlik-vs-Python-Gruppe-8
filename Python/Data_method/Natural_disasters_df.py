import os
import sys
import pandas as pd

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from python_param import folder_path_2

natural_disasters_df = pd.DataFrame()

# Reading the natural disasters data from CSV file
natural_disasters_df = pd.read_csv(folder_path_2 + '/natural_disasters.csv')