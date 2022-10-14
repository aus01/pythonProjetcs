import random 
def greeting():
    print('Heyyyy.....Welcome to the guessing game!! What is your name?')
    name = input()
    print(f'Okay {name}.....you have to guess a number between 1 and 9,'
        ' and if you guessed it right you win. You have 5 rounds, goodluck.....!')

    print(guess_number(name)) 

def guess_number(name):

    score = 0
    count = 0
    computer_guess = random.randint(0, 9)
    computer_guessed_numbers = []

    user_guess = input(f'Now....{name} guess the number\n')
    while not user_guess.isdecimal():
        print('Invalid number')
        user_guess = input('Enter a valid number\n')
    if user_guess == computer_guess:
        computer_guessed_numbers.append(computer_guess)
        score +=1
    else:
        score = score
        computer_guessed_numbers.append(computer_guess)
        print(f'Oooops....The computer guessed {computer_guess}')
    count += 1

    while count < 5:
        other_guesses = input('Enter another number\n')
        while not other_guesses.isdecimal():
            print('Invalid number')
            other_guesses = input('Enter a valid number\n')
        computer_guess = random.randint(0, 9)
        if other_guesses == computer_guess:
            computer_guessed_numbers.append(computer_guess)
            score +=1
        else:
            score = score
            computer_guessed_numbers.append(computer_guess)
            print(f'Oooops....The computer guessed {computer_guess}')
        count += 1
            
    if score > 2.5:
        return f'Good game, you won......Your score is {score}.'
    else:
        return f'You lost the game......You guessed {score} correct.'

if __name__ == '__main__':
    greeting()
