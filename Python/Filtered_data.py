from Process_csv_files import process_csv_files
from Python_param import folder_path

# Call the function with the folder path
result = process_csv_files(folder_path)

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
result_df = result[~result['Country or Area'].isin(regions_to_exclude)]