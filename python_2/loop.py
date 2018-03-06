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

# Print a square & 2
n = int(input('Anwer to square: give me a number for the size of the square'))
print('*' * n)
for i in range(n-2):
    print ('*' + ' ' * (n-2) + '*')
print('*' * n)

# print a box
n = int(input('Anwer to box: What is the width?'))
m = int(input('Anwer to box: What is the height?'))
print('*' * n)
for i in range(m-2):
    print ('*' + ' ' * (m-2) + '*')
print('*' * n)

# print a triangle
def triangle(n):
     
    # number of spaces
    k = 2*n - 2
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
    # Driver Code
n = int(input('What is the size of the triangle?'))
triangle(n)

# print multiplication_table
n=int(input('Please enter a positive integer between 1 and 15: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, "\t",end = "")      
    print()
    
# Bonus: Print a Banner
n = input('Text?')
m = len(n)+2
print('*' * m)
print ('*' + n + '*')
print('*' * m)

