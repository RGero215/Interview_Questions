# This challenge requires you to alphabetically sort the 
# characters in a string. We'll sort the characters using
# the built-in array sort function.

print('''
Enter word to get sorted characters.
input: "Monday" 
output: Madnoy
''')
def alphabetSoup(str):
    chars = list(str) # turn string into list of characters
    sortedChars = sorted(chars)
    return ''.join(sortedChars)

print(alphabetSoup(input()))
