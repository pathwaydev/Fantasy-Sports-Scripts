import pandas as pd

yrLst = list(range(2014,2017))
frmtLst = ['Std','Ppr']

df = pd.DataFrame()

for yr in yrLst:
    for frmt in frmtLst:
        f = r'data/masterData%s%d.csv' % (frmt, yr)
        tempDf = pd.read_csv(f)
        print(tempDf.size, 'rows for %s format in year %d' % (frmt, yr))
        df = df.append(tempDf)

print(df.size, 'rows total in final dataframe.')
df.to_csv(r'data/masterDataAll.csv')
