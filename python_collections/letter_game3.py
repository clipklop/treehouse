# A letter game.


import os
import sys
import random


# make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'lemon'
]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def welcome():
    start = input("Press enter/return to start or Q to quit: ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True


def get_guess(guesses):
    while True:
        # take guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in guesses:
            print("You have already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess


def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')
    print('Missed letters:')

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    # draw guessed letters, spaces and strikes
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')

    print('')


def play(done):
    clear()
    # pick a random word
    secret_word = random.choice(words)
    bad_guesses = set()
    good_guesses = set()
    word_set = set(secret_word)

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses | good_guesses)

        if guess in word_set:
            good_guesses.add(guess)
            if not word_set.symmetric_difference(good_guesses):
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                sys.exit()


print("Welcome to Letter Guess!")

done = False

while True:
    clear()
    welcome()
    play(done)