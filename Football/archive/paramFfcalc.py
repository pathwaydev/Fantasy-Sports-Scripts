'''
Parameters for fantasyfootballcalculator.com API
'''
# pylint: disable=C0103

import datetime as dt
import requests

# Initialize params dictionary
ffParamDict = {}

# Base url for site
ffParamDict['base'] = r'https://fantasyfootballcalculator.com/adp_xml.php?'

# Fantasy league format
ffParamDict['frmt'] = [
    'standard',
    'ppr',
    'dynasty',
    'rookie'
]

# Number of teams in league
ffParamDict['tmAmt'] = [
    '8',
    '10',
    '12',
    '14'
]

# Generate list of available years
yrMax = int(dt.datetime.now().year)
yrMin = 2007
yrDiff = yrMax - yrMin
ffParamDict['yr'] = [(yrMin + x) for x in range(yrDiff+1)]

urls = []

for fmt in ffParamDict['frmt']:
    for tmAmt in ffParamDict['tmAmt']:
        for yr in ffParamDict['yr']:
            x = ffParamDict['base'] + 'format=%s&year=%s&teams=%s' % (fmt, yr, tmAmt)
            urls.append(x)

ffParamDict['urls'] = urls
print(ffParamDict['urls'])
