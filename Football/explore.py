import pandas as pd

yrsLst = list(range(2014,2017))
frmtLst = ['Std', 'Ppr']

df = pd.DataFrame()

for yr in yrsLst:
    for frmt in frmtLst:
        f = r'data/masterData%s%d.csv' % (frmt, yr)
        tempDf = pd.read_csv(f)
        print('tempDf size: ', tempDf.size)
        df = df.append(tempDf)

print('findal_size: :', df.size)
df.to_csv('data/masterDataAll.csv', index=False)
