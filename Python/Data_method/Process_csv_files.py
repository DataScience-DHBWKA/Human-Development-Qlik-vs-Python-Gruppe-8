import sys
import os
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from python_param import folder_path

# Define a function to process CSV files in a given folder
def process_csv_files(folder_path):
    # Get list of all CSV files in the folder
    files_to_exclude = ['natural_disasters.csv', 'WHR2021.csv']
    file_paths = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv') and file not in files_to_exclude:
            file_paths.append(os.path.join(folder_path, file))

    # List to store DataFrames
    dfs = []

    # Iterate through each CSV file
    for file_path in file_paths:
        df = pd.read_csv(file_path)

        # Rename columns
        df.rename(columns={'Year(s)': 'Year', 'Time Period': 'Year', 'Reference Area': 'Country or Area',
                           'Observation Value': 'Value', 'Country or territory of origin': 'Country or Area',
                           'Refugees*': 'Value', 'Countries, territories and areas': 'Country or Area'},
                  inplace=True)

        # Filter out rows with year 2101
        df = df[df['Year'] != 2101]

        # Filter rows where 'Sex' column is 'all genders'
        if 'Sex' in df.columns:
            df = df[df['Sex'] == 'All genders']

        # Filter columns
        df = df[['Country or Area', 'Year', 'Value']]

        # Convert data types
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')  # Convert to numeric, coerce errors to NaN
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')  # Convert to numeric, coerce errors to NaN

        # Extract the last part of the file path as the column suffix
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        # Create custom column names
        custom_names = [f'{file_name}' if col == 'Value' else col for col in ['Country or Area', 'Year', 'Value']]

        # Rename columns
        df.columns = custom_names
        dfs.append(df)

    # Merge the DataFrames based on 'Country or Area' and 'Year'
    combined_df = dfs[0]
    for df in dfs[1:]:
        combined_df = pd.merge(combined_df, df, on=['Country or Area', 'Year'], how='outer')

    # Multiply 'total_population' column by 1000
    combined_df["total_population"] *= 1000

    return combined_df