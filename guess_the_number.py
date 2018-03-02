# Step 1
number = 6
print ('I am thinking of a number between 0 and 10.')
while (number >= 0):
    # print ('You have', count, 'coins.')
    guess = int(input('What is the number?'))
    if guess == number:
        print("Yes! You win")
        break
    elif guess > number:
        print(guess, 'is too high.')
    elif guess < number:
        print(guess, 'is too low.')
        
 
       