import unittest

def reverse_character(message, left, rigth):
    while left < rigth:
        message[left], message[rigth] = message[rigth], message[left]
        left += 1
        rigth -= 1


def reverse_message(message):
    reverse_character(message, 0, len(message) - 1)
    current_word_start = 0

    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse_character(message, current_word_start, i - 1)
            current_word_start = i + 1


class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse_character(list_of_chars, 0, len(list_of_chars) - 1)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_char(self):
        list_of_chars = ['A']
        reverse_character(list_of_chars, 0, len(list_of_chars) - 1)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_long_list(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E', 'F']
        reverse_character(list_of_chars, 0, len(list_of_chars) - 1)
        expected = ['F', 'E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)

    def test_reverse_empty_message(self):
        message = list('')
        reverse_message(message)
        reverse_message(message)
        expected = list('')
        self.assertEqual(message, expected)

    def test_reverse_one_word(self):
        message = list('hello')
        reverse_message(message)
        expected = list('hello')
        self.assertEqual(message, expected)

    def test_reverse_long_message(self):
        message = list('Ramon is name my hello')
        reverse_message(message)
        expected = list('hello my name is Ramon')
        self.assertEqual(message, expected)

if __name__ == '__main__':
    unittest.main()
