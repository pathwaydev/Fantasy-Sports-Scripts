'''
Python module to request xml adp fantasy football data from
fantasyfootballcalculator.com using site's standard API.
'''
# pylint: disable=C0103
import requests
import re
import os.path
from lxml import etree as et
import pandas as pd
from paramFfcalc import ffParamDict as params

urls = params['urls']
#test urls
'''urls = [
    r'https://fantasyfootballcalculator.com/adp_xml.php?format=dynasty&year=2016&teams=8',
    r'https://fantasyfootballcalculator.com/adp_xml.php?format=dynasty&year=2017&teams=8'
]'''

def ffCalcPull(urls):
    '''
    Function to execute data pull from FantasyFootballCalculator. 
    Accepts: List of ffcalc urls. 
    Actions: Iterates through list, generates dataframe, writes dataframe to csv.
    Retusn: CSV file of data pulled from ffcalc XML of selected url in 'data' directory.
    '''
    for url in urls:
        
        adpDict = {
            'playerId': [],
            'rdAdp': [],
            'ovrlAdp': [],
            'name': [],
            'pos': [],
            'team': [],
            'draftCnt': [],
            'byeWk': [],
            'frmt': [],
            'tmCnt': [],
            'rdCnt': [],
            'year': None
        }

        r = requests.get(url)
        root = et.fromstring(r.content)
        adpInfo = root[0]

        if adpInfo[0].text is not None:
            frmt = re.findall(r'format=([^(]*?)\&', url)[0]
            year = re.findall(r'year=([^(]*?)\&', url)[0]
            outFile = 'data/adp_%s_%stm_%s.csv' % (year, adpInfo[0].text, frmt)
            adpData = root[1]

            for child in adpData:
                adpDict['playerId'].append(child[0].text) #Player ID
                adpDict['rdAdp'].append(child[1].text) #ADP by Round
                adpDict['ovrlAdp'].append(child[2].text) #Overall ADP
                adpDict['name'].append(child[3].text) #Name
                adpDict['pos'].append(child[4].text) #Position
                adpDict['team'].append(child[5].text) #Team
                adpDict['draftCnt'].append(child[6].text) #Times Drafted
                adpDict['byeWk'].append(child[7].text) #Bye Week
                adpDict['frmt'].append(frmt) #League Format
                adpDict['tmCnt'].append(adpInfo[0].text) #Amout of Teams in League
                adpDict['rdCnt'].append('15') #Rounds in Draft
                adpDict['year'] = year #Year of Draft

            if not os.path.isfile(outFile):
                adpDf = pd.DataFrame.from_dict(adpDict)
                adpDf.to_csv(outFile, index=False)
            else:
                print('DUPLICATE. File skipped.')

        else:
            print('No data for parameters specified in ', url)
            print('File write skipped.')
            
ffCalcPull(urls)
