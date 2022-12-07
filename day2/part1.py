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

def calculate_score(opponent, player):
    score = 0
    score += pick_points[player]

    opponent = conversion[opponent]
    if player == opponent:
        return score + 3
    if win_dict[player] == opponent:
        return score + 6
    return score
    

def run():
    lines = open('./day2/input/input.txt','r').read().splitlines()
    score = 0
    for line in lines:
        score += calculate_score(*(line.split(" ")))
    print(score)

run()