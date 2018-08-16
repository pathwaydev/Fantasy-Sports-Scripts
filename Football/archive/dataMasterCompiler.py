import pandas as pd

yrLst = list(range(2014,2017))
frmtLst = ['Std','Ppr']

for yr in yrLst:
    for frmt in frmtLst:
        adpFile = r'data/adpRank%s%d.csv' % (frmt, yr)
        scoreFile = r'data/aggAdpScoreRank%s%d.csv' % (frmt, yr)

        adpDf = pd.read_csv(adpFile)
        scoreDf = pd.read_csv(scoreFile)

        crossDf = pd.merge(
            left=adpDf, right=scoreDf,
            how='inner', left_on='plyrId', right_on='adpPlyrId',
            sort=False
        )

        outfile = r'data/masterData%s%d.csv' % (frmt, yr)
        crossDf.to_csv(outfile, index=None)
