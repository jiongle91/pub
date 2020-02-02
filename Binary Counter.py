# -*- coding: utf-8 -*-
"""
Binary Counter learning project using generator function

For a given integer n > 0, count up and print from 1 to n in binary

Example:
    n = 5:
    >> 1
    >> 10
    >> 11
    >> 100
    >> 101
"""


def binary_count(n):
    if type(n) != int or n <= 0:  # catch out of bounds
        print('Please input a positive integer.')
    else:
        for x in print_to_bin(n):
            print(x)


def print_to_bin(n):
    a = '1'  # Binary number for int 1
    for i in range(n):
        yield a
        a = bin_add(a)


def bin_add(b):
    '''
    Function to iterate through a string b representing binary value and
    add one to the binary value. Returns the binary value of b + 1.
    '''
    # If b is already all 1's it can only progress to a binary number
    # of n+1 length.
    if '0' not in b:
        b = '1' + '0' * len(b)
    else:
        arr_b = [digit for digit in b]

        # Starting from the last digit, flip 0s to 1s and vice versa.
        # If digit at -i is 0, just flip to 1 and the function is done.
        # However if digit at -i is 1, flip to 0 and flip the preceding
        # digit -j as well. If -j is a 0 then the function is complete,
        # but if -j is 1 then the loop iterates to digit at -j and does
        # it for -j-1 and so on until a 0 is flipped to a 1.
        for i in range(1, len(arr_b) + 1):
            if arr_b[-i] == '0':
                arr_b[-i] = '1'
                break

            elif arr_b[-i] == '1':
                arr_b[-i] = '0'
                j = i + 1

                if j < len(arr_b):
                    if arr_b[-j] == '0':
                        arr_b[-j] = '1'
                        break
                    else:
                        continue

        b = ''.join(arr_b)  # Convert array representation to str

    return b
