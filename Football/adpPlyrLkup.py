import requests
import json
import pandas as pd
import numpy as np

plyrsYr = {
    '2017': r'https://www71.myfantasyleague.com/2017/export?TYPE=players&DETAILS=&SINCE=&PLAYERS=&JSON=1',
    '2016': r'https://www71.myfantasyleague.com/2016/export?TYPE=players&DETAILS=&SINCE=&PLAYERS=&JSON=1',
    '2015': r'https://www71.myfantasyleague.com/2015/export?TYPE=players&DETAILS=&SINCE=&PLAYERS=&JSON=1',
    '2014': r'https://www71.myfantasyleague.com/2014/export?TYPE=players&DETAILS=&SINCE=&PLAYERS=&JSON=1'
}

selectedYr = list(range(2014,2017+1))

for yr in selectedYr:
    plyrId = []
    firstName = []
    lastName = []
    pos = []
    tm = []
    r = requests.get(plyrsYr[str(yr)])
    data = json.loads(r.text)
    plyrData = data['players']['player']
    for v in plyrData:
        plyrId.append(v['id'])
        firstName.append(v['name'].split(',')[1].strip())
        lastName.append(v['name'].split(',')[0].strip())
        pos.append(v['position'])
        tm.append(v['team'])

        df = pd.DataFrame(
            np.column_stack([plyrId, firstName, lastName, pos, tm]),
            columns = ['plyrId', 'firstNm', 'lastNm', 'pos', 'tm']
        )
        df = df.drop_duplicates(['plyrId'], keep='first')

        df.to_csv(r'data/plyrLkup%d.csv' % yr, index=False)
