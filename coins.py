# 10. How many coins?
# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program.
count = 0
yes = 'yes'
# print ('You have', count, 'coins.')

while (count >= 0):
    print ('You have', count, 'coins.')
    more = str(input('Do you want another?'))
    if more == yes:
        count += 1
    else:
        print('Bye.')
        break