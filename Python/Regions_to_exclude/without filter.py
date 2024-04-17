import pandas as pd
import os

# Folder path containing CSV files
folder_path = 'data' # "Medium" predictions are used

# Get list of all CSV files in the folder
file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

# List to store DataFrames
dfs = []

# Read each CSV file into a DataFrame and rename columns
for file_path in file_paths:
    df = pd.read_csv(file_path)
    
    # Rename column 'Year(s)' to 'Year'
    df.rename(columns={'Year(s)': 'Year', 'Time Period': 'Year', 'Reference Area': 'Country or Area', 'Observation Value': 'Value'}, 
              inplace=True)

    df = df[(df['Year'] != 2101)]
    
    if 'Sex' in df.columns:
        # Filter rows where 'sex' column is 'all genders'
        df = df[df['Sex'] == 'All genders']
    
    # Filter columns
    df = df[['Country or Area', 'Year', 'Value']]
    
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

# Display the number of rows and columns in the DataFrame
num_rows, num_cols = combined_df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)