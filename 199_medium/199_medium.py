zero = [' _ ',
        '| |',
        '|_|']
one = ['   ',
       '  |',
       '  |']

two = [' _ ',
       ' _|',
       '|_ ']

three = [' _ ',
         ' _|',
         ' _|']

four = ['   ',
        '|_|',
        '  |']

five = [' _ ',
        '|_ ',
        ' _|']

six = [' _ ',
       '|_ ',
       '|_|']

seven = [' _ ',
         '  |',
         '  |']

eight = [' _ ',
         '|_|',
         '|_|']

nine = [' _ ',
        '|_|',
        ' _|']

digits = [zero, one, two, three, four, five, six, seven, eight, nine]

inputs = [""" _  _  _  _  _  _  _  _  _
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
""",
"""
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
""",
"""    _  _  _  _  _  _     _
|_||_|| || ||_   |  |  ||_
  | _||_||_||_|  |  |  | _|
"""]
for input in inputs:
    lines = input.split('\n')
    numberstring = ''
    for i in range(len(lines[0])//3):
        digit = [lines[0][i*3:i*3+3], lines[1][i*3:i*3+3], lines[2][i*3:i*3+3]]
        for j in range(len(digits)):
            if digits[j] == digit:
                numberstring += str(j)
                break
    print(numberstring)