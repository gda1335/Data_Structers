#siklik bulma


"""
input="aabbccdd"
out=2222 seklinde bir cikti vermeli


#str harflere eris
#next indexe bak ayniysa counter say
#birlestir str icinde
#return
"""



def siklikBulma(string):
    
    i = 0
    final_string = ""
    # stringin harflerine eris
    while i < len(string):
        
        c = string[i] # 0 aldi
        
        j = i + 1  #bir sonraki index
    
        compressed = [1,c] #harf siklik
    
        while j < len(string): #2.index
            if string[j] == c: #oncekine esitse
                compressed[0] += 1 #counter
            else: 
                break
            j += 1
        # birlestir bir string icinde   
        # [2,k]  [3,c] 
        final_string += "".join(map(str,compressed))
         #harf adet olarak map etti
        i = j
    
    # return
    return final_string


print(siklikBulma("kkkkkkaaaa"))



#%%


def frequencyDict(string):
 
    # Oncelikle harfleri kucultup, bosluklari siliyoruz.
    string = string.lower().replace(" ", "")
    
    # counter(sayac) dictionary kuruyoruz    
    counter = {} #key : harf , value: freq  counter[i]
 
    # final return icin string kuruyoruz.
    newWord = ""
    
    # harflere ulasip key, value olarak dict e ekliyoruz
    for letter in string: 
        # eger gorulmusse 1 ekliyoruz.
        if letter in counter:
            counter[letter] += 1
        # gorulmemisse 1 olarak kayda geciyor
        else:
            counter[letter] = 1
    
    # dict' teki key, value degerini string e ceviriyoruz.
    for letter in counter:
        newWord += str(counter[letter]) + (letter)
    
    # final stringimizi return yapiyoruz.
    return newWord


print(frequencyDict("aaaagggggg"))



#%%% alternative more understandble

def findFrequency(text):

    control = ""

    newText = ""

    text = text.lower()

    for i in text:

        if control == i:

            continue

        newText += str(text.count(i)) + i

        control = i

    return newText

print(findFrequency("aag"))





#%%



dict1={"izmir":35,"ank":6}



dict1["izmir"]
