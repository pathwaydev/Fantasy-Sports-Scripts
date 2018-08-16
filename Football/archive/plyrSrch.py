import nfldb

db = nfldb.connect()

player, _ = nfldb.player_search(db, 'Kareem Hunt', position='RB')
print player.player_id

q = nfldb.Query(db)
q.player(player_id=player.player_id)
for pp in q.as_aggregate():
    print player.team
    print pp
