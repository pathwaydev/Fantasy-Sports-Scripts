#import website query library | BeautifulSoup functions to parse data returned from website | pandas to convert list to data frame
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from gen_br_src import br_dict

def br_web_scrape(player_id, year, url):
    #Query website and return html to var page
    page = urlopen(url).read()

    #Parse the html in the 'page' var, and store it in Beautiful Soup format
    soup = BeautifulSoup(page, 'html.parser')

    #Find right table
    target_table = soup.find('table', id='batting_gamelogs')
    target_tbody = target_table.find('tbody')

    #Generate lists for stat columns
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    I = []
    J = []
    K = []
    L = []
    M = []
    N = []
    O = []
    P = []
    Q = []
    R = []
    S = []
    T = []
    U = []
    V = []
    W = []
    X = []
    Y = []
    Z = []
    AA = []
    AB = []
    AC = []
    AD = []
    AE = []
    AF = []
    AG = []
    AH = []
    AI = []
    AJ = []
    AK = []


    #Append player stats to columns
    for row in target_tbody.findAll('tr'):
        cells = row.findAll('td')
        if len(cells) == 37:
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
            F.append(cells[5].find(text=True))
            G.append(cells[6].find(text=True))
            H.append(cells[7].find(text=True))
            I.append(cells[8].find(text=True))
            J.append(cells[9].find(text=True))
            K.append(cells[10].find(text=True))
            L.append(cells[11].find(text=True))
            M.append(cells[12].find(text=True))
            N.append(cells[13].find(text=True))
            O.append(cells[14].find(text=True))
            P.append(cells[15].find(text=True))
            Q.append(cells[16].find(text=True))
            R.append(cells[17].find(text=True))
            S.append(cells[18].find(text=True))
            T.append(cells[19].find(text=True))
            U.append(cells[20].find(text=True))
            V.append(cells[21].find(text=True))
            W.append(cells[22].find(text=True))
            X.append(cells[23].find(text=True))
            Y.append(cells[24].find(text=True))
            Z.append(cells[25].find(text=True))
            AA.append(cells[26].find(text=True))
            AB.append(cells[27].find(text=True))
            AC.append(cells[28].find(text=True))
            AD.append(cells[29].find(text=True))
            AE.append(cells[30].find(text=True))
            AF.append(cells[31].find(text=True))
            AG.append(cells[32].find(text=True))
            AH.append(cells[33].find(text=True))
            AI.append(cells[34].find(text=True))
            AJ.append(cells[35].find(text=True))
            AK.append(cells[36].find(text=True))

    #Generate Pandas dataframe
    df = pd.DataFrame(A, columns = ['GCar'])
    df['GTm'] = B
    df['Date'] = C
    df['Team'] = D
    df['Away Flag'] = E
    df['Opponent'] = F
    df['Result'] = G
    df['Innings'] = H
    df['Plate Appearances'] = I
    df['At Bats'] = J
    df['Hits'] = K
    df['Runs'] = L
    df['2B'] = M
    df['3B'] = N
    df['HR'] = O
    df['RBI'] = P
    df['BB'] = Q
    df['IBB'] = R
    df['SO'] = S
    df['HBP'] = T
    df['SH'] = U
    df['SF'] = V
    df['ROE'] = W
    df['GDP'] = X
    df['SB'] = Y
    df['CS'] = Z
    df['BA'] = AA
    df['OBP'] = AB
    df['SLG'] = AC
    df['OPS'] = AD
    df['BOP'] = AE
    df['aLI'] = AF
    df['WPA'] = AG
    df['RE24'] = AH
    df['DFS(DK)'] = AI
    df['DFS(FD)'] = AJ
    df['POS'] = AK

    #Set filename using br player ID
    if year != '':
        filename = player_id + '_' + year + '_br_stats.csv'
    else:
        current_year = str(date.today().year)
        filename = player_id + '_' + current_year + '_br_stats.csv'

    path = 'data/' + input('What is the data subfolder name that this file belongs to?')

    filename = path + filename

    #Write to CSV file
    df.to_csv(filename, index = False)

    return filename