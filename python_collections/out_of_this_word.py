"""
    * A game Out of this Word *
    * where you should come up with the words
    * from letters in giving word, eek?!
"""
import random


WORDS = (
    'treehouse',
    'python',
    'learner',
    'avocado'
)


def ask_word(challenge):
    guesses = set()
    print(f'What words can you find in the word - *{challenge}*')
    print()
    print('(Enter Q to quit the game)')

    while True:
        guess = input(f"{len(guesses)+1} words >  ")
        if guess.upper() == 'Q' or len(guesses) == len(challenge):
            print('Ok, bye!')
            break
        guesses.add(guess.lower())
    return guesses


def print_score(number, p1_words, p2_words):
    shared_words = p1_words & p2_words
    print()
    if number == 1:
        p_unique = p1_words - p2_words
        print(f'Player {number} Results:')
        print(f'{len(p1_words)} guesses, {len(p_unique)} unique')
    else:
        p_unique = p2_words - p1_words
        print(f'Player {number} Results:')
        print(f'{len(p2_words)} guesses, {len(p_unique)} unique')

    output_results(p_unique)
    print("-" * 10)
    print()
    print(f"Shared guesses:")
    output_results(shared_words)
    print()
    return p_unique, shared_words


def output_results(results):
    print([print(f'* {x}') for x in results])


def main():
    challenge_word = random.choice(WORDS)

    player1_words = ask_word(challenge_word)
    player2_words = ask_word(challenge_word)
    print_score(1, player1_words, player2_words)


if __name__ == '__main__':
    main()
