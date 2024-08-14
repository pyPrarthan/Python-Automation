#Extracting CSV file from URL 

import pandas as pd

football = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E1.csv')

#Chaning the column name 
football.rename(columns={'AvgCAHH':'home_goals', 
                        'AvgCAHA':'away_goals'},inplace=True)

print(football)