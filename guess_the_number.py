import random
my_random_number = random.randint(1, 10)
times = 5
yes = 'Y'
print ('I am thinking of a number between 0 and 10.')
while (my_random_number >= 0 and times <= 5):
    print ('You have', times, 'guesses.')
    guess = int(input('What is the number?'))
    if guess == my_random_number:
        print("Yes! You win")
        break
    elif guess > my_random_number and times > 1:
        times -= 1
        print(guess, 'is too high.')
    elif guess < my_random_number and times > 1:
        times -= 1
        print(guess, 'is too low.')
    elif times <=1:
        print("You ran out of guesses!")
        again = str(input('Do you want to play again (Y or N)?'))
        if again == yes:
            times = 5
        else :
            print("Bye!")
            break