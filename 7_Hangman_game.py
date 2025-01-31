import random
HANGMANPICS = ['''
  +---+
  |   |
  O   |
 ~|~  |
 ( )  |
      |
=========''', '''
  +---+
  |   |
  O   |
 ~|~  |
 (    |
      |
=========''', '''
  +---+
  |   |
  O   |
 ~|~  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 ~|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
 +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

#  Step 1
fruit =["Banana", "Apple", "Strawberry", "Avocado", "Pineapple", "Watermelon", "Mango", "Kiwi"]

guess_word = random.choice(fruit).lower()
print(guess_word)

# step 2

place_holder = []
for letter in guess_word:
    place_holder += "_"
print(place_holder)
lives = 6

game_over = False
while not game_over:
    # step 3
    guess_letter = input("Guess a Letter : ").lower()
    

    for position in range(len(guess_word)) :
        letter = guess_word[position]
        if letter == guess_letter:
            place_holder[position] = guess_letter
    print(place_holder)
    if guess_letter not in guess_word:
        lives -= 1

        if lives == 0:
            game_over = True
            print("******************* YOU LOSE ******************") 

    if "_" not in place_holder:
        game_over = True
        print("**************** YOU WIN ******************")
    print(HANGMANPICS[lives])
    