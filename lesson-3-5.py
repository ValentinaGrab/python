#Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
import random

def get_jokes(n, repeat):
    if n > 5:
        return 'Вы хотите слишком много шуток'
    else:
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        jokes = []
        joke = ''
        for i in range(n):
            word_1 = random.choice(nouns)
            word_2 = random.choice(adverbs)
            word_3 = random.choice(adjectives)
            joke = f"{word_1} {word_2} {word_3}\n"
            #Если слова не должны повторяться, то удалить их из списков
            if repeat == False:
                nouns.remove(word_1)
                adverbs.remove(word_2)
                adjectives.remove(word_3)
            jokes.append(joke)
        return jokes

print(*get_jokes(4,False))
