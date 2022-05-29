import nltk
from nltk.corpus import wordnet
from nltk.corpus import names

# nltk.download() #using the interactive downloader
# nltk.download('wordnet') #downloading the specific package without interactive downloader
# nltk.download('names')

import random


# 1

def generate_names(char, num):
    global final_lst
    lst = []
    x = names.words('female.txt')
    y = names.words('male.txt')
    u = names.words('female.txt') + names.words('male.txt')
    z = [(i, "female") for i in x]
    h = [(i, "male") for i in y]
    # über x iterieren
    # für jedes element firstchar = "x" checken
    for i in u:
        if i[0] == char and i in x:
            lst.append((i, "female"))
        if i[0] == char and i in y:
            lst.append((i, "male"))
        else:
            continue

    random.shuffle(lst)
    print(lst[0:num])
    if len(lst) == 0:
        print("Sadly, there are no names starting with", char, ". Try again.")

# 2
    with open("female_names", 'w') as writer:
        with open("male_names", 'w') as männlich:
            res = list(map(''.join, lst[0:num]))
            print(res)
            for i in res:
                print(i)
                fml_lst = []
                if "female" in i:
                    writer.write(i[:-6] + "\n")
                    fml_lst.append(i)
                if "male" in i and i not in fml_lst:
                    männlich.write(i[:-4] + "\n")

    # print out a list of random female and male names, beginning with the given character char
    # The number of names is given by the num parameter
    # The names should be displayed in tuples to indicate if it is tagged as a female or male name


generate_names("E", 6)


# 3

class SynAnt:

    def __init__(self, words):
        self.word_dicts = []

        for word in words:
            synonyms = []
            antonyms = []
            syns = wordnet.synsets(word)
            for syn in syns:
                for l in syn.lemmas():
                    synonyms.append(l.name())
                    if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())


            if len(synonyms) == 0:
                synonyms.append("there are no synonyms")
            if len(antonyms) == 0:
                antonyms.append("there are no antonyms")

            self.word_dicts.append({'word': word, 'synonyms': set(synonyms), 'antonyms': set(antonyms)})

    def find_synonyms(self):
        print("These are the Synonyms:")
        for word_dict in self.word_dicts:
            print("Word: {} | Synonyms: {}".format(word_dict['word'], word_dict['synonyms']))

    def find_antonyms(self):
        print("These are the Synonyms:")
        for word_dict in self.word_dicts:
            print("Word: {} | Antonyms: {}".format(word_dict['word'], word_dict['antonyms']))


my_word = ['love']
syns_and_ants = SynAnt(my_word)
syns_and_ants.find_synonyms()
syns_and_ants.find_antonyms()