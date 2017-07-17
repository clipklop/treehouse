# ### Letter Game
# # A game based on Hang Man
# # The game picks a random word from a list and lets us guess letters
# # until we either get all of the letters in the word or we run out of chances.
# ###


# import os
# import sys
# import random

# # make a list of words
# words = [
#     'apple',
#     'banana',
#     'orange',
#     'coconut',
#     'strawberry',
#     'lime',
#     'grapefruit',
#     'lemon',
#     'kumquat',
#     'blueberry',
#     'melon',
#     'feijoa'
# ]

# def welcome():
#     start = input("Press enter/return to start, or enter Q to quit ")
#     if start.lower() == 'q':
#         print("Bye!")
#         sys.exit()
#     else:
#         return True

# def clear():
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')

# def draw(bad_guesses, good_guesses, secret_word):
#     clear()

#     print('Strikes: {}/7'.format(len(bad_guesses)))
#     print('')

#     for letter in bad_guesses:
#         print(letter, end=' ')
#     print("\n\n")

#     # draw guessed letters, spaces and strikes
#     for letter in secret_word:
#         if letter in good_guesses:
#             print(letter, end='')
#         else:
#             print("_", end='')

#     print('')

# def get_guess(bad_guesses, good_guesses):
#     while True:
#         # take guess
#         guess = input("Guess a letter: ").lower()

#         if len(guess) != 1:
#             print("You can only guess a single letter!")
#             continue
#         elif guess in bad_guesses or guess in good_guesses:
#             print("You've already guess that letter!")
#             continue
#         elif not guess.isalpha():
#             print("You can only guess letters!")
#             continue
#         else:
#             return guess

# def play(done):
#     clear()
#     secret_word = random.choice(words)
#     bad_guesses = []
#     good_guesses = []

#     while True:
#         draw(bad_guesses, good_guesses, secret_word)
#         guess = get_guess(bad_guesses, good_guesses)

#         if guess in secret_word:
#             good_guesses.append(guess)
#             found = True
#             for letter in secret_word:
#                 if letter not in good_guesses:
#                     found = False
#             if found:
#                 print("You win!")
#                 print("The secret word was {}".format(secret_word))
#                 done = True
#             else:
#                 bad_guesses.append(guess)
#                 if len(bad_guesses) == 7:
#                     draw(bad_guesses, good_guesses, secret_word)
#                     print("You lost!")
#                     print("The secret word was {}".format(secret_word))
#                     done = True

#             if done:
#                 play_again = input("Play again? Y/n ").lower()
#                 if play_again != 'n':
#                     print("Bye!")
#                     return play(done=False)
#                 else:
#                     sys.exit()

# print("Welcome to Letter Guess Game!")

# done = False

# while True:
#     clear()
#     welcome()
#     play(done)

# # while True:
# #     start = input("Press enter/return to start, or enter Q to quit ")
# #     if start.lower() == 'q':
# #         break

# #     # pick a random word
# #     secret_word = random.choice(words)
# #     bad_guesses = []
# #     good_guesses = []

# #     while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):


# #         if guess in secret_word:
# #             good_guesses.append(guess)
# #             if len(good_guesses) == len(list(secret_word)):
# #                 print("You win! The word was {}".format(secret_word))
# #                 break
# #         else:
# #             bad_guesses.append(guess)

# #     else:
# #         print("You didn't guess it! My secret word was {}".format(secret_word))


# def disemvowel(word):
#     vowels = "aeiou"
#     for vowel in word:
#         if vowel in vowels:
#             word = list(word)
#             word.remove(vowel)
#             word = "".join(word)

#     return word

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
#messy_list.insert(0, messy_list.pop(3))
alist = []
for messy in messy_list:
    if isinstance(messy, int):
        if not isinstance(messy, bool):


            alist.append(messy)

print(alist)