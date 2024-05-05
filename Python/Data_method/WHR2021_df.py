import sys
import os
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from python_param import folder_path_2

WHR2021_df = pd.DataFrame()
WHR2021_df = pd.read_csv(folder_path_2 + '/WHR2021.csv')
WHR2021_df = WHR2021_df[['Country name', 'Ladder score']]
WHR2021_df.rename(columns={'Country name': 'Country or Area'}, inplace=True)
WHR2021_df.rename(columns={'Ladder Score': 'Value'}, inplace=True)