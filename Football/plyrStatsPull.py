import nfldb
import pandas as pd

def plyrStatsPull(minAdpPlayer, team, pos, year):
    attrib = {}
    score = {}

    db = nfldb.connect()

    player, _ = nfldb.player_search(db, minAdpPlayer, team=team, position=pos)

    q = nfldb.Query(db)
    q.player(player_id=player.player_id)
    q.game(season_year=year, season_type='Regular')
    for pp in q.as_aggregate():
        score['passYds'] = pp.passing_yds
        score['passTd'] = pp.passing_tds
        score['passInt'] = pp.passing_int
        score['pass2pt'] = pp.passing_twoptm
        score['rushYds'] = pp.rushing_yds
        score['rushTd'] = pp.rushing_tds
        score['rush2pt'] = pp.rushing_twoptm
        score['recYds'] = pp.receiving_yds
        score['recTd'] = pp.receiving_tds
        score['rec2pt'] = pp.receiving_twoptm
        score['recRec'] = pp.receiving_rec
        score['kRetTd'] = pp.kickret_tds
        score['pRetTd'] = pp.puntret_tds
        score['fumRecTd'] = pp.fumbles_rec_tds
        score['fumLost'] = pp.fumbles_lost
        attrib['pos'] = pos
        attrib['team'] = team
        attrib['playerName'] = minAdpPlayer
        plyrIdx = minAdpPlayer, pos, team
        
    df1 = pd.DataFrame(score, index=[plyrIdx])
    df1 = df1[[
        'passTd', 'passYds', 'passInt', 'pass2pt',
        'rushTd', 'rushYds', 'rush2pt',
        'recTd', 'recYds', 'rec2pt', 'recRec',
        'kRetTd', 'pRetTd', 'fumRecTd', 'fumLost'
        ]]
    return df1
