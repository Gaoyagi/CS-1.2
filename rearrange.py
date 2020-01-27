from random import randint

def rearrange(string):
    neo = []
    words = string.split()
    length = len(words)-1
    for x in range(len(words)):
        neo.append(words.pop(randint(0,length)))
        length-=1
    print(' '.join(neo))

rearrange('flying bats and scary cats')