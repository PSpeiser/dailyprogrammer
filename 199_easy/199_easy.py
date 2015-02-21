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

inputs = ['000000000',
          '111111111',
          '490067715', ]
for input in inputs:
    input = [int(digit) for digit in input]
    lines = []
    for i in range(3):
        for digit in input:
            print(digits[digit][i], end='')
        print("")
    print("")




