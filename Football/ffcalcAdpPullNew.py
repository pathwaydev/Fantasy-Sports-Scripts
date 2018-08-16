'''
Python module to request xml adp fantasy football data from
fantasyfootballcalculator.com using site's standard API.
'''
# pylint: disable=C0103
import requests
import json
import pandas as pd

url = 'https://fantasyfootballcalculator.com/api/v1/adp/standard?teams=12&year=2018'
r = requests.get(url)
rStr = r.text
data = json.loads(rStr)
adpData = data['players']
df = pd.DataFrame(adpData)

print(df.head())
