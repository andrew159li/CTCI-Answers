'''
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
'''

'''
Notes:
common approach to string manipulation problems is to edit string from end and work backwards
this allows for usage of extra buffer at the end, so we don't need to worry about what we are overwriting

REVIEW
'''

# Time: O(n)
# Space: O(n)
def urlify(string, length):
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == " ":
            string[new_index - 3:new_index] = "%20"
            new_index -= 3
        else:
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

