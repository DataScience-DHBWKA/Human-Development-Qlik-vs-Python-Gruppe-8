import pandas as pd
from Filtered_data import result_df

#Let's go export with csv
output_file_path = 'filtered_data.csv'
result_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")