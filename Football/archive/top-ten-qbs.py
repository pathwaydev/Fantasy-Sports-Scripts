import nfldb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2017, season_type='Regular')
for pp in q.sort('receiving_yds').limit(10).as_aggregate():
    print pp.player, pp.receiving_yds

dict = {
    'name': [],
    'yds': []
}

q.game(season_year=2017, season_type='Regular')
for pp in q.sort('receiving_yds').limit(10).as_aggregate():
    dict['name'].append(pp.player)
    dict['yds'].append(pp.receiving_yds)
    #print pp.player, pp.passing_yds, pp.passing_tds, pp.passing_int
