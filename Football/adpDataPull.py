import requests
import json

year = '2017'
baseUrl = r'www03.myfantasyleague.com/%s/adpexport?TYPE=ADP' % year
paramDays = r'&TIME=30'
paramFranchises = r'&FRANCHISES=12'
paramPpr = r'&IS_PPR=1'
paramKpr = r'&IS_KEEPER=0'
paramMock = r'&IS_MOCK=-1'
paramInj = r'&INJURED=1'
paramCutoff = r'&CUTOFF='
paramJson = r'&JSON=1'

tst = r'http://www03.myfantasyleague.com/2017/export?TYPE=adp&FRANCHISES=12&JSON=1'

r = requests.get(tst)
data = json.loads(r.text)
print(data['adp']['totalDrafts'])
