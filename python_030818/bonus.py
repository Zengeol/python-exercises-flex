def bonus():
    phrase = str(input("Enter some words: ")).lower()
    word_list = phrase.split()
    word_dict = {}
    for i in word_list:
        word_dict[i] = 0
    for i in word_list:
        word_dict[i] += 1
        
    order = sorted(word_dict, key = word_dict.get, reverse=True)
    values = [word_dict[key] for key in order]
    for i in range(3):
        print (order[i], ":", values[i])
bonus()