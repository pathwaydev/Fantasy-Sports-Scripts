import pandas as pd
from gen_br_src import br_dict
from web_scrape import br_web_scrape

#br_dict = gen_br_src()
player_id = br_dict['player_id']
year = br_dict['year']
url = br_dict['br_src']

filename = br_web_scrape(player_id, year, url)
