players_by_level = [800,600,450,338,253,190,142,107]
first_level_players = players_by_level[0]
last_level_players = players_by_level[-1]
last_to_first_ratio = last_level_players/first_level_players
print(last_to_first_ratio)
players_by_level.append(62)
players_by_level.append(34)
players_mid_slice = players_by_level[4:7]
print (players_mid_slice)
players_end_slice = players_by_level[-3: ] 
print (players_end_slice)
