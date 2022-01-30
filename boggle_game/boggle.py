"""
File: boggle.py
Name: Eric 孔令傑
----------------------------------------
Boggle game needs the player to find more words which letters are more or equal to 4 as they can.
This program help finding out all the answers in a boggle game.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
SIDE_LENGTH = 4
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def main():
    """
    Find all the ans in a boggle game!
    """
    print('')
    print(f'Please enter {SIDE_LENGTH} letters in each row, and each letter must be separated with a space! ')
    #  Check the format of user's input and make a list and dict with those letters
    char_dict = {}
    letter_list = []
    for i in range(SIDE_LENGTH):
        row = input(f'{i + 1} row of letters: ')
        if not row.replace(' ', '').isalpha() or len(row.replace(' ', '')) != SIDE_LENGTH or len(
                row) < SIDE_LENGTH * 2 - 1 or len(row) > SIDE_LENGTH * 2:
            print('Illegal input')
            break
        else:
            for j in range(len(row.replace(' ', ''))):
                char = row.replace(' ', '')[j].lower()
                char_dict[i * SIDE_LENGTH + j] = char
                if char not in letter_list:  # Drop out the repeated letters
                    letter_list.append(char)
    start = time.time()
    dictionary = read_dictionary(letter_list)
    all_words = find_the_words(char_dict, dictionary)
    for word in all_words:
        print(f'Found "{word}"')
    print(f'There are {len(all_words)} words in total.')
    ####################
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_the_words(char_dict, dictionary):
    word_list = []
    for key in char_dict:
        word_list += find_the_word_helper(char_dict, key, [key], dictionary, [])
    return word_list


def find_the_word_helper(char_dict, key, current, dictionary, list):
    """
    :param char_dict: (dict) gives every letter a different number to make each letter distinguished.
    :param key: (int) key
    :param current: (list) contains the keys of the words appended into it.
    :param dictionary: (list) the dictionary
    :return list: (list) all the word start with the letter which is also within the dictionary
    """
    s = ''
    for key in current:
        value = char_dict[key]
        s += value
    if len(current) >= SIDE_LENGTH:
        if s in dictionary and s not in list:
            list.append(s)
        if has_prefix(s, dictionary):
            next_list = next_(key)
            for key in next_list:
                if key in current:
                    pass
                else:
                    current.append(key)
                    find_the_word_helper(char_dict, current[-1], current, dictionary, list)
                    current.pop()
    else:
        if has_prefix(s, dictionary):
            next_list = next_(key)
            for key in next_list:
                if key in current:
                    pass
                else:
                    current.append(key)
                    find_the_word_helper(char_dict, current[-1], current, dictionary, list)
                    current.pop()
    return list


def next_(key):
    connect_list = []
    if key == 0:
        connect = [key + 1, key + SIDE_LENGTH, key + SIDE_LENGTH + 1]
        connect_list += connect
    # Lower left
    elif key == SIDE_LENGTH * (SIDE_LENGTH - 1):
        connect = [key + 1, key - SIDE_LENGTH, key - SIDE_LENGTH + 1]
        connect_list += connect
    # Upper right
    elif key == SIDE_LENGTH - 1:
        connect = [key - 1, key + SIDE_LENGTH - 1, key + SIDE_LENGTH]
        connect_list += connect
    # Lower right
    elif key == SIDE_LENGTH * SIDE_LENGTH - 1:
        connect = [key - 1, key - SIDE_LENGTH, key - SIDE_LENGTH - 1]
        connect_list += connect
    else:
        # bottom limit
        if key % SIDE_LENGTH == 0:
            connect = [key - SIDE_LENGTH, key - SIDE_LENGTH + 1, key + 1, key + SIDE_LENGTH, key + SIDE_LENGTH + 1]
            connect_list += connect
        # top limit
        elif key < SIDE_LENGTH:
            connect = [key - 1, key + 1, key + SIDE_LENGTH, key + SIDE_LENGTH - 1, key + SIDE_LENGTH + 1]
            connect_list += connect
        # left limit
        elif key > SIDE_LENGTH * (SIDE_LENGTH - 1):
            connect = [key - SIDE_LENGTH - 1, key - SIDE_LENGTH, key - SIDE_LENGTH + 1, key - 1, key + 1]
            connect_list += connect
        # right limit
        elif key % SIDE_LENGTH == SIDE_LENGTH-1:
            connect = [key - SIDE_LENGTH - 1, key - SIDE_LENGTH, key - 1, key + SIDE_LENGTH, key + SIDE_LENGTH - 1]
            connect_list += connect
        else:
            connect = [key - SIDE_LENGTH - 1, key - SIDE_LENGTH, key-SIDE_LENGTH+1, key-1, key+1, key+SIDE_LENGTH-1, key+SIDE_LENGTH, key+SIDE_LENGTH+1]
            connect_list += connect
    return connect_list


def read_dictionary(letter_list):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list, but get rid of those useless words first.
    """
    with open(FILE) as f:
        dictionary = []
        for line in f:
            inside = True
            for char in ALPHABET:
                if char not in letter_list:
                    if line.find(char) == -1:
                        inside = True
                    else:
                        inside = False
                        break
            if inside is True:
                dictionary.append(line.strip())
        return dictionary


def search_dictionary(word, dictionary):
    if word in dictionary:
        return True
    return False


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    count = 0
    for word in dictionary:
        if count == 1:
            return True
        if word.startswith(sub_s):
            count += 1
        else:
            pass


if __name__ == '__main__':
    main()
