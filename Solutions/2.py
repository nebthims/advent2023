def main():
    with open(r"C:\Users\User\Documents\Coding\Advent\Inputs\2.txt","r") as f:
        data = f.read()
    data_list = data.split("\n")

    formatted = {}
    sum = 0
    power = 0
    for i in range(len(data_list)):
        formatted[i+1] = clean_data(data_list[i])
    for key, value in formatted.items():
        b = check_for_plausibility(value)
        if b:
            sum+=key
        power += check_for_minimum(value)
    print("Sum for Part 1:"+str(sum))
    print("Sum of Powers for Part 2: "+str(power))


def clean_data(item):
    _, data = item.split(": ")
    _, num = _.split(" ")
    trials = data.split("; ")
    game = {}
    list = []
    for i in trials:
        res = {}
        info = i.split(", ")
        for j in info:
            n, col = j.split(" ")
            res[col] = n
        list.append(res)
    return list


def check_for_plausibility(game):
    red_max = 12
    green_max = 13
    blue_max = 14
    for i in range(len(game)):
        if "red" in game[i].keys():
            red = int(game[i]["red"])
        else:
            red = 0
        if "blue" in game[i].keys():
            blue = int(game[i]["blue"])
        else:
            blue = 0
        if "green" in game[i].keys():
            green = int(game[i]["green"])
        else:
            green = 0

        if red>red_max or green>green_max or blue>blue_max:
            return False
    return True

def check_for_minimum(game):
    red = 0
    blue = 0
    green = 0
    for i in range(len(game)):
        if "red" in game[i].keys() and int(game[i]["red"])>red:
            red = int(game[i]["red"])
        if "blue" in game[i].keys()and int(game[i]["blue"])>blue:
            blue = int(game[i]["blue"])
        if "green" in game[i].keys()and int(game[i]["green"])>green:
            green = int(game[i]["green"])
    return red * green * blue

main()