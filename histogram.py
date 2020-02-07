import random

# #dictionary version
# def histogram(source_text):
#     histogram = {}      #histogram dictionary of all words
#     with open(f'{source_text}.txt', 'r') as text:
#         for line in text:
#             for word in line.split():
#                 if word not in histogram:
#                     histogram[word] = 1
#                 else:
#                     histogram[word]+=1
#     return histogram

#list version
def histogram(source_text):
    histogram = []
    with open(f'{source_text}.txt', 'r') as text:
        for line in text:
            for word in line.split():
                isIn = False
                for item in histogram:
                    if item[0] == word:
                        item[1]+=1
                        isIn = True
                if isIn == False:
                    histogram.append([word, 1])
    return histogram

# #tuple version
# def histogram(source_text):
#     histogram = ()
#     with open(f'{source_text}.txt', 'r') as text:
#         for line in text:
#             for word in line.split():
#                 isIn = False
#                 temp = list(histogram)
#                 for item in temp:
#                     temp2 = list(item)
#                     if temp2[0] == word:
#                         temp2[1]+=1
#                         isIn = True
#                 if isIn == False:
#                     temp.append((word, 1))
#                 histogram = tuple(temp)
#     return histogram


def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    # #dictionary version
    # print(f"{word} shows up {histogram[word]} times")

    #list and tuple version
    for item in histogram:
        if item[0] == word:
            print(f"{item[0]} shows up {item[1]} times")

def percentages(histogram):
    length = 0
    for item in histogram:
        length+=item[1]
    for item in histogram:
        item.append(item[1]/length)
        print(f"{item[0]} ==> {item[2]}")
    return length

def weightedRandom(histogram, length):
    chosen = random.randint(0, length)
    print(chosen)
    indexes = 0
    for words in histogram:
        indexes+=words[1]
        if indexes>chosen:
            return words[0]
    
        



temp = histogram("words")
print(f"there are {unique_words(temp)} unique words")
frequency("george", temp)
print(weightedRandom(temp, percentages(temp)))