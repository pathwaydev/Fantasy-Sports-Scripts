import pandas as pd


yrLst = list(range(2014,2017))
frmtLst = ['Std', 'Ppr']

'''
yrLst = [2016]
frmtLst = ['Ppr']
'''

for yr in yrLst:
    lkupFile = r'data/plyrLkup%d.csv' % yr
    plyrDf = pd.read_csv(lkupFile)

    for frmt in frmtLst:
        adpFile = r'data/adpByPlyrId%s%d.csv' % (frmt, yr)
        adpDf = pd.read_csv(adpFile)
        
        combDf = pd.merge(
            left=adpDf, right=plyrDf,
            how='inner', on='plyrId'
        )

        allowedPos = ['QB', 'RB', 'WR', 'TE']
        combDf = combDf[combDf['pos'].isin(allowedPos)]
        combDf['adpRank'] = combDf['avgPick'].rank(ascending=1, method='first')

        filename = r'data/adpRank%s%d.csv' % (frmt, yr)
        combDf.to_csv(filename, index=False)
