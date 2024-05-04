import sys
import os
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Python_param import folder_path_2

natural_disasters_df = pd.DataFrame()
natural_disasters_df = pd.read_csv(folder_path_2 + '/natural_disasters.csv')