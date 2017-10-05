'''
sandbox
'''
# pylint: disable=C0103
import nfldb
import pandas as pd
import numpy as np
from plyrStatsPull import plyrStatsPull
from scoreCfg import ptsLst

adpFile = r'data/adp_2016_12tm_standard.csv'

df_start = pd.read_csv(adpFile)
df = df_start
df_final = pd.DataFrame()

row_iterator = df.iterrows()
for i,row in row_iterator:
    try:
        adpPlyr = row['name']
        if row['team'] == 'LAC':
            adpTeam = 'SD'
        elif row['team'] == 'JAC':
            adpTeam = 'JAX'
        elif row['team'] == 'LAR':
            adpTeam = 'LA'
        else:
            adpTeam = row['team']
        if row['pos'] != 'PK':
            adpPos = row['pos']
        else:
            adpPos = 'K'
        df_final = df_final.append(plyrStatsPull(adpPlyr, adpTeam, adpPos, 2017))
    except:
        adpTeam = row['team']
        print 'No relevant information for %s of %s, playing %s.' % (adpPlyr, adpTeam, adpPos)
        pass


scorePts = pd.DataFrame(ptsLst, index=None)

totScore = np.dot(df_final, scorePts)
df_final['totScore'] = totScore
print df_final['totScore']
