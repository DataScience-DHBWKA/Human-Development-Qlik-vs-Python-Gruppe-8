import pandas as pd
from Python_param import folder_path

natural_disasters_df = pd.DataFrame()
natural_disasters_df = pd.read_csv(folder_path + '/natural_disasters.csv')