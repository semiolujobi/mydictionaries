
words = []
wordcount = []
with open('sometext.txt','r') as outfile:
    for line in outfile:
        for word in line.split():
            words.append(word)
        for i in words:
            words.count(i)
            wordcount.append(words.count(i))
#word_dict = {'words': words, 'count': wordcount}   
#print (word_dict)         
word_list = zip(words, wordcount)
word_dict = dict(word_list)
print(word_dict)            




