
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
meaning = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}
def read_input():
    input_path = '/home/ownercz/Seafile/Package/advent-of-code-2022/day-2/input'
    input_file_content = open(input_path,'r')
    return(input_file_content.read().splitlines())

def game(other, me, styles):
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

def next_move(oponent_played, strategy, styles):
    if strategy == "lose": return styles[oponent_played]['wins_over']
    elif strategy == "win":
        styles_temp = {}
        styles_temp = styles.copy()
        del styles_temp[styles_temp[oponent_played]['wins_over']]
        del styles_temp[oponent_played]
        for key, value in styles_temp.items():
            return key
    elif strategy == "draw": return oponent_played
    else: return None

moves = read_input()
sum = 0
for move in moves:
    single_move = move.split()
    oponent = single_move[0]
    print("Oponent played:" + get_info(oponent,styles))
    strategy = single_move[1]
    print("Need to: "+ meaning[strategy] )
    my_move = next_move(get_info(oponent,styles), meaning[strategy], styles)
    print("My move:"+ str(my_move))
    game_single = game(get_info(single_move[0],styles),my_move,styles
    game_single_points = count_points_per_game(points_game, styles, game_single)
    sum = sum + game_single_points

print(sum)


