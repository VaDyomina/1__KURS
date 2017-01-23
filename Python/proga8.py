def words():
    d = {}
    with open ("words.csv", 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.replace('\n', '').split(",")
            d[word[0]] = word[1]
    return d


def playing(d):
    q = len(d)
    for key, val in d.items():
        i = 3
        print("Подсказка: ", key, "...")
        print("У Вас ", i, "попыток(и)")
        print("GO!")
        s = str(input())
        i = 2
        while s != val:
            print("Мимо!")
            if i == 0:
                print("Снова мимо : (")
                print("Загаданное слово:", val)
                print("Словосочетание полностью:", key, val)
                print("----------------------------")
                print("Еще?")
                a = str(input())
                if a == "нет" or a == "Нет":
                    print("Спасибо за игру!")
                    return a
                elif a == "да" or a == "Да":
                    q -= 1
                    break
            if s != val:
                print("Подсказка: ", key, "...")
                print("У Вас осталось", i, "попыток(и)")
                s = str(input())
                i -= 1
        if s == val:
            print("Верно! Красава!")
            q -= 1
            print("В этом разделе осталось еще ", q, "загадок(и)")
            if q == 0:
                print("Я иссяк! Спасибо за энтузиазм!")
                break
            else:
                print("Еще?")                
                d = str(input())
                if d == "нет" or d == "Нет":
                    print("Спасибо за игру!")
                    break

def welcoming():
    print("Добра! Вас беспокоит увлекательнейшая игра \"Отгадай слово по подсказке\"!")
    print("Хотите поиграть?")
    a = str(input())
    if a == "нет" or a == "Нет":
        print("До скорого!")
    elif a == "да" or a == "Да":
        print("Думаю...")
        print("Наслаждайтеь")
        print("__________________________")
        playing(words())
            
welcoming()
