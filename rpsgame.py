import random

def winner(you, com):
    if you == com:
        return "draw"
    yours = [('r', 's'), ('s', 'p'), ('p', 'r')]
    if (you, com) in yours:
        return "you"
    else:
        return "com"

print('r, p, s? ', end='')
you = input()
com = random.choice(['r', 'p', 's'])
print(f"Computer chose {com}.")
res = winner(you, com)
if res == "you":
    print("You won.")
elif res == "com":
    print("Computer won.")
else:
    print("Draw.")