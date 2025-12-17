#Guess the number Game.
#It uses random module for generating a random number.
#It also tells how many tries you took to guess the number.
import random
print('You have to guess the number between 1 to 50.')
random_num=random.randint(1,50)
tries=0
while True:
    tries = tries + 1
    guess=int(input('>'))
    if guess == random_num:
        print('You guessed the number in '+ str(tries) + ' tries.')
        break
    elif guess > random_num:
        print('Too high')
    else:
        print('Too low')
