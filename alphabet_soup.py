# This challenge requires you to alphabetically sort the 
# characters in a string. We'll sort the characters using
# the built-in array sort function.

''' 
Clarifying question:
    do I have to create a sorted function or can I use 
    sorted method?

Assumptions:
    input can be a sentences or a single word
    we can use sorted method

Thinking out laoud:
  If we use sorted to arrange the characters in a word
  we just need to turned the string into an array of 
  chars and return it.

Rationale:
  convert the string into a list of characters
  sort the list in alphabetical order
  return the newly joined string 
'''

print('''
Enter word to get sorted characters.
input: "Monday" 
output: Madnoy
''')
def alphabetSoup(str):
    chars = list(str)
    sortedChars = sorted(chars)
    return ''.join(sortedChars)

print(alphabetSoup(input()))
