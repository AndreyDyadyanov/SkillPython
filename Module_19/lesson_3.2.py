players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Traning'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Traning'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'},
}

players_a_team = [
    i_player['name']
    for i_player in players_dict.values()
    if i_player['team'] == 'A' and i_player['status'] == 'Rest'
]

players_b_team = [
    i_player['name']
    for i_player in players_dict.values()
    if i_player['team'] == 'B' and i_player['status'] == 'Traning'
]

players_c_team = [
    i_player['name']
    for i_player in players_dict.values()
    if i_player['team'] == 'C' and i_player['status'] == 'Travel'
]

print(',   '.join(players_a_team))
print(', '.join(players_b_team))
print(', '.join(players_c_team))
