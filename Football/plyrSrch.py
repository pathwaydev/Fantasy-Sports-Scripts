import nfldb

db = nfldb.connect()

player, _ = nfldb.player_search(db, 'Randy Bullock', position='K')
print player

q = nfldb.Query(db)
q.player(player_id=player.player_id)

q.game(season_year=2016, season_type='Regular')
for pp in q.as_aggregate():
    print pp
