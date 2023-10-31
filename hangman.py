import random

list_of_words = open("hangman_dict.txt", "r", encoding="utf-8")

list_from_file = list()

while True:
    word_in_dict = list_of_words.readline()
    if not word_in_dict:
        break
    list_from_file.append(word_in_dict)

list_from_file = [line.rstrip() for line in list_from_file]

def hangman(word):
    wrong = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if win != True:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))

r = len(list_from_file)

x = random.randint(0, r)

hangman(list_from_file[x])