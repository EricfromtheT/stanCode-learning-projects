"""
File: anagram.py
Name: Eric 孔令傑
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        start = time.time()
        dict_list = read_dictionary()
        anagrams = find_anagrams(s, dict_list)
        print(len(anagrams), 'anagrams: ', anagrams)
        ####################
        ####################
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE) as f:
        dictionary = []
        for line in f:
            dictionary += [line.strip()]
        return dictionary


def find_anagrams(s, dict_list):
    """
    :param s: a word
    :return: return a list with all anagrams with the word
    """
    anagrams = []
    print('Searching....')
    for word in create_all_sets(s, dict_list):
        if word in dict_list:
            print('Found: ', word)
            print('Searching....')
            anagrams.append(word)
    return anagrams


def create_all_sets(s, dict_list):
    """
    :param s:
    :param dict_list:
    :return:
    """
    return create_all_sets_helper(s, [], into_a_list(s), [], dict_list)


def create_all_sets_helper(s, current_list, choosing_list, all_sets, dict_list):
    if len(current_list) == len(s) and "".join(current_list) not in all_sets:
        all_sets.append("".join(current_list))
    else:
        for char in choosing_list:
            if len(current_list) == 2 and not has_prefix("".join(current_list), dict_list):
                pass
            else:
                if char in current_list:
                    if count_amount(char, current_list) < count_amount(char, s):
                        current_list.append(char)
                        create_all_sets_helper(s, current_list, choosing_list, all_sets, dict_list)
                        current_list.pop()
                    else:
                        pass
                else:
                    current_list.append(char)
                    create_all_sets_helper(s, current_list, choosing_list, all_sets, dict_list)
                    current_list.pop()
    return all_sets


def into_a_list(s):
    s_list = []
    for char in s:
        s_list.append(char)
    return s_list


def count_amount(checker, sample):
    """
    Count the amount of the character in a word
    :param checker: the thing you want to count inside the
    :param be_checked: the
    :return: amount of the character in the word
    """
    counter = 0
    for thing in sample:
        if thing == checker:
            counter += 1
    return counter


def has_prefix(sub_s, dict_list):
    """
    search if there's some
    :param sub_s:
    :param dict_list:
    :return:
    """
    count = 0
    for word in dict_list:
        if count == 1:
            return True
        if word.startswith(sub_s):
            count += 1
        else:
            pass


if __name__ == '__main__':
    main()
