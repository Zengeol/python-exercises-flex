# Hello
def hello(name):
    print('Hello {}'.format(name))
    
hello('abc')

# y=x+1 and xxx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot

def f(x):
    return x+1
xs = list(range(-3, 4))
ys = []
ym = []
for x in xs:
    ys.append(f(x))
plot.plot(xs, ys)
plot.savefig('myplot.png')
plot.close()

#xxx
def g(x):
    return x*x*8
xm = list(range(-100, 100))
y = []
for x in xs:
    y.append(g(x))
plot.plot(xs, y)
plot.savefig('myplotxxx.png')
plot.close()

# Odd or Even
def f(x):
    if x%2 == 0:
        return -1
    else:
        return 1
        
x3 = list(range(-5,5))
y = []
for x in x3:
    y.append(f(x))
plot.bar(x3, y)
plot.savefig('myplotOddEven.png')
plot.close()

# sin
import math
def f(x):
    return math.sin(x)
        
x4 = list(range(-5,5))
y = []
for x in x4:
    y.append(f(x))
plot.plot(x4, y)
plot.savefig('myplotsin.png')
plot.close()

# sin2
from numpy import arange
x4 = arange(-5,6,0.1)
y = []
for x in x4:
    y.append(f(x))
plot.plot(x4, y)
plot.savefig('myplotsin2.png')
plot.close()

# Degree
def f(x):
    a = 9.0/5.0 * x + 32
    return a
#Celsius = int(input("Enter a temperature in Celsius: "))
#Fahrenheit = 9.0/5.0 * Celsius + 32
#print ("Temperature:", Celsius, "C = ", Fahrenheit, "F")
x5 = range(-20,20)
y = []
for x in x5:
    y.append(f(x))

plot.plot(x5, y)
plot.savefig('myplottemp.png')
plot.close()

# Play again?
def play(x):
    if x == 'Y':
        print(x)
        return True
    else:
        return False 
        
x6 = input('Do you want to play again? (Y or N)')
print(play(x6))

# play again? again
def play(x):
    while True:
        if x == 'Y':
            return True
        elif x == 'N':
            return False
        else:
            print ('Invalid input.')
            x = again()
        
def again():
    return input('Do you want to play again (Y or N)?')

x6 = input('Do you want to play again? (Y or N)')
print(play(x6))
