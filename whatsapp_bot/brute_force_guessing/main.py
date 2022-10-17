import itertools
import string
import time


def common_word(word):
    with open('words.txt', 'r') as word:
        data = word.read().splitlines()

    for i, match in enumerate(data):
        if match == word:
            return f'The word is: {match} (Attempt #({i}))'

    return 0


def brute_force(word, min_length=4, max_length=10, includes_digit=False, includes_symbols=False):
    char = string.ascii_lowercase

    if includes_digit:
        char += string.digits

    if includes_symbols:
        char += string.punctuation

    attempts = 0

    for word_length in range(min_length, max_length):
        for guess in itertools.product(char, repeat=word_length):
            attempts += 1
            guess = ''.join(guess)

            if guess == word:
                no_attempts = '{:,}'.format(attempts)
                return f'"{word}"was found  in {no_attempts} guesses.'

            # print(guess,attempts)


searchterm = input("Which word:-").lower()
start_time = time.time()
common_search = common_word(searchterm)
print('searching...')
if common_search != 0:
    print(common_search)
else:
    request = brute_force(searchterm, min_length=3,
                          max_length=10, includes_digit=False)
    print(request)

print(round(time.time()-start_time, 2), 's')
