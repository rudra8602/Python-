#Rock Paper Scissors Game.
import random,sys
loss=0
win=0
tie=0

while True:
    print('Loss %s, Wins %s, Ties %s' % (loss,win,tie))
    move=input('>')
    if move == 'q':
        sys.exit()
    if move == 'r' or move == 'p' or move == 's':
        break
    print('Please type r,p,s,q')

if move == 'r':
    print('Rock v/s')
elif move == 'p':
    print('Paper v/s ')
elif move == 's':
    print('Scissors v/s ')

move_number = random.randint(1, 3)
if move_number == 1:
        computer_move = 'r'
        print('ROCK')
elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

if move == computer_move:
        print('It is a tie!')
        tie = tie + 1
elif move== 'r' and computer_move == 's':
        print('You win!')
        win = win + 1
elif move == 'p' and computer_move == 'r':
        print('You win!')
        win = win + 1
elif move == 's' and computer_move == 'p':
        print('You win!')
        win = win + 1
elif move == 'r' and computer_move == 'p':
        print('You lose!')
        loss = loss + 1
elif move == 'p' and computer_move == 's':
        print('You lose!')
        loss = loss + 1
elif move == 's' and computer_move == 'r':
        print('You lose!')
        loss = loss + 1        



