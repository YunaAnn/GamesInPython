import random


def number_guessing():
    # computer randomly chooses a number between 1 to 100
    number = random.randint(1, 100)
    correct = False
    # print(number)

    while not correct:
        try:
            guess = int(input('Enter your guess! (1 - 100)'))
            if number == guess:
                print('Hit! Jackpot!')
                correct = True
            elif number > guess:
                print('Your guess is too low!')
            else:
                print('Your guess is too high!')

        except ValueError:
            print('Oops! That was not an integer :C')


if __name__ == '__main__':
    print('Number Guessing Mini-game')
    number_guessing()
