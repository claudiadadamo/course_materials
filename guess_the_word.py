# guess the word game!

import random


# create a map of possible words and a hint
words_and_hints = {'cat': 'animal', 'book': 'item', 'apple': 'fruit', 'alligator': 'animal', 'banana': 'fruit'}

def validate_input(input_string):

    # must be one character
    if len(input_string) != 1:
        return False

    # must be letters
    if not input_string.isalpha():
        return False

    return True


def play():

    # randomly select a word from a list of possible words
    word = random.choice(words_and_hints.keys())

    guessed_letters = []
    wrong_guess_maximum = 5
    wrong_guesses = 0

    # create empty string of length of the word
    base_list = []
    for char in word:
        base_list.append('_')

    print 'guess the word! you have {} guesses'.format(wrong_guess_maximum)
    print 'your hint: {}'.format(words_and_hints[word])
    print '--------'

    while True:

        print 'total guesses: {}, wrong guesses: {}'.format(wrong_guess_maximum, wrong_guesses)
        print 'you have guessed: {}'.format(guessed_letters)
        print ' '.join(base_list)
        print ''

        guess = raw_input('enter a letter: ')

        # let's lowercase their input in case they pass in a capital letter
        guess = guess.lower()

        if not validate_input(guess):
            print 'invalid input for word guess! must be a single letter.'

        elif guess in guessed_letters:
            print 'you already guessed that letter, try again.'

        else:
            guessed_letters.append(guess)

            letter_in_word = False

            # go through all of the letter in the word and check to see if their guess is there
            for index in range(len(word)):
                if word[index] == guess:
                    base_list[index] = guess
                    letter_in_word = True

            if not letter_in_word:
                wrong_guesses += 1

            if '_' not in base_list:
                print 'YOU WIN WOO!'
                break

            if wrong_guesses == wrong_guess_maximum:
                print 'oh no! you lost :('
                break

play()