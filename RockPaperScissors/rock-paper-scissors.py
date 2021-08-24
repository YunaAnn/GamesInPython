import random


def rock_paper_scissors():
    player = input('Start! - - - Choose rock, paper or scissors')
    if player.lower() == 'rock' or player.lower() == 'paper' or player.lower() == 'scissors':
        rock = 'rock'
        paper = 'paper'
        scissors = 'scissors'
        rock_paper_scissors_list = [rock, paper, scissors]
        computer = random.choice(rock_paper_scissors_list)
        print(computer)
        if player == computer:
            print('Draw!', 'P:', player, '-', 'C:', computer)
        elif player == rock and computer == scissors or player == scissors and computer == rock:
            if player == rock:
                win(player, computer)
            else:
                lose(player, computer)
        elif player == paper and computer == rock or player == rock and computer == paper:
            if player == paper:
                win(player, computer)
            else:
                lose(player, computer)
        else:
            if player == scissors:
                win(player, computer)
            else:
                lose(player, computer)
    else:
        print('Wrong choice! Choose: "rock", "paper" or "scissors"')


def win(player, computer):
    return print('Player wins! ', 'P:', player, '-', 'C:', computer)


def lose(player, computer):
    return print('Computer wins! ', 'P:', player, '-', 'C:', computer)


if __name__ == '__main__':
    stop = False
    while not stop:
        print('Rock, Paper, Scissors')
        rock_paper_scissors()
        reply = input('Try again? (Y/N)')
        if reply.lower() == 'y':
            pass
        else:
            stop = True
