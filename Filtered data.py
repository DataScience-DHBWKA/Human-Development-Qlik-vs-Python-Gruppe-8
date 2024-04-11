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

# regions to filter out (NOT READY, ONLY SOME SELECTED), no list found to differ from country and area
regions_to_exclude = ['Africa', 'Asia', 'Australia/New Zealand', 'Australia/New Zealand', 'World', 'Eastern Africa', 
                      'Eastern Africa', 'Eastern and South-Eastern Asia', 'Eastern Europe', 'High-income countries', 
                      'Land-locked Developing Countries (LLDC)', 'Less developed regions, excluding China', 'Less developed regions', 
                      'Less developed regions, excluding least developed countries', 'Small Island Developing States (SIDS)', 
                      'No income group available', 'Northern Africa', 'Northern Africa and Western Asia', 'Northern America', 
                      'Northern Europe', 'Low-income countries', 'Middle-income countries', 'More developed regions', 'Middle Africa', 
                      'Eastern Asia', 'Soutern Asia', 'Western Europe', 'Upper-middle-income countries', 'Lower-middle-income countries', 
                      'Europe', 'South-Eastern Asia', 'Southern Europe', 'Southern Asia', 'Southern Africa', 'Europe and Northern America', 
                      'Central Asia', 'Central America', 'Central and Southern Asia', 'Sub-Saharan Africa', 'Least developed countries', 
                      'Latin America and the Caribbean', 'Western Africa', 'South America', 'Western Asia']

def filter_regions(df, regions_to_exclude):
    filtered_df = df[~df['Country or Area'].isin(regions_to_exclude)]
    return filtered_df

# filter out regions
filtered_combined_df = filter_regions(combined_df, regions_to_exclude)

print(filtered_combined_df.head())

#Let's go export with csv
output_file_path = 'filtered_data.csv'
filtered_combined_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")