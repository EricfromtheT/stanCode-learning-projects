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
    TODO:
    """
    position_dict = {}
    letters = ''  # 'fycliomgorilhjhu'
    for i in range(ROW):
        chars = input(f'{str(i + 1)} row of letters: ')
        # Checking format
        chars = chars.replace(' ', '')
        chars = chars.lower()
        letters += chars
        if len(chars) != ROW or not chars.isalpha():
            print('Illegal format')
            break
        # Collect data
        else:
            for j in range(ROW):
                position_dict[(j, i)] = chars[j]  # { (0, 0): 'i', (1, 0): 'o'......}
    start = time.time()
    ####################
    dictionary = read_dictionary(letters)
    for lst in find_real_word(position_dict, dictionary):
        for word in lst:
            if word in dictionary[word[0]]:
                print(word)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_real_word(position_dict, dictionary):
    """
    :param position_dict: dict, { (coordinate tuple): 'char' }
    :return: list[list[str]], a list contains several lists having strings
    """
    whole_possibility = []
    for position in position_dict:
        whole_possibility.append(find_real_word_helper(position_dict[position], position_dict, [position], [], dictionary))
    return whole_possibility

def find_real_word_helper(current_str, position_dict, used_position, words, dictionary):
    """
    :param current_str: the word in process
    :param position_dict: the coordinate to each char
    :param used_position: the coordinates have been connected
    :param words:
    :param dictionary:
    :return:
    """
    if len(current_str) == ROW * ROW:
        pass
    else:
        # x = used_position[-1][0]
        # for x in x-1, x, x+1:
        #     y = used_position[-1][1]
        #     for y in y-1, y, y+1:
        x = used_position[-1][0]
        y = used_position[-1][1]
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if 0 <= x + i < ROW and 0 <= y + j < ROW:
                    if (x + i, y + j) not in used_position:

                        current_str += position_dict[(x + i, y + j)]

                        if len(current_str) >= 4:
                            words.append(current_str)
                        used_position.append((x + i, y + j))
                        if has_prefix(current_str, dictionary):
                            find_real_word_helper(current_str, position_dict, used_position, words, dictionary)

                        current_str = current_str[:len(current_str)-1]
                        used_position.pop()
    return words

def read_dictionary(letters):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    d = {}
    with open(FILE) as f:
        for line in f:
            word = line.strip()
            if word[0] in letters:
                if word[0] in d:
                    d[word[0]].append(word)
                else:
                    d[word[0]] = [word]

    return d

def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dictionary[sub_s[0]]:
        if word.startswith(sub_s):
            return True
    return False



if __name__ == '__main__':
    main()
