word_list = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", 
         "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat", 
         "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", 
         "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven", 
         "rhino", "salmon", "seal", "shark", "sheep", "skunk", "sloth", "snake", "spider", 
         "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf", 
         "wombat", "zebra"]
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
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
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 5
for _ in range(word_length):
    display += "_"
game_end = False
while not game_end:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that is not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            game_end = True
            print("You Lose!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        game_end = True
        print("You win!")
    print(stages[lives])
print(f'The word is {chosen_word}! \n Play Again!')