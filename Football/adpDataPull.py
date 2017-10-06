import requests
import json
from datetime import datetime as dt
import pandas as pd
import numpy as np
import re

adpUrls = []
currYr = dt.now().year
pprMd = [0,1]

paramDays = r'&TIME='
paramFranchises = r'&FRANCHISES=12'
paramPpr = r'&IS_PPR=1'
paramKpr = r'&IS_KEEPER='
paramMock = r'&IS_MOCK=-1'
paramInj = r'&INJURED='
paramCutoff = r'&CUTOFF='
paramJson = r'&JSON=1'

for yr in range(currYr-3, currYr+1):
    for md in pprMd:
        paramPpr = r'&IS_PPR=%d' % (md)
        baseUrl = r'http://www03.myfantasyleague.com/%s/export?TYPE=adp' % yr
        url = (baseUrl + paramDays + paramFranchises
               + paramPpr + paramMock + paramInj
               + paramJson)
        adpUrls.append(url)

for url in adpUrls:
    yr = re.findall(".com/([0-9].*)/", url)[0]

    if r'IS_PPR=1' in url:
        pprFlg = 1
    else:
        pprFlg = 0

    plyrId = []
    avgPick = []
    draftCnt = []

    r = requests.get(url)
    data = json.loads(r.text)
    totDrafts = data['adp']['totalDrafts']
    adpData = data['adp']['player']

    for v in adpData:
        plyrId.append(v['id'])
        avgPick.append(v['averagePick'])
        draftCnt.append(v['draftsSelectedIn'])

    df = pd.DataFrame(
        np.column_stack([plyrId, avgPick, draftCnt]),
        columns = ['plyrId', 'avgPick', 'draftCnt']
    )
    df['totDrafts'] = totDrafts
    df['pprFlg'] = pprFlg
    df['year'] = yr
    if pprFlg == 0:
        frmt = 'Std'
    else:
        frmt = 'Ppr'

    df = df.drop_duplicates(['plyrId'], keep='first')
    df.to_csv(r'data/adpByPlyrId%s%s.csv' % (frmt, yr), index=False)
