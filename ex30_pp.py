from random import shuffle

def picture(chances):
    if chances == 5:
        print(" ____ \n"
              "|    0\n"
              "|\n"
              "|\n"
              "|__\n"
              "{} chances left".format(chances))
        return True
    elif chances == 4:
        print(" ____ \n"
              "|    0\n"
              "|    |\n"
              "|\n"
              "|__\n"
              "{} chances left".format(chances))
        return True
    elif chances == 3:
        print(" ____ \n"
              "|  \ 0\n"
              "|    |\n"
              "|\n"
              "|__\n"
              "{} chances left".format(chances))
        return True
    elif chances == 2:
        print(" ____ \n"
              "|  \ 0 /\n"
              "|    |\n"
              "|\n"
              "|__\n"
              "{} chances left".format(chances))
        return True
    elif chances == 1:
        print(" ____ \n"
              "|  \ 0 /\n"
              "|    |\n"
              "|   /\n"
              "|__\n"
              "{} chance left".format(chances))
        return True
    else:
        print(" ____ \n"
              "|  \ 0 /\n"
              "|    |\n"
              "|   / \ \n"
              "|__\n"
              "YOU ARE DEAD")
        return False
dictionary = ''
with open('sowpods.txt', 'r') as file:
    dictionary = file.read().split()
shuffle(dictionary)
word = dictionary[0]
guessed = '_'*len(word)

lstguessed = []
chances = 6
print("Here's your word to guess \n" + ("_ " * len(word)) + "\nYou have {} chances. Good luck!".format(chances))
guessed = list(guessed)
word = list(word)

while True:
    letter = input("Choose a letter ").upper()
    if letter in lstguessed:
        print('Already guessed pick another one')
    elif letter in word:
        while letter in word:
            lstguessed.append(letter)
            index = word.index(letter)
            guessed[index] = letter
            word[index] = '_'
        print(' '.join(guessed))
    else:
        chances -= 1
        game = picture(chances)
        lstguessed.append(letter)
        print(' '.join(guessed))
        if not game:
            break

    if '_' not in guessed:
        print("You won!!")
        break




