import random

def noun():
    nouns = []
    with open('nouns.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            nouns.append(line)
    nouns.remove(" ")
    n = random.choice(nouns)
    n = n[0:len(n)-1]
    return "la " + n

def noun2():
    nouns2 = []
    with open('nouns.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            nouns2.append(line)
    nouns2.remove(" ")
    n = random.choice(nouns2)
    n = n[0:len(n)-1]
    return "la " + n

def preposition():
    prepositions = []
    with open('prepositions.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            prepositions.append(line)
    prepositions.remove(" ")
    p = random.choice(prepositions)
    p = p[0:len(p)-1]
    return p

def verb():
    verbs = []
    with open('verbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            verbs.append(line)
    verbs.remove(" ")
    v = random.choice(verbs)
    v = v[0:len(v)-1]
    return v

def imperative_verb():
    imp_verbs = []
    with open('imp_verbs.txt','r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for line in lines:
            imp_verbs.append(line)
    imp_verbs.remove(" ")
    iv = random.choice(imp_verbs)
    iv = iv[0:len(iv)-1]
    return iv


def declarative_sentence():
    return (noun() + ' ' + verb() + " " + preposition() + " " + noun2()+ '.')


def interrogative_sentence():
    return (noun() + ' ' + verb() + " " + preposition() + " " + noun2() +'?')


def negative_sentence():
    return (noun() + ' ne ' + verb() + ' pas ' + preposition() + " " + noun2() + '.')


def conditional_sentence():
    return ('Si ' + noun() + ' ' + verb() + ' ' + preposition() + " " + noun2() + ', ' + noun() + " " + verb() +  '.')    


def imperative_sentences():
    return (imperative_verb() + '!')



elem = 0
a = []
for i in range(1,6):
    a.append(i)
random.shuffle(a)
for j in range(5):
    i = a[elem]   
    if i == 1:
        print(declarative_sentence().capitalize())
    elif i == 2:
        print(interrogative_sentence().capitalize())
    elif i == 3:
        print(negative_sentence().capitalize())
    elif i == 4:
        print(conditional_sentence().capitalize())
    else:
        print(imperative_sentences().capitalize())
    a.pop(elem)
