import random
def hangman(word):
    wrong = 0
    stages= ["",
             "_________          ",
             "|        |         ",
             "|        0         ",
             "|       /|\        ",
             "|       / \        ",
             "|                  "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to hangman！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a  letter "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose！It was {}.".format(word))

answers = ["cat","dog","tiger","lion","rabbit","bird","mouse",
           "pig","cow","horse","monkey","gorilla","panda","elephant",
           "marina","kangaroo","snake","sheep" ]
n = random.randint(0,17)
hangman(answers[n])
