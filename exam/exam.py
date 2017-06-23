import os
import csv
import re

#1
def opening():
    path = os.getcwd() + "/news"
    for root, dirs, files in os.walk(path): 
        for f in files:
            if f == ".DS_Store":
                continue
            else:
                path1 = os.path.join(root, f)
                with open(path1, 'r', encoding='cp1251') as j:
                    text = j.read()
                    lines = []
                    lines = text.split("\n")    
                    sents = 0
                    reg = '.</se>'
                    for line in lines:
                        if re.search(reg, line):
                            sents += 1
                    template = "{}\t{}\n"
                    with open('list.txt', 'a', encoding='utf-8') as t:
                        t.write(template.format(f, sents))
                                    

#2
def making_csv():
    with open('table.csv', 'w', encoding='utf-8') as f:
        output = csv.writer(f, delimiter=',')
        header = ['Название файла', 'Автор', 'Тематика текста' ]
        output.writerow(header)
    path = os.getcwd() + "/news"
    for root, dirs, files in os.walk(path): 
        for f in files:
            if f == ".DS_Store":
                continue
            else:
                path1 = os.path.join(root, f)
                with open(path1, 'r', encoding='cp1251') as j:
                    text = j.read()   
                    reg = '<meta content=\"(.*)\" name=\"author\"'
                    reg1 = '<meta content=\"(.*)\" name=\"topic\"'
                    if re.search(reg, text) and re.search(reg1, text):
                           author = re.search(reg, text).group(1)
                           topic = re.search(reg1, text).group(1)
                           topic = topic.replace(",", " ")
                           with open('table.csv', 'a', encoding='utf-8') as o:
                                output = csv.writer(o, delimiter=',')
                                output.writerow([f, author, topic])


#3 (не закончила)
def making_bigramms():
  path = os.getcwd() + "/news"
  for root, dirs, files in os.walk(path): 
        for f in files:
            if f == ".DS_Store":
                continue
            else:
                path1 = os.path.join(root, f)
                with open(path1, 'r', encoding='cp1251') as j:
                    text = j.read()
                    lines = []
                    lines = text.split("\n")    
                    reg = 'gr=\".*,gen.*</ana>(.*)</w>'
                    for i in range(len(lines)): 
                        if re.search(reg, lines[i]) and re.search(reg, lines[i+1]):
                           a = re.search(reg, lines[i]).group(1)
                           b = re.search(reg, lines[i+1]).group(1)
                        
                           template = "{}\t{}\n"
                           with open('bi.txt', 'a', encoding='utf-8') as t:
                                t.write(template.format(a, b))
                    sents = []
                    for line in lines:
                        reg = "\n.*</ana>(.*)</w>"
                        if re.search(reg, line):
                           word = re.search(reg, line).group(1)
                           sents.append(word)
                           with open('bi.txt', 'a', encoding='utf-8') as t:
                               for sent in range(len(sents)):
                                   t.write(template.format(a, b, sent))






def main():
    lines = opening()
    making_csv()
    making_bigramms()


main()
