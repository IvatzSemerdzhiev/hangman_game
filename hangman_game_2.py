import random
from replit import clear
import os

def screen_clear():
    clear()
print("Type letter! ")
words_list = ['apple', 'kiwi','network']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
secret_word = random.choice(words_list)
display = []

for i in range(0, len(secret_word)):
    display += '*'
print(display)

counter = 0

chosen_words = ''

while True:
    if counter == 6:
        print("No more lifes! You lose!")
        break
    guess = input()
    
    screen_clear()


    if guess in chosen_words:
        print(f"Already gave {guess}")
        continue

    chosen_words += guess



    for index, char in enumerate(secret_word):
        i = secret_word[index]
        if char == guess:
            display[index] = i

    if guess in secret_word:
        print(f"You have chosen {guess}, it's correct!")

    else:
        counter += 1

        if counter == 1:
            print(f"You have chosen {guess}, that is not a correct letter, you lose a life!")
            print(stages[5])
        elif counter == 2:
            print(f"You have chosen {guess}, that is not a correct letter, you lose a life!")
            print(stages[4])
        elif counter == 3:
            print(f"You have chosen {guess}, that is not a correct letter, you lose a life!")
            print(stages[3])
        elif counter == 4:
            print(f"You have chosen {guess}, that is not a correct letter, you lose a life!")
            print(stages[2])
        elif counter == 5:
            print(f"You have chosen {guess}, that is not a correct letter, you lose a life!")
            print(stages[1])
        elif counter == 6:
            print(f"You have chosen {guess}, that is not a correct letter, you lose a life!")
            print(stages[0])


    if '*' not in display:
        print(display)
        print("You win!")
        break
    print(display)





