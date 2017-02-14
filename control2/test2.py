# coding = utf-8

import re
import csv

def opening(text):
    words = []
    text = text.lower()
    words = text.split("\n")
    return words
#5 баллов

def counting(words):
    count = str(len(words))
    with open('counting.txt', 'w', encoding='utf-8') as f:
        f.write(count)
# 8 баллов
def creating(words):
    forms = {}
    for i in range (len(words)):
        reg = "<w lemma=\"(.*)\" type=\"(.*)\""
        if re.search(reg, words[i]):
            res = re.search(reg, words[i]).group(2)
            if res not in forms:
                forms[res] = 1
            else:
                forms[res] += 1
        else:
            continue
    return forms
                            
def printing(forms):
    with open('forms.txt', 'w', encoding='utf-8') as f:
       for key,freq in forms.items():
         word = str(key) + '\n'
         f.write(word)




#10 баллов

def searching_forms(words):
    another_forms = {}
    for i in range (len(words)):
        reg = "<w lemma=\"(.*)\" type=\"(l.f.*?)\">(.*)<"
        if re.search(reg, words[i]):
            res = re.search(reg, words[i]).group(3)
            another_forms.append(res)
    return another_forms

def adding(another_words):
    with open('forms.txt','w', encoding='utf-8') as f:
        for i in range (len(another_words)):
            word = another_word[i]
            f.write(word)

def reorganizing(words):
    reg = "<w lemma=\"(.*)\" type=\"(.*)\">l(.*)</w>"
    for i in range (len(words)):
        if re.search(reg, words[i]):
            res = re.search(reg, words[i]).group(1)

            with open('corpus.txt', 'a', encoding='utf-8') as f:
                line = res + "\n"
def main():
    with open("F.xml", 'r', encoding='utf-8') as f:
        text = f.read()
    words = opening(text)
    counting(words)
    forms = counting_words(words)
    creating(forms)
    another_forms = searching_forms(words)
    adding(another_forms)
    reorganizing(words)
   
main()
    
        

            
                               
