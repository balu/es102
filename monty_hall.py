def select_door(doors):
    from random import choice
    return choice(doors)

def remaining_doors(a, b):
    xs = []
    for x in range(1, 4):
        if x not in [a, b]:
            xs.append(x)
    return xs

wins = 0
for i in range(100):
    all_doors = [1, 2, 3]
    prize = select_door(all_doors)
    pick = select_door(all_doors)
    remaining = remaining_doors(prize, pick)
    host = select_door(remaining)
    if pick == prize:
        wins += 1
print(wins)

wins = 0
for i in range(100):
    all_doors = [1, 2, 3]
    prize = select_door(all_doors)
    pick = select_door(all_doors)
    remaining = remaining_doors(prize, pick)
    host = select_door(remaining)
    pick = select_door(remaining_doors(pick, host))
    if pick == prize:
        wins += 1
print(wins)
