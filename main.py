# объявление переменной
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

user_level = {
    "легкий": words_easy,
    "средний": words_medium,
    "сложный": words_hard,
}

answers = {}
right_answer = 0

# выбор сложности
print("Выберите уровень сложности.")
print("Легкий, средний, сложный.")

answ_user = input()
if answ_user == "легкий":
    print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод. ")
elif answ_user == "средний":
    print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод. ")
elif answ_user == "сложный":
    print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод. ")
else:
    print("Введите корректный уровень сложности. ")

word_dict = user_level[answ_user]

# цикл вопрос-ответ
for key, value in word_dict.items():
    answer = input(f"{key}, {len(value)} букв, начинается на {value[0]}... Ответ: ")
    if answer == value:
        print(f"Верно, {key} — это {value}.")
    else:
        print(f"Неверно. {key} — это {value}.")
    answers[key] = answer == value

# вывод статистики
print()
print("Правильно отвечены слова: ")
for word, bool_v in answers.items():
    if bool_v is True:
        print(word)
        right_answer += 1

print()
print("Неправильно отвечены слова: ")
for word, bool_v in answers.items():
    if bool_v is False:
        print(word)

# подсчет ранга
print("Ваш ранг: ")
print(f"{levels[right_answer]}")
