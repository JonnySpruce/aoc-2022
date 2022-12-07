pick_points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

conversion = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

win_dict = {
    "X": "Z",
    "Y": "X",
    "Z": "Y",
}

lose_dict = { v: k for k, v in win_dict.items() }

def calculate_score(opponent, player):
    score = 0
    score += pick_points[player]

    if player == opponent:
        return score + 3
    if win_dict[player] == opponent:
        return score + 6
    return score

def calculate_play(opponent, instruction):
    if instruction == "X": # win
        return win_dict[opponent]
    if instruction == "Z": # lose
        return lose_dict[opponent]
    return opponent

def run():
    lines = open('./day2/input/input.txt','r').read().splitlines()
    score = 0
    for line in lines:
        opponent, instruction = line.split(" ");
        opponent = conversion[opponent]
        player = calculate_play(opponent, instruction)
        score += calculate_score(opponent, player)
    print(score)

run()