#import random
#guess = ''
#while guess not in ('heads', 'tails'):
#    print('Guess the coin toss! Enter heads or tails:')
#    guess = input()
#toss = random.randint(0, 1)  # 0 is tails, 1 is heads
#if toss == guess:
#    print('You got it!')
#else:
#    print('Nope! Guess again!')
#    guess = input()
#    if toss == guess:
#        print('You got it!')
#    else:
#        print('Nope. You are really bad at this game.')

#import random
#guess = ''
#while guess not in ('heads', 'tails'):
#    print('Guess the coin toss! Enter heads or tails:')
#    guess = input()
#toss = random.randint(0, 1)  # 0 is tails, 1 is heads
#if toss == 0 and guess == 'tails':
#    print('You got it!')
#elif toss == 1 and guess == 'heads':
#    print('You got it!')
#else:
#    print('Nope. You are really bad at this game.')

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.choice(['heads', 'tails'])
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


#toss = random.randint(0, 1)  # 0 is tails, 1 is heads
#if toss == guess:  # Issue: Comparing an integer with a string
#    print('You got it!')

#toss = random.choice(['heads', 'tails'])
#if toss == guess:  # Correct: Comparing strings
#    print('You got it!')





