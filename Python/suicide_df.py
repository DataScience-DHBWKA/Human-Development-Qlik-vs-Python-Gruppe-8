import pandas as pd
from python_param import folder_path

suicide_df = pd.DataFrame()
suicide_df = pd.read_csv(folder_path + '/suicide_rates.csv')

for column in suicide_df.columns[1:]:
    # Extract point estimates from entries in the column
    suicide_df[column] = suicide_df[column].apply(lambda x: float(x.split()[0]) if isinstance(x, str) else x)