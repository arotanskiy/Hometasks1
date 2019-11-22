import random

def get_length_word():
    while True:
        try:
            word_size = input('Input a length of word used for a game in ragnge 3 - 10: ')
            if int(word_size) < 3 or int(word_size) > 10:  # check a length and type of word
                print("Pleas input a number in a range from 3 to 10")
                continue
            if int(word_size):  # Exit from a loop
                return int(word_size)
                break
        except ValueError:
            print("This is not a digit! Try again")


def get_all_words(word_size):
    """
    To create a list of possible words with length N letters
    :return: list of the possible words
    """
    # list of english words was obtained from: https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    words_list = []
    with open('words_list.txt', 'r') as f:
        for line in f:
            if line.rstrip('\n').isalpha() and len(line) == word_size + 1:
                words_list.append(line.rstrip('\n').lower())
    return words_list



def get_hidden_word(words_list):
    """
        To chose one candidate word from an available list
        :return: hidden word
        """
    hidden_word = random.choice(words_list)
    return hidden_word


def input_word(word_size):
    """
    To get a word from user and
    :return:
    """
    while True:
        word = input('Input your word with a length {}: '.format(word_size))
        if len(word) == word_size and word.isalpha():  # check a length and type of word

            break
            continue
        else:
            print("Pleas input a correct word")
    return word


def check_word(try_word, hidden_word):
    """
    To compare the suggested word and hidden and return a result
    :return: Amounts of cows and bulls
    """
    bulls, cows = 0, 0
    for i, letter in enumerate(try_word):
        if letter in hidden_word:
            if try_word[i] == hidden_word[i]:
                bulls += 1
            else:
                cows += 1
    print('You have: {} bulls and {} cows'.format(bulls, cows))
    return bulls, cows

word_size = get_length_word()
hidden_word = get_hidden_word(get_all_words(word_size))
print('And now you must disclose a hidden word', word_size*'*')
print('Hidden word is: ', hidden_word)
word_attempts = []
while True:
    word_attempts.append(input_word(word_size))
    bulls, cows = check_word(word_attempts[-1], hidden_word)
    if bulls == word_size:
        print('\nYou won!!! Bye')
        exit(0)


