#!/usr/bin/env python3

# Warning: Please refrain from using global variables! Your solution will be checked
# by importing your function, not from the raw input/output.

from wordlist import Wordlist

# mapping of digit to possible letters
# e.g., keypad[2] returns all letters mapped to 2
keypad = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

words = Wordlist('EnglishWords.txt')

### DON'T TOUCH the code above

def predict(digits: str) -> set[str]:
    # TO-DO


### DON'T TOUCH the code below

if __name__ == '__main__':
    assert predict('6263') == {'mane', 'name', 'oboe'}
    assert predict('43556') == {'hello'}
    assert predict('96753') == {'world'}
    assert predict('237593') == set()
    print('All sample test cases passed!')
