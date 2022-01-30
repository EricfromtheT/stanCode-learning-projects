"""
File: largest_digit.py
Name: Eric 孔令傑
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
	:param n: an integer
	:return: the max digit in this integer (negative sign isn't included)
	"""
    if n < 0:  # Make the integer positive
        n = 0 - n
    else:
        if n == 0:
            return n
    digits_num = digits_num_finder(n, 1)
    if digits_num == 1:
        return n
    return find_largest_digit_helper(n, 0, digits_num, 1)


def digits_num_finder(n, counter):
    """
    Used to find the quantity of the digits
	:param n: the integer turned into positive already
	:param counter: each time the counter plus 1 means the quantities of the digit plus 1
	:return: the number counting how many digits the integer has
	"""
    if n < 10 ** counter:
        return counter
    else:
        return digits_num_finder(n, counter + 1)


def find_largest_digit_helper(n, competitor, digits_num, counter):
    """
    Find the largest digit
    :param n: the value going to be found the largest digit inside of it
    :param competitor: the biggest digit in the value will be the competitor
    :param digits_num: the quantities of the digit of the value
    :param counter: count the times, helping the function to recognize when to end
    :return:
    """
    if digits_num < counter:
        return competitor
    else:
        d1 = int(n % 10)
        competitor = max(d1, competitor)
        counter += 1
        return find_largest_digit_helper((n - d1) / 10, competitor, digits_num, counter)


if __name__ == '__main__':
    main()
