n_amt = int(input('Кол-во участников: '))
man_team = int(input('Кол-во человек в команде: '))
team_list = []
n = 1
if n_amt % man_team == 0:
    for _ in range(n_amt // 4):
        team_list.append(list(range(n, n + man_team)))
        n += man_team
    print('Общий список команд:', team_list)

else:
    print(n_amt, 'участников невозможно поделить на команды по', man_team, 'человек!')