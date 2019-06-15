# This challenge requires you to reverse an input string. 
''' 
Clarifying question:
    is the input only a single word?
    if not, do I have to handle black space?
    can I used reversed method?

Assumptions:
    input can be a sentences or a single word
    can't use reversed

Thinking out laoud:
  the easiest way to reverse a string in python is 
  treating the string as an array and appending the character in it.

Rationale:
  The colons inside represent str[start:stop:step] where if step is a negative number
  it'll loop through the string backwards 
'''


print('''Enter word in single quotes or double quotes to be reverse. 
Ex. input: "Monday" output: yadnoM''')

def FirstReverse(str): 
    return str[::-1]

print(FirstReverse(input()))