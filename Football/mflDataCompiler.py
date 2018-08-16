import os
from glob import glob
import pandas as pd

curPth = os.path.dirname(os.path.abspath(__file__))
os.chdir(curPth)

files = glob('data/adp*.csv')


df = pd.DataFrame()
for f in files:
    df = pd.concat([df, pd.read_csv(f)])

df.to_csv('data/masterData.csv', index=False)
