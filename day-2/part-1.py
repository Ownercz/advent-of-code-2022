
styles = {
    'paper': {
        'me': 'Y',
        'other': 'B',
        'points': 2,
        'wins_over': 'rock'},
    'rock': {
        'me': 'X',
        'other': 'A',
        'points': 1,
        'wins_over': 'scissors'},
    'scissors': {
        'me': 'Z',
        'other': 'C',
        'points': 3,
        'wins_over': 'paper'}
    }
points_game = {
    'draw': 3,
    'win': 6,
    'lost':0
    }

def read_input():
    input_path = 'input'
    input_file_content = open(input_path,'r')
    return(input_file_content.read().splitlines())

def game(other, me):
    if me == other: return { 'state': 'draw', 'my_choice': me}
    elif styles[me]['wins_over'] in other: return { 'state': 'win', 'my_choice': me}
    elif styles[other]['wins_over'] in me: return { 'state': 'lost', 'my_choice': me}
    else: return None

def get_info(played,styles):
    for name, info in styles.items():
        if(info["me"] == played): return name
        if(info["other"] == played): return name

def count_points_per_game(points_game,styles, game_result):
    return points_game[game_result["state"]]+styles[game_result["my_choice"]]["points"]

moves = read_input()
sum = 0
for move in moves:
    single_move = move.split()
    print(game(get_info(single_move[0],styles),get_info(single_move[1],styles)))
    print(count_points_per_game(points_game, styles, game(get_info(single_move[0],styles),get_info(single_move[1],styles))))
    sum = sum + count_points_per_game(points_game, styles, game(get_info(single_move[0],styles),get_info(single_move[1],styles)))

print(sum)


