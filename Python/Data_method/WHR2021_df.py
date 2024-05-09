import os
import sys
import pandas as pd

# Importing necessary modules
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Getting the parent directory path
sys.path.append(parent_dir) # Appending parent directory to system path for module import
from python_param import folder_path_2

WHR2021_df = pd.DataFrame()
# Reading the WHR2021 data from CSV file
WHR2021_df = pd.read_csv(folder_path_2 + '/WHR2021.csv')

# Selecting specific columns
WHR2021_df = WHR2021_df[['Country name', 'Ladder score']]

# Renaming columns for clarity
WHR2021_df.rename(columns={'Country name': 'Country or Area'}, inplace=True)
WHR2021_df.rename(columns={'Ladder Score': 'Value'}, inplace=True)