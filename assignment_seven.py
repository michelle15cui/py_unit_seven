import random
def word_option():                                                              # A function that can return the random word to the other main functions.
    words = ["peach","bench","apple","happy","raise","lover","great","funny"]   # A list of words that we can choose
    return random.choice(words)

def word_display(word, correction):                                             # A function that can fill the correct letters in and replace the other letters in underscore.
    display = " "                                                               # this can make the display store as a empty string.
    for letter in word:
        if letter in correction:                                                # If the letter is in the selected word the letter will stay.
            display += letter
        else:
            display += "_"                                                      # If the letter is not in the right sopt in the wrod it will be replace by an underscore.
    return display                                                              # returning display to put it in the final function later.

def word_bank():                                                                # a fucntion that can if the main part of the code to play the game.
    targeted_word = word_option()                                               # defined a random word a name.
    correct_guesses = set()                                                     # a set that can store the correct guesses(I got inspired by chatgpt by using the set code).
    wrong_placed = set()                                                        # a set that can store the misplaced guesses.
    dne = set()                                                                 # a set that can store the does not exist guesses.
    try_times = 5                                                               # the total number of attempts.
    start_times = 0                                                             # the number of attempts the player made.
    print("Hi! Welcome to the word bank game!")
    print(word_display(targeted_word, correct_guesses))                         # showing the initial state of word.

    while try_times > start_times:                                              # a loop that can always working when the attempts didn't reach to 5.
        print("As a reminder, the first letter of this word is:",targeted_word[0])# Providing a reminder for the player for the first letter.
        attempt = input("Enter your guess word: ")                              # name user's input r their guess
        if len(attempt) != 5:                                                   # a check if the word is not having five letters
            print("This is not a five letters word, please enter a five letters word.")
            continue                                                            # If the user's input is not valid the loop will still work.
        if attempt == targeted_word:                                            # a check if the user put in the right word.
            print("YES! you guessed the correct word!", targeted_word)
            break                                                               # The loop will stop working if the word is right.

        start_times_changed = False                                             # to check if the function updated from the iteration(I got inspired by chat gpt too)

        for i in range(len(attempt)):
            letter = attempt[i]                                                 # give every letter in the word a name.
            if letter == targeted_word[i]:                                      # checking if the letter is right and also in the right position.
                correct_guesses.add(letter)                                     # adding the correct letters to the set of it.
                if not start_times_changed:
                    start_times += 1
                    start_times_changed = True                                  # if the function didn't update during playing the attempting time will plus one.
            elif letter in targeted_word:                                       # checking if the letter is in the word but miplaced.
                wrong_placed.add(letter)                                        # adding the miplaced letters to the set of it.
                if not start_times_changed:
                    start_times += 1
                    start_times_changed = True                                  #if the function didn't update during playing the attempting time will plus one.
            else:
                dne.add(letter)                                                 # When the letter does not exist in the word.
                if not start_times_changed:
                    start_times += 1
                    start_times_changed = True                                  # #if the function didn't update during playing the attempting time will plus one.

        print("Attempts left:", try_times - start_times)
        print("Current progress:", word_display(targeted_word, correct_guesses))
        print("Correct letters")
        print("Wrong placed letters:", ", ".join(wrong_placed))
        print("Incorrect letters:", ", ".join(dne))

    else:
        print("Sorry, you used all of your chances.")                           # When the game ended without the break, the user is out of chances.

if __name__ == "__main__":
    word_bank()                                                                 # calling the main function to start the word bank game.


