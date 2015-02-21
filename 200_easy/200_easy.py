inputs = [('37 22',
           """.....................................
...#######################...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#######.....
...###.................##......#.....
...#..##.............##........#.....
...#....##.........##..........#.....
...#......##.....##............#.....
...#........#####..............#.....
...#........#..................#.....
...#.......##..................#.....
...#.....##....................#.....
...#...##......................#.....
...#############################.....
.....................................
.....................................
.....................................
.....................................""",
           '8 12 @'),
          ('16 15',
           """----------------
-++++++++++++++-
-+------------+-
-++++++++++++-+-
-+------------+-
-+-++++++++++++-
-+------------+-
-++++++++++++-+-
-+------------+-
-+-++++++++++++-
-+------------+-
-++++++++++++++-
-+------------+-
-++++++++++++++-
----------------"""
           , '2 2 @'),
          ('9 9',
           """aaaaaaaaa
aaadefaaa
abcdafgha
abcdafgha
abcdafgha
abcdafgha
aacdafgaa
aaadafaaa
aaaaaaaaa""",
           '8 3 ,')]


def image_string_to_array(image_string):
    lines = image_string.split('\n')
    lines = [list(line) for line in lines]
    return lines


def print_image(image):
    lines = [''.join(line) for line in image]
    print('\n'.join(lines))


def flood_fill(image, x, y, symbol):
    x = int(x)
    y = int(y)
    old_symbol = image[y][x]
    image[y][x] = symbol
    # check neighbours and fill them too
    neighbours = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
    for nx, ny in neighbours:
        if ny >= len(image) or ny < 0:
            continue
        if nx >= len(image[ny]) or nx < 0:
            continue
        if image[ny][nx] == old_symbol:
            image = flood_fill(image, nx, ny, symbol)
    return image


for input in inputs:
    height, width = input[0].split(' ')
    image = image_string_to_array(input[1])
    x, y, symbol = input[2].split(' ')
    new_image = flood_fill(image, x, y, symbol)
    print_image(new_image)
