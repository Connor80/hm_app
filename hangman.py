""" Command Line version of the game """

import random
import sys

hangman = [
"""
 +----+
 |    |
      |
      |
      |
   ___|___\n""",
"""
 +----+
 |    |
 0    |
      |
      |
   ___|___\n""",
"""
 +----+
 |    |
 0    |
 |    |
      |
   ___|___\n""",
"""
 +----+
 |    |
 0    |
/|    |
      |
   ___|___\n""",
"""
 +----+
 |    |
 0    |
/|\   |
      |
   ___|___\n""",
"""
 +----+
 |    |
 0    |
/|\   |
/     |
   ___|___\n""",
"""
 +----+
 |    |
 0    |
/|\   |
/ \   |
   ___|___\n"""
]


def get_word():
    word_list = ["fruit", "train", "vacation", "hypnotist", "teacher",
                 "salad", "kick", "screw", "absurd", "woozy", "class",
                 "steel", "extend", "disastrous", "incredible", "ship",
                 "acoustic", "drum", "explain", "aggressive", "teeth",
                 "stew", "copy", "noiseless", "picayune", "brainy", "foamy",
                 "erratic", "numerous", "tightfisted", "bake", "interest",
                 "accurate", "annoy", "horn", "concentrate", "swift",
                 "straight", "fear", "crack", "breakable", "camera",
                 "abandoned","awful", "dazzling", "admit", "joke", "trace",
                 "shrill", "mother", "coach", "frog", "fearful", "telling",
                 "charge", "press", "crib", "cows", "knife", "simple",
                 "concerned", "wild", "lumber", "rock", "unbiased", "groan",
                 "delirious", "meat", "hydrant", "exist", "listen", "scrawny",
                 "obscene", "crush", "escape", "suck", "pull", "trip",
                 "continue", "nappy", "dull", "pinch",
                 "certain", "petite", "lettuce", "honey", "debonair",
                 "trade", "tame", "stiff", "size", "messy", "road",
                 "harsh", "reign", "match", "pray", "soda", "stir", "edge"
                 ]
    return random.choice(word_list).upper()


def main():
    word = get_word()
    incorrect = 0
    attempts = 0
    print ("H A N G M A N")
    print (hangman[incorrect])
    print ("The word contains " + str(len(word)) + " letters.\n")
    print ("_" * len(word))
    print ("\nYou have " + str((6 - attempts)) + " attempts remaining.")
    guessed_letters = []
    incorrect = 0
    solved = False
    while not solved and attempts < 6:
        print ("\nHere is what you've already guessed:")
        print (" ".join(guessed_letters))
        guess = input ("\nGuess a letter.\n")
        guess = guess.upper()
        if guess in guessed_letters:
            print ("You've already guessed that letter.")
        elif len(guess) == 1 and guess.isalpha():
            guessed_letters.append(guess)
            result = check_guess(word, guessed_letters, guess)
            if result == word:
                print ("Congrats! You guessed the word. It was " + word + ".")
                solved = True
            else:
                if guess not in word:
                    incorrect += 1
                    attempts += 1
                    print (hangman[incorrect])
                    print (result)
                    print ("You have " + str((6 - attempts)) + " attempts remaining.")
                    if attempts == 6:
                        print ("The man was hanged! The word was " + word + ".")
                else:
                    print (hangman[incorrect])
                    print ("You have " + str((6 - attempts)) + " attempts remaining.")
                    print (result)
        elif len(guess) != 1:
            print ("Please guess only one letter at a time.\n")
        elif len(guess) == 1 and guess.isdigit():
            print ("Please only guess letters.  The word contains no numbers.")
        else:
            print ("Invalid Response.\n")
    while solved or attempts == 6:
        play_again = input ("\nDo you want to play again? Type 'Y' or 'N'\n")
        play_again = play_again.upper()
        if play_again == "Y":
            main()
        elif play_again == "N":
            print ("Thanks for playing!")
            sys.exit()
        else:
            print ("Please type 'Y' or 'N'")


def check_guess(word, guessed_letters, guess):
    status = ""
    matches = 0
    for letter in word:
        if letter in guessed_letters:
            status += letter
        else:
            status += "_"
        if letter == guess:
            matches += 1

    if matches == 1:
        print ("The word contains the letter " + str(guess))
    elif matches > 1:
        print ("The word contains " + str(matches) + " letter " + str(guess) + "'s")
    else:
        print ("Sorry, the word does not contain the letter " + str(guess) + ".")

    return status


main()
