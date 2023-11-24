import random

def play():
    user = input("What's your choice ? 'r' for rock, 'p' for paper, 's' for scissors\n-->").casefold().strip()[0]
    computer = random.choice(['r','p','s'])

    if(user == computer):
        return "It's a tie"

    if(is_win(user,computer)):
        return "You Won !"
    
    return "You lost!"

    

def is_win(player,oppnent):
    # return true if player wins
    # r > s, s > p, p > r
    if(player == 'r' and oppnent == 's' or player == 's' and oppnent == 'p' or player == 'p' and oppnent == 'r'):
        return True
    
print(play())