def Q1():
    fh = (input("Let's read an existing file. Enter a file name: "))
    with open(fh, 'r') as fh:
        contents = fh.read()
    print(contents)
    fh.close()
# Q1()

def Q2():
    filename = input("Let's create a new file. Enter a file name: ")
    fh = open(filename, 'w')
    contents = (input("Type a paragraph."))
    fh.write(contents)
    fh.close()
    
    fh = open(filename, 'r')
    contents = fh.read()
    fh.close()
    print(contents)
# Q2()

def Q3():
    filename = input("Let's create a new file. Enter a file name: ")
    fh = open(filename, 'w')
    contents = (input("Type a paragraph:"))
    fh.write(contents)
    fh.close()
    
    import collections
    letters = collections.Counter(contents.lower())
    print(letters)
    
    def countWords(contents):
        #contents = contents.lower()
        word_list = contents.split()
        word_dict = {}
        for i in word_list:
            word_dict[i] = 0
        for i in word_list:
            word_dict[i] += 1
            
        order = sorted(word_dict, key = word_dict.get, reverse=True)
        values = [word_dict[key] for key in order]
        for i in range(3):
            print (order[i], ":", values[i])
    print(countWords(contents))

#Q3()

def Q4():
    import json
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plot
    data = {
      "data": [
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4]
      ]
    }
    x_list = []
    y_list = []
    for i in data['data']:
        x_list.append(i[0])
        y_list.append(i[1])

    plot.plot(x_list, y_list)
    plot.savefig('myplot.png')
    plot.show()
    
    with open('data.json', 'w') as fh:
      json.dump(data, fh)
    with open('data.json', 'r') as fh:
      data = json.load(fh)
    print(data)
# Q4()

def bonus():
    def crash():
        fh = open('crash.txt', 'w')
        counter = 0
        while True:
            fh.write('c' * (10 ** counter))
            counter += 10 ** counter
            print('Characters Written:', counter)


    if __name__ == '__main__':
        crash()
    
# bonus()