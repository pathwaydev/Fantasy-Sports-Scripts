'''
Dictionaries of fantasy football settings.
'''
# pylint: disable=C0103

scoreEspnStd = [
    # Passing
    ['passTd', 4],
    ['passYds', (25**-1)],
    ['pass2pt', 2],
    ['passInt', -2],
    # Rushing
    ['rushTd', 6],
    ['rushYds', (10**-1)],
    ['rush2pt', 2],
    # Receiving
    ['recTd', 6],
    ['recYds', (10**-1)],
    ['rec2pt', 2],
    ['recRec', 0],
    # Misc Off
    ['kReturnTd', 6],
    ['pReturnTd', 6],
    ['fumRecReturnTd', 6],
    ['fumLost', -2],
    # Kicking
    ['fgMade50', 5],
    ['fgMade40', 4],
    ['fgMade', 3],
    ['patMade', 1],
    ['fgMiss', -1],
    # DST
    ['dstTd', 6],
    ['dstInt', 2],
    ['dstFumRec', 2],
    ['dstKPBlock', 2],
    ['dstSafety', 2],
    ['dstSack', 1],
    ['dstAllow0', 5],
    ['dstAllos6', 4],
    ['dstAllow13', 3],
    ['dstAllow17', 1],
    ['dstAllow27', 0],
    ['dstAllow34', -1],
    ['dstAllow45', -3],
    ['dstAllowMore46', -5]
]

scoreEspnHalfPpr = {
    # Passing
    'passTd': 4,
    'passYds': (25**-1),
    'pass2pt': 2,
    'passInt': -2,
    # Rushing
    'rushTd': 6,
    'rushYds': (10**-1),
    'rush2pt': 2,
    # Receiving
    'recTd': 6,
    'recYds': (10**-1),
    'rec2pt': 2,
    'recRec': .5,
    # Misc Off
    'kReturnTd': 6,
    'pReturnTd': 6,
    'fumRecReturnTd': 6,
    'fumLost': -2,
    # Kicking
    'fgMade50': 5,
    'fgMade40': 4,
    'fgMade': 3,
    'patMade': 1,
    'fgMiss': -1,
    # DST
    'dstTd': 6,
    'dstInt': 2,
    'dstFumRec': 2,
    'dstKPBlock': 2,
    'dstSafety': 2,
    'dstSack': 1,
    'dstAllow0': 5,
    'dstAllos6': 4,
    'dstAllow13': 3,
    'dstAllow17': 1,
    'dstAllow27': 0,
    'dstAllow34': -1,
    'dstAllow45': -3,
    'dstAllowMore46': -5
}

scoreEspnPpr = [
    # Passing
    ['passTd', 4],
    ['passYds', (25**-1)],
    ['pass2pt', 2],
    ['passInt', -2],
    # Rushing
    ['rushTd', 6],
    ['rushYds', (10**-1)],
    ['rush2pt', 2],
    # Receiving
    ['recTd', 6],
    ['recYds', (10**-1)],
    ['rec2pt', 2],
    ['recRec', 1],
    # Misc Off
    ['kReturnTd', 6],
    ['pReturnTd', 6],
    ['fumRecReturnTd', 6],
    ['fumLost', -2],
    # Kicking
    ['fgMade50', 5],
    ['fgMade40', 4],
    ['fgMade', 3],
    ['patMade', 1],
    ['fgMiss', -1],
    # DST
    ['dstTd', 6],
    ['dstInt', 2],
    ['dstFumRec', 2],
    ['dstKPBlock', 2],
    ['dstSafety', 2],
    ['dstSack', 1],
    ['dstAllow0', 5],
    ['dstAllos6', 4],
    ['dstAllow13', 3],
    ['dstAllow17', 1],
    ['dstAllow27', 0],
    ['dstAllow34', -1],
    ['dstAllow45', -3],
    ['dstAllowMore46', -5]
]

ptsLst = []
for k, v in scoreEspnPpr[:15]:
    ptsLst.append(v)
