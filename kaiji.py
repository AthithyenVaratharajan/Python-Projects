import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors" )
    computer = random.choice(['r','p','s'])
    print(f"You chose {user} and computer chose {computer}:")
    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
