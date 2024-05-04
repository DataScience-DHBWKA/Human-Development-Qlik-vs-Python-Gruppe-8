import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Data_method.Natural_disasters_df import natural_disasters_df
from Python_param import output_file_path_Natural_disasters_df as output_file_path

#Let's go export with csv
natural_disasters_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")