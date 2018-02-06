# guess the word!

import random


words = ['cat', 'book', 'bacon', 'alligator', 'banana']

# how can we incorporate a clue about the word when someone starts the game?
clues = {'cat': 'animal', 'book': 'item', 'apple': 'fruit', 'alligator': 'animal', 'banana': 'fruit'}

def validate_input(input_string):
    """
    Check to make sure that the input from the user is valid.
    """

    # must be one character
    if len(input_string) != 1:
        return False

    # must be letters
    if not input_string.isalpha():
        return False

    return True

def play():

    # TODO randomly select a word from a list of possible words
    word = 'alligator'

    guessed_letters = []
    total_guesses = 5
    wrong_guesses = 0

    # create empty string of length of the word
    base_list = []
    for char in word:
        base_list.append('_')

    print 'guess the word! you have {} guesses'.format(total_guesses)
    print 'your hint: {}'.format(clues[word])

    while wrong_guesses < total_guesses:

        print 'total guesses: {}, wrong guesses: {}'.format(total_guesses, wrong_guesses)
        print 'you have guessed: {}'.format(guessed_letters)
        print ''.join(base_list)

        guess = raw_input('enter a letter: ')

        # let's lowercase their input in case they pass in a capital letter (maybe remove this?)
        guess = guess.lower()

        if not validate_input(guess):
            print 'invalid input for word guess! must be a single letter.'

        elif guess in guessed_letters:
            print 'you already guessed that letter!'

        else:
            guessed_letters.append(guess)

            char_in_word = False
            for index in range(len(word)):
                if word[index] == guess:
                    base_list[index] = guess
                    char_in_word = True
            if not char_in_word:
                wrong_guesses += 1
            if '_' not in base_list:
                print 'YOU WIN WOOT'
                break

    # if we're outside the while loop we have guessed more wrong letters than allowed
    print 'you lose!'

play()