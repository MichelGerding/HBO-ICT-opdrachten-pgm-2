def create_one_row(width):
    """Returns one row of zeros of width "width".
       You might use this in your create_board(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def create_board(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    a = []
    for row in range(height):
        a += [create_one_row(width)]        # gebruik de bovenstaande functie zodat ... één rij is!!
    return a

def print_board(a):
    """This function prints the 2D list-of-lists a."""
    for row in a:               # row is de hele rij
        for col in row:         # col is het individuele element
            print(col, end='')  # druk dat element af
        print()

def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                a[row][col] = 1
            else:
                a[row][col] = 0

    return a

def inner_cells(width, height):
    """ Creates a empty board and then modifies it
        so that all interior cells are set
    """
    a = create_board(width, height)

    for i in range(1, height-1):
        for j in range(1, width-1):
            a[i][j] = 1

    return a

import random

def random_cells(width, height):
    """ Creates a empty board and then modifies it 
        so that all interior cells are randomly seet
    """
    a = create_board(width, height)

    for i in range(1, height-1):
        for j in range(1, width-1):
            a[i][j] = random.randint(0,1)

    return a

def copy(a):
    """Returns a DEEP copy of the 2D array a."""
    height = len(a)
    width = len(a[0])
    new_a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            # welke enkele regel moet hier staan om elk element van a
            # naar het corresponderende element van new_a te kopiëren?
            new_a[row][col] = a[row][col]

    return new_a

def inner_reverse(a):
    """ copys a board and set invers all interior cells
    """
    new_a = copy(a)
    for i in range(1, len(a) -1):
        for j in range(1, len(a[0])-1):
            new_a[i][j] = int( not a[i][j])

    return new_a

def count_neighbours(x, y, a):
    indexes = [
        [x-1, y+1], [x, y+1], [x+1, y+1],
        [x-1, y], [x+1, y],
        [x-1, y-1], [x, y-1], [x+1, y-1]
    ]
    count = 0
    for i in indexes:
        if a[i[0]][i[1]] == 1:
            count += 1
    
    return count

a = [[0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0]]


def next_life_generation(a):
    """ generate the next generation of the game based on 
        passed through game board
    """
    height = len(a)
    width = len(a[0])
    neigbours = create_board(height, width)

    for i in range(1, height-1):
        for j in range(1, width-1):
            current= a[i][j]
            neigbours[i][j] = count_neighbours(i,j, a)

    for i in range(1, height-1):
        for j in range(1, width -1):
            a [i][j]= 1 if alive(neigbours[i][j], a[i][j]) else 0
    
    return a

def alive(neighbours, current):
    """ checks if a cell should be alive"""
    if current == 1:
        if neighbours == 2 or neighbours == 3:
            return True
    else:
        if neighbours ==3:
            return True
             
    return False

a = [
    [0, 0, 0, 0, 0], # 01110
    [0, 0, 1, 0, 0], # 02120
    [0, 0, 1, 0, 0], # 
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

a2 = next_life_generation(a)
print_board(a2)
assert a2 == [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
# print()
# a3 = next_life_generation(a2)
# print_board(a3)


