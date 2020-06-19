'''
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? 
'''

'''
Notes:
Ask ASCII vs Unicode
Can implement with bit vectors and bit manipulation to reduce space by factor of 8
'''
# Time: O(n), iterates through entire string
# Space: O(n), due to using set


def isUniqueChars(str):
    s = set()
    for i in str:
        if i not in s:
            s.add(i)
        else:
            return False
    return True

# Time: O(n), because it has to iterate through the entire string. Can be O(1) if string > 128 chars
# Space: O(1), due to fixed array size of 128


def isUniqueChars(str):
    if len(str) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in str:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True
