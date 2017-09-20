fname = input('What is the player\'s first name?').lower()
lname = input('What is the player\'s last name?').lower()
year = input('What year are you trying to gather stats for? (Leave blank if current year stats are desired.').lower()

fname = fname[0:2]
lname = lname[0:5]
num = '01'

player_id = lname + fname + num
br_src = 'http://www.baseball-reference.com/players/gl.cgi?id=' + player_id + '&t=b&year=' + year

br_dict = {'player_id': player_id, 'year': year, 'br_src': br_src}