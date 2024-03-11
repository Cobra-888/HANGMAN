import random
import os
import time

#Screen cleaning function
def clear():
  time.sleep(2)
  os.system("clear")

#Error visualization (pictures)
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
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
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt ').split()


#Randomly chooses a word from the word bank
word = random.choice(words)
#print(word)

#length the word
lineWord = "_" * len(word)

wrong = 0    #Number of errors
lives = 6    #Number of lives
use = []     #List of letters used

print("It's a HANGMAN!")

#Game cycle 
#as long as wrong is less than 6 and lineWord is not equal to word, the loop continues
while wrong < 6 and lineWord != word:
  print(HANGMANPICS[wrong])                #image output
  print(f"You have {lives} lives left")    #withdrawal of lives
  print()
  print(f"Used letters: {use}")            #output of used letters
  print()
  print(f"word: {lineWord}")               #lineWord output
  print()
  print("Enter yout guess")                #output of a letter input request
  answer = input(">>> ").strip().lower()
  clear()                                  #clearing the screen

  #If the entered word is in use
  if answer in use:
    lives -= 1                               #Editing the parameters
    wrong += 1                               #Editing the parameters
    print("You already used this letter")    #We inform the player about this
    clear()                                  #Clearing the screen
    continue                                 # We continue the cycle

  #Otherwise, if the entered word is in word
  elif answer in word:
    use.append(answer)                                  #Adding to use
    print(f"You got it! '{answer}' is in the word")     #We inform the player about this
    for i in range(len(word)):                          #Searching for a letter in a word
      if answer == word[i]:                             #If the letter is in the word
        lineWord = lineWord[:i] + answer + lineWord[i+1:]   #Replace the "_" sign with this letter
        clear()                #Clearing the screen
        continue               # We continue the cycle

  #If the letter is not in the word
  else:
    use.append(answer)          #Adding a letter to use
    lives -= 1                  #Editing the parameters
    wrong += 1                  #Editing the parameters
    print("Nope, not in there")    #We inform the player about this
    clear()                     #Clearing the screen
    continue                    # We continue the cycle

#If wrong is equal to 6 (the player lost)
if wrong == 6:
  print(HANGMANPICS[wrong])        #We display the picture
  print(f"Your lives {lives}")     #Output the number of lives
  print()
  print("You lost!")               #We inform the player about this
  print()
  print(f"The word was {word}")    #Output the word
  exit()                #Completing the game

#If lineWord is equal to word (the player won)
elif lineWord == word:
  print(HANGMANPICS[wrong])       #We display the picture
  print(f"Your lives {lives}")    #Output the number of lives
  print()
  print("You won!")               #We inform the player about this
  print()
  print(f"The word was {word}")   #Output the word
  exit()                #Completing the game
    