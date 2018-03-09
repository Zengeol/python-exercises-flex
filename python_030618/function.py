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
#def g(x):
    #return x*x*x

xs = list(range(-3, 4))
#xm = list(range(-100,100))
ys = []
ym = []
for x in xs:
    ys.append(f(x))
    #ym.append(g(x))

plot.plot(xs, ys)
plot.savefig('myplot.png')
#plot.plot(xm, ym)
#plot.savefig('myplotSquere.png')
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