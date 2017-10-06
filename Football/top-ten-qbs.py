import nfldb
import pandas as pd
import matplotlib.pyplot as plt

db = nfldb.connect()
q = nfldb.Query(db)

dict = {
    'name': [],
    'yds': []
}

q.game(season_year=2017, season_type='Regular')
for pp in q.sort('passing_yds').limit(10).as_aggregate():
    dict['name'].append(pp.player)
    dict['yds'].append(pp.passing_yds)
    #print pp.player, pp.passing_yds, pp.passing_tds, pp.passing_int

df = pd.DataFrame(dict)
print df

df.plot(kind='barh', x='name')
plt.show()
