import sys
import os
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from python_param import folder_path_2

suicide_df = pd.DataFrame()
suicide_df = pd.read_csv(folder_path_2 + '/suicide_rates.csv')

for column in suicide_df.columns[1:]:
    # Extract point estimates from entries in the column
    suicide_df[column] = suicide_df[column].apply(lambda x: float(x.split()[0]) if isinstance(x, str) else x)