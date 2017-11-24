# --*-- coding: utf-8 --*--

def left(str, split):
    start = str.find(split)
    print (start, ' start ')
    while start == 0:
        str = str[start+1:]
        print (str, '@@@@')
        start = str.find(split)
    return str

def right(str, split):
    reverse_str = str[::-1]
    print (str)
    start = str[::-1].find(split)
    print (reverse_str)
    while start == 0:
        reverse_str = reverse_str[start+1:]
        start = reverse_str.find(split)
    ret = reverse_str[::-1]
    return ret

a = ' adsadd sdas dsad '
# print (a)
print (left(a, ' '))
print (right(a, ' '))
