import random


def dice_rolling():
    # user chooses the number of dices
    # program generates a random number for each dice
    try:
        number_of_dices = int(input('Enter number of dices (1-3)'))
        if number_of_dices == 1:
            return random.sample(range(1, 6), 1)
        elif number_of_dices == 2:
            return random.sample(range(1, 6), 2)
        elif number_of_dices == 3:
            return random.sample(range(1, 6), 3)
        else:
            return 'Wrong number. Choose in range 1-3'
    except ValueError:
        print('Oops! That was not an integer :C')


if __name__ == '__main__':
    stop = False
    while not stop:
        print('Dice Rolling')
        print(dice_rolling())
        reply = input('Try again? (Y/N)')
        if reply.lower() == 'y':
            pass
        else:
            stop = True
            
