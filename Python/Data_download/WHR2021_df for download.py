import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Data_method.WHR2021_df import WHR2021_df
from python_param import output_file_path_WHR2021_df as output_file_path

#Let's go export with csv
WHR2021_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")