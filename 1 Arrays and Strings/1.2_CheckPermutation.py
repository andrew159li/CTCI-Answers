'''
Given two strings, write a method to decide if one is a permutation of the
other.
'''
'''
Notes:
Permutation of a string is another string that contains the same chars, only the order of the chars can be different
ex) abcd and dabc are permutations

First ask if permutation comparison is case sensitive (YES)
ask if white space is significant (YES)
'''
# Time: O(nlogn), bottlenecked by Timsort's runtime
# Space: O(n), creates arrays the size of each string, 2n simplifies to n




from collections import Counter
def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Time: O(n), O(2n) due to two for loops, which simplifies down
# Space: O(n), but we can assume array will be at most 128 chars due to ASCII, so can be O(1) space
def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True
