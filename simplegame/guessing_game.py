from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number : 0, 1 or 2 ")
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print(f"CONGRATS ! YOU WON ! O was at the {guess}")
    else:
        print("GAME OVER! ")
        print(mylist)


# Initial List
mylist = [' ', 'O', ' ']

# Shuffled List
shuffled_list = shuffle_list(mylist)
# User Guess moruk
guess = player_guess()
# Check guess
check_guess(shuffled_list, guess)
