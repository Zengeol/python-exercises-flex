# 8. Tip Calculator 2
# Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst.
bill = float(input('Total bill amount? '))
level = str(input("Level of service? Choose from good/bad/neutral\n"))
ways = int(input('Split how many ways? '))
tip = float(input('Tip amount? '))
total = bill + tip
per_person = total/ways
print ('Total amount: $', total)
print ('Amount per person: $', per_person)