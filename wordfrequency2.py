
from multiprocessing.sharedctypes import Value
#word = ''
#countvalue = 1
#word_dict = {word:countvalue}
#countvalue = word_dict.values
#next {word_dict[1]}
#with open ('sometext.txt','r') as outfile:
#    for line in outfile:
       # for word in line.split():
            
         #   if word in word_dict:
         #       word_dict[word] = countvalue
         #   else:
         #       word_dict[word] = countvalue
         #       countvalue += 1
#print(word_dict)



word_dict = {}
countvalue = word_dict.values
with open ('sometext.txt','r') as outfile:
    for line in outfile:
        for word in line.split():
            #for value in word_dict.values():
                #value = 1
                #countvalue = value
            if word in word_dict:
                word_dict[word] += 1
            else:
                    #countvalue = 2
                word_dict[word] = 1
                
print(word_dict)
