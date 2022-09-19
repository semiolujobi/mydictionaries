codes = {'A':'%','a':'9','B':'@','b':'#','C':'$','c':'!','D':'8','d':'^','E':'7','e':'[','F':'*','f':'-','G':'6','g':'%','H':'+','h': '=','I':'|','i':'>','J':'&','j':']','K':'>','L':'5','l':',','M':'[','m':';','N':':','n':'4','O':'A','o':'`','P':'<','p':'~','Q':'4','q':'.','R':'g','r':'L','S':'?','s':'3','T':'v','t':'e','U':'2','u':'I','V':'_','v':'yr','W':'q','w':'1','Y':'0','y':'p','Z':'l','z':'NA'}
outfile = open('info_security.txt','r') 
words = outfile.read().replace(' ','').replace('.','')
words_list = []
for letter in words:
    words_list.append(letter)
encryption = ""
#print (words_list)
for i in words_list:
    if i in words_list:
        encryption += codes.values()
print(encryption)

