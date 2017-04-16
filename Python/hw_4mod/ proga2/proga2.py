import os
import re

def reading_and_splitting():   
    fileslist = [file for file in os.listdir() if os.path.isfile(file)]
    names = []
    for file in fileslist:
        name = file.rsplit('.', maxsplit=1)[0]
        names.append(name)
    return names

def printing(names):
    printing_names = []
    files = 0
    punct_names = [name for name in names if re.search('[.,!?:;)(-]', name) != None]
    for i in range(len(punct_names)):
        files += 1
        if punct_names[i] not in printing_names:
            printing_names.append(punct_names[i])
    print("Найдено ", files, " файлов: ")
    for i in range(len(printing_names)):
        print(printing_names[i])

    
def main():
    names = reading_and_splitting()
    printing(names)       


main()