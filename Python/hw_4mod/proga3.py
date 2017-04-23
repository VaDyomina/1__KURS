import re
import os

kol = 0
files = []
t = (os.getcwd())+"{}"
roots = [root[1:] for root, dirs, files in os.walk('.')]
for root in roots:
    if root != "":
        files.append(os.listdir(path = t.format(root)))
    elif root == "":
        files.append(os.listdir(path = "."))
for i in range (len(files)):
    expansions = {}
    for j in range(len(files[i])):
        if re.search ('[.]',files[i][j]) != None:
            exp = files[i][j].rsplit('.', maxsplit = 1) [1]
            if exp in expansions:
                expansions[exp] += 1
            else:
                expansions[exp] = 1
    for key in expansions:
        if expansions[key] > 1:
            kol += 1
print("В", kol, "папках встречается несколько файлов с одним и тем же расширением")





                
         
    
