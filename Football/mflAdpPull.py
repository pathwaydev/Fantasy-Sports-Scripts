'''
Python module to request xml adp fantasy football data from
myfantasyleague.com using site's standard API.
'''
# pylint: disable=C0103
import requests
from urllib.request import urlopen
import json
import itertools
import os
import re
import time
from pathlib import Path
import pandas as pd

# Generate paramaters for league rules and sizes
curYr = 2018
yrLst = list(range(curYr-4,curYr+1))
#yrLst = [2018]
isPprLst = ['&IS_PPR=%s' % (x) for x in ['0', '1']]
tmCntLst = ['&FRANCHISES=%s' % (x) for x in list(range(8,16,2))]

# Generate list of URLs for API pulls using cross product of configuration parameters
adpBaseUrlLst = ['https://www70.myfantasyleague.com/%s/export?TYPE=adp&JSON=1' % (yr) for yr in yrLst]
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
    plyrLkupUrl = 'https://www70.myfantasyleague.com/%s/export?TYPE=players&JSON=1' % (yr)
    
    time.sleep(10)
    #rAdp = requests.get(adpUrl)
    rAdp = urlopen(adpUrl).read().decode('utf8')
    #adpData = json.loads(rAdp.text)['adp']
    adpData = json.loads(rAdp)['adp']
    #rPlyr = requests.get(plyrLkupUrl)
    rPlyr = urlopen(plyrLkupUrl).read().decode('utf8')
    #plyrData = json.loads(rPlyr.text)['players']
    plyrData = json.loads(rPlyr)['players']

    adpDf = pd.DataFrame(adpData['player'])
    plyrDf = pd.DataFrame(plyrData['player'])
    combDf = pd.merge(adpDf, plyrDf, how='left', on='id')
    combDf['TEAM_COUNT'] = tmCnt
    combDf['PPR_FLG'] = pprFlg
    combDf['YEAR'] = int(yr)
    combDf['SRC_ADP'] = adpUrl
    combDf['SRC_PLYR'] = plyrLkupUrl
    print(adpUrl)
    return yr, tmCnt, pprFlg, combDf

def adpCsvGen(url):
    '''
    Function to generate CSVs of adp data cross-listed with player metadata.
    '''
    yr, tmCnt, pprFlg, df = getAdp(url)
    if pprFlg == '1':
        fmt = 'ppr'
    elif pprFlg == '0':
        fmt = 'std'
    curPth = os.path.dirname(os.path.abspath(__file__))
    outfileNm = 'data/adpData_%stm_%s_%s.csv' % (tmCnt, fmt, yr)
    outfile = Path(curPth) / outfileNm
    df.to_csv(outfile, index=False)

if __name__ == '__main__':
    [adpCsvGen(url) for url in adpUrlLst]
