import re


def opening_text(fname):
    sentences = []
    words = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('[\.\?\!…]', 'q', text)
    sentences = new_text.split('q')
    for i in range(len(sentences)):
        sentences[i] = re.sub('[\.,*<>«»:;\'\"\n–-]','', sentences[i])
        sentences[i] = sentences[i].strip()
    return (sentences)


def making_list(sentences):
    true_sentences = [[sentence, (len(sentence) - (len(sentence.split(' ')) - 1)) / (len(sentence.split(' ')))] for sentence in sentences if len(sentence.split(' ')) > 10 ]
    template = "Предложение \"{}\" со словами длинны {:.1f}"
    for i in true_sentences:
        print(template.format(i[0], i[1]))
    

def main():
    sentences = opening_text(input("Введите название файла: "))
    making_list(sentences)


main()
