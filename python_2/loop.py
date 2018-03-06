# 1 to 10
a = range (1,11)
print('Answer to 1 to 10:')
for i in a:
    print(i)

# n to m
print('n to m starts here.')
i1 = input('Start from:')
i2 = input ('End on:')
b = list(filter(lambda x: x < int(i2)+1 and x >int(i1)-1, a))
#for i in a:
    #if i >= int(i1) and int i <= int(i2):
print('Answer to n to m:',b)

# odd
b = list(filter(lambda x: x%2 != 0, a))
print('Answer to odd:',b)

# Print a square
n = int(input('Anwer to square: give me a number for the size of the square'))
print('*' * n)
for i in range(n-2):
    print ('*' + ' ' * (n-2) + '*')
print('*' * n)
