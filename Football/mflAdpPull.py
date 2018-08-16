'''
Python module to request xml adp fantasy football data from
myfantasyleague.com using site's standard API.
'''
# pylint: disable=C0103
import requests
import json
import itertools
import os
import re
from pathlib import Path
import pandas as pd

# Generate paramaters for league rules and sizes
curYr = 2018
yrLst = list(range(curYr-4,curYr+1))
isPprLst = ['&IS_PPR=%s' % (x) for x in ['0', '1']]
tmCntLst = ['&FRANCHISES=%s' % (x) for x in list(range(8,16,2))]

# Generate list of URLs for API pulls using cross product of configuration parameters
adpBaseUrlLst = ['http://www74.myfantasyleague.com/%s/export?TYPE=adp&JSON=1' % (yr) for yr in yrLst]
cfgLst = [''.join(x) for x in list(itertools.product(tmCntLst, isPprLst))]
adpUrlLst = [''.join(x) for x in list(itertools.product(adpBaseUrlLst,cfgLst))]

# Test Urls
'''
adpUrl = 'http://www03.myfantasyleague.com/2018/export?TYPE=adp&FRANCHISES=12&JSON=1'
'''

def getAdp(adpUrl):
    '''
    Function to grab ADP for league format and year specified in passed URL parameter.
    '''
    
    yr = re.findall(r'.com/(.*?)/', adpUrl)[0]
    tmCnt = re.findall(r'FRANCHISES=(.*?)&', adpUrl)[0]
    pprFlg = re.findall(r'IS_PPR=(\d*?)$', adpUrl)[0]
    plyrLkupUrl = 'https://www74.myfantasyleague.com/%s/export?TYPE=players&DETAILS=&SINCE=&PLAYERS=&JSON=1' % (yr)
    
    rAdp = requests.get(adpUrl)
    adpData = json.loads(rAdp.text)['adp']
    rPlyr = requests.get(plyrLkupUrl)
    plyrData = json.loads(rPlyr.text)['players']

    adpDf = pd.DataFrame(adpData['player'])
    plyrDf = pd.DataFrame(plyrData['player'])
    combDf = pd.merge(adpDf, plyrDf, how='left', on='id')
    combDf['TEAM_COUNT'] = tmCnt
    combDf['PPR_FLG'] = pprFlg
    return yr, tmCnt, pprFlg, combDf

df = getAdp(adpUrlLst[1])

curPth = os.path.dirname(os.path.abspath(__file__))
outfile = Path(curPth) / 'data/data.csv'

df.to_csv(outfile, index=False)
