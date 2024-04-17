from Filtered_data import result_df

result_df_year = result_df[result_df['Year'] == 2021] 

total_refugees = result_df_year['refugees_origin'].sum()

# Berechnen Sie den Prozentsatz der Flüchtlinge im Vergleich zur Weltbevölkerung
world_population = 7.9e9  # geschätzte weltweite Bevölkerung
percentage_refugees = (total_refugees / world_population) * 100

print("Prozentsatz der Weltbevölkerung, der Flüchtlinge ist:", percentage_refugees)
