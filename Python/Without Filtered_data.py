from Process_csv_files import process_csv_files

# Call the function with the folder path
folder_path = 'data'
result_df = process_csv_files(folder_path)

# Display the number of rows and columns in the DataFrame
num_rows, num_cols = result_df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)