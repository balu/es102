def winner(p1, p2, p1msg = "Player 1", p2msg = "Player 2"):
    if p1 == "rock" and p2 == "paper":
        return p2msg
    elif p1 == "rock" and p2 == "scissors":
        return p1msg
    elif p1 == "paper" and p2 == "scissors":
        return p2msg
    elif p1 == p2:
        return "Tie"
    else:
        return winner(p2, p1, p2msg, p1msg)


print(winner("paper", "rock"))