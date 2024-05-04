import pandas as pd
from Filtered_data import result_df
from Python_param import output_file_path

#Let's go export with csv
result_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")