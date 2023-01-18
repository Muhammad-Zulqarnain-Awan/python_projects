#Importing modules
import random
import hangman_art
import hangman_words

#Variables initializations
words = hangman_words.word_list
chosen_word = random.choice(words)
end_of_game = False
lives = 6

#Create a list of "_" equal to chosen word.
display = []
for _ in range(len(chosen_word)):
    display += "_"

#Display the hangman logo at start of game.
print(hangman_art.logo)


#Run a while loop until any of condition met.
while not end_of_game:
    
    #Prompt to user for guessing a word!
    guess = input("Guess a letter: ").lower()
    
    #Check if the guess word already been guessed or not.
    if guess in display:
        print(f"'{guess}' is already guessed!")
    
    #Replace the guess letter in display with "_", if correct.
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    print(" ".join(display))

    #Check if guess word in the chosen word. If yes then, decrease the live by 1.
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in word.\nYou lose a live!")
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The correct word is {chosen_word}.")
    
    #Check if the display has any "_" left or not.
    if "_" not in display:
        end_of_game = True
        print("Congratulations, You Win!")
    
    #Display the hangman figure!
    print(hangman_art.stages[lives])

print("###########################################################################################")