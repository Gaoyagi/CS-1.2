from dictogram import Dictogram
import random

class MarkovChain:

    def __init__(self, word_list):


        #The Markov chain will be a DICTIONARY OF DICTIONARIES { {} {} {} {} }
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.markov_chain = self.build_markov(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    #1st order markov chain
    def build_markov(self, word_list):
        markov_chain = {}

        #traverse the string
        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            #checks if crruent word is in the chain already
            if current_word in markov_chain.keys():
                #get the histogram(dic) for that word in the chain
                histogram = markov_chain[current_word]
                #finds the next_word in the histogram and adds to its weight (chance of it showing up enxt after current word)
                histogram[next_word] = histogram.get(next_word, 0) + 1
            else: #first entry in the chain and creates a new dictionary with next_word as the first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        #TODO: generate a sentence num_words long using the markov chain
        sentence = random.choice(list(self.markov_chain))
        current = self.markov_chain[sentence]
        for num in range(num_words):
            word = current.sample()
            current = self.markov_chain[word]
            sentence += " " + word
        return sentence
        

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))