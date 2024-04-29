import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Filtered_data import result_df

columns_to_include = ['Country or Area', 'Year', 'GDP_per_capita_constant_dollar_2017','infant_mortality_rate',
                      'life_expectancy','refugees_origin','school_life_expextancy_ISCED_1-8','suicide_rates',
                      'total_fertility_rate','total_population']  

# pairplot
sns.pairplot(result_df[columns_to_include])
plt.suptitle('Pairplot des données', y=1.02) 
plt.show()