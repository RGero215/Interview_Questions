def reverse_str(string):
     current = len(string) - 1
     new_str = ''
     while current >= 0:
          new_str += string[current]
          current -= 1
     return new_str

print(reverse_str('hello'))