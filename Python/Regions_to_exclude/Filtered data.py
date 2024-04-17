import pandas as pd
import os

def process_csv_files(folder_path):
    # Get list of all CSV files in the folder
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

    # List to store DataFrames
    dfs = []

    for file_path in file_paths:
        df = pd.read_csv(file_path)

        # Rename columns
        df.rename(columns={
            'Year(s)': 'Year',
            'Time Period': 'Year', 
            'Reference Area': 'Country or Area',
            'Observation Value': 'Value', 
            'Country or territory of origin': 'Country or Area',
            'Refugees*': 'Value'},
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

        # Find rows where 'Year' column contains 'Footnote'
        rows_with_footnote = df[df['Year'] == 'Footnote']
        if not rows_with_footnote.empty:
            print(f"Footnote found in file: {file_path}")
            print(rows_with_footnote)

    # Merge the DataFrames based on 'Country or Area' and 'Year'
    combined_df = dfs[0]
    for df in dfs[1:]:
        combined_df = pd.merge(combined_df, df, on=['Country or Area', 'Year'], how='outer')

    # Regions to exclude
    regions_to_exclude = ['Africa', 'Asia', 'Australia/New Zealand', 'Australia/New Zealand', 'World', 'Eastern Africa',
                          'Eastern Africa', 'Eastern and South-Eastern Asia', 'Eastern Europe', 'High-income countries',
                          'Land-locked Developing Countries (LLDC)', 'Less developed regions, excluding China',
                          'Less developed regions',
                          'Less developed regions, excluding least developed countries',
                          'Small Island Developing States (SIDS)',
                          'No income group available', 'Northern Africa', 'Northern Africa and Western Asia',
                          'Northern America',
                          'Northern Europe', 'Low-income countries', 'Middle-income countries', 'More developed regions',
                          'Middle Africa',
                          'Eastern Asia', 'Soutern Asia', 'Western Europe', 'Upper-middle-income countries',
                          'Lower-middle-income countries',
                          'Europe', 'South-Eastern Asia', 'Southern Europe', 'Southern Asia', 'Southern Africa',
                          'Europe and Northern America',
                          'Central Asia', 'Central America', 'Central and Southern Asia', 'Sub-Saharan Africa',
                          'Least developed countries',
                          'Latin America and the Caribbean', 'Western Africa', 'South America', 'Western Asia']

    # Filter out regions
    filtered_combined_df = combined_df[~combined_df['Country or Area'].isin(regions_to_exclude)]

    indices_to_delete = [0, 1]
    df = filtered_combined_df.drop(indices_to_delete)

    return df

# Call the function with the folder path
folder_path = 'data'
result_df = process_csv_files(folder_path)

print(result_df.head())

# Display the number of rows and columns in the DataFrame
num_rows, num_cols = result_df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)