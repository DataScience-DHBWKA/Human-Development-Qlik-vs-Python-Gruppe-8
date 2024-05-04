import pandas as pd
from Python_param import folder_path_2

natural_disasters_df = pd.DataFrame()
natural_disasters_df = pd.read_csv(folder_path_2 + '/natural_disasters.csv')