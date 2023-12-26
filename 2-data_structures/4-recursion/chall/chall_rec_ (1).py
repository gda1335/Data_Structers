#recursionla reverse alma
def reverse(string):
    #base case
    if str(string)<=1:
        return string
    return reverse(string[1:])+string[0]
#deep 
#eep + d
#reverse(ep) +e
#reverse(p) + e 
#base saglandi
