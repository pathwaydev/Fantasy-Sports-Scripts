'''
sandbox
'''
# pylint: disable=C0103
import nfldb
import pandas as pd
import numpy as np
from plyrStatsPull import plyrStatsPull
from scoreCfg import ptsLst


yrLst = list(range(2014,2017))
frmtLst = ['Std', 'Ppr']

for yr in yrLst:
    for frmt in frmtLst:
        adpFile = r'data/adpRank%s%d.csv' % (frmt, yr)
        df = pd.read_csv(adpFile)
        df_final = pd.DataFrame()

        row_iterator = df.iterrows()
        for i,row in row_iterator:
            name = row['firstNm'] + ' ' + row['lastNm']
            try:
                adpPlyr = name

                if row['tm'] == 'LAC':
                    adpTeam = 'SD'
                elif row['tm'] == 'JAC':
                    adpTeam = 'JAX'
                elif row['tm'] == 'LAR':
                    adpTeam = 'LA'
                else:
                    adpTeam = row['tm']

                if row['pos'] != 'PK':
                    adpPos = row['pos']
                else:
                    adpPos = 'K'

                df_final = df_final.append(plyrStatsPull(row['plyrId'], adpPlyr, adpPos, yr))

            except:
                adpTeam = row['tm']
                print 'No relevant information for %s of %s, playing %s in %d.' % (adpPlyr, adpTeam, adpPos, yr)
                pass

        outfile = r'data/aggAdpScoreRank%s%d.csv' % (frmt, yr)
        scorePts = pd.DataFrame(ptsLst, index=None)
        totScore = np.dot(df_final, scorePts)
        df_final['totScore'] = totScore
        df_final['scoreRank'] = df_final['totScore'].rank(ascending=False, method='min')
        df_final.index.names = ['adpPlyrId']
        df_final.to_csv(outfile)
