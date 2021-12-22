guess = int(input('Guess a number (between 1 and 9): '))
number = 9
chances = 5
while chances < 5:
    print(chances)
    if (guess>3):
        print('Your guess was too low: Guess a number higher than 3')
    elif (guess>5):
        print('Your guess was too low: Guess a number higher than 5')
    elif(guess>7):
        print('Your guess was too low: Guess a number higher than 7')
    else:
        print('Congratulations YOU WON!!!')
        break
if not chances < 5:
    print('YOU LOSE!!! The number is',number)
    