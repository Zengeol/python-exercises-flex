def countWords(A):
   dic={}
   for x in A:
       if not x in dic:        #Python 2.7: if not dic.has_key(x):
          dic[x] = A.count(x)
   return dic
phrase = str(input("Enter a paragraph of text: ")).lower()
word_list = phrase.split()
print(countWords(word_list))