def gen_br_src():
    #URL specification
    url = 'http://www.baseball-reference.com/players/gl.cgi?id=andruel01&t=b&year=2015'
    keyword = 'id='

    fname = input('What is the player\'s first name?').lower()[0:2]
    lname = input('What is the player\'s last name?').lower()[0:5]
    year = input('What year are you trying to gather stats for?').lower()

    #fname = fname[0:2]
    #lname = lname[0:5]
    num = '01'

    player_id = lname + fname + num
    br_src = 'http://www.baseball-reference.com/players/gl.cgi?id=' + player_id + '&t=b&year=' + year

    print(player_id)
    print(year)
    print(br_src)

gen_br_src()