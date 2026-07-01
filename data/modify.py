#Using statistics, teams, and seasons, calculate the average points per game (PTS / G) for every team in each season.
import pandas as pd

stats= pd.read_csv("teams_stats1.csv")

stats['Season_ID']+=2000
print(stats)

stats.to_csv("teams_stats.csv", index=False)