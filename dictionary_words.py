import random
def randDictionary(int):
    words = open('/usr/share/dict/words', 'r')
    words_list = words.read().split('\n')
    neo = []
    for _ in range(int):
        neo.append(words_list[random.randint(0, len(words_list)-1)])
    print(' '.join(neo))
    words.close()


randDictionary(6)