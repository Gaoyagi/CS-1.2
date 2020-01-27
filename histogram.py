def histogram(source_text):
    histogram = []      #list of list of all words
    #open file and put all the lines in a list, then closes it
    words = open(f'{source_text}.txt', 'r')
    words_list = words.readLines()
    words.close()
    #loop through the list of lines
    for line in words_list:
        #splits each line into a list of words
        temp = line.split(' ')
        #loops through the list of words
        for word in temp:
            #if the listogram is empty just add the word
            if len(listogram) == 0:
                histogram.append([word, 1])
            else:
                #checks the listogram if the word is  already in it
                for item in histogram:
                    if item[0] == word:
                        item[1] += 1
    return histogram

def dictogram(source_text):
    histogram = []      #list of list of all words
    #open file and put all the lines in a list, then closes it
    words = open(f'{source_text}.txt', 'r')
    words_list = words.read().split('')
    words.close()
    for line in words_list:
        #splits each line into a list of words
        temp = line.split('\\s')
        #loops through the list of words
        for word in temp:
            if word in histogram:
                histogram[word]+=1
            else:
                histogram[word]=1
    return histogram

def tuptogram(source_text):
    histogram = []      #list of list of all words
    #open file and put all the lines in a list, then closes it
    words = open(f'{source_text}.txt', 'r')
    words_list = words.read().split('')
    words.close()
    for line in words_list:
    #splits each line into a list of words
        temp = line.split('\\s')
        #loops through the list of words
        for word in temp:
            #if the listogram is empty just add the word as a tuple
            if len(listogram) == 0:
                histogram.append((word, 1))
            else:
                #checks the listogram if the word is  already in it
                for item in range(len(histogram)-1):
                    if histogram[item][0] == word:
                        quan = item[1]
                        histogram[item] = (word, quan+1)
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    for item in histo
