#
# wk9ex2.py
#
# Naam: Michel Gerding
#


# dit is een functie om tweedimensionale arrays
#  (lijsten van lijsten) af te drukken
def print_2d(a):
    """print_2d prints a 2D array, a
       as rows and columns
       Argument: a, a 2D list of lists
       Result: None (no return value)
    """
    rows = len(a)
    cols = len(a[0])

    for r in range(rows):      # rows == aantal rijen
        for c in range(cols):  # cols == aantal kolommen
            print(a[r][c], end=' ')
        print()

# maak een tweedimensionale array van een ééndimensionale string
def create_a(rows, cols, s):
    """Returns a 2D array with
       rows rows and
       cols cols
       using the data from s: across the
       first row, then the second, etc.
       We'll only test it with enough data!
    """
    a = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row += [s[0]]  # voeg dat karakter toe
            s = s[1:]          # verwijder het eerste karakter
        a += [new_row]
    return a


# een paar tests voor create_a:
a = [['X', ' ', 'O'], ['O', 'X', 'O']]
new_a = create_a(2, 3, 'X OOXO')
assert new_a == a

a = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
new_a = create_a(4, 2, 'XO XOOOX')
assert new_a == a


def in_a_row_3_east(ch, r_start, c_start, a):
    """ check if there are 3 characters in a row of ch 
        to the east of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows or r_start < 0:
        return False
    if c_start > cols -3 or c_start < 0:
        return False

    for i in range(c_start, c_start + 3):
        if a[r_start][i] != ch:
            return False
        
    return True


def in_a_row_3_south(ch, r_start, c_start, a):
    """ check if there are 3 characters in a row of ch 
        to the south of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows - 3 or r_start < 0:
        return False
    if c_start > cols:
        return False

    for i in range(r_start, r_start + 3):
        if a[i][c_start] != ch:
            return False
        
    return True


def in_a_row_3_southeast(ch, r_start, c_start, a):
    """ check if there are 3 characters in a row of ch 
        to the southeast of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows - 3 or r_start < 0:
        return False
    if c_start > cols - 3 or c_start < 0:
        return False

    for i in range(1,  3):
        if a[r_start + i][c_start + i] != ch:
            return False
        
    return True


def in_a_row_3_northeast(ch, r_start, c_start, a):
    """ check if there are 3 characters in a row of ch 
        to the northeast of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows or r_start < 0:
        return False
    if c_start + 2 > cols or c_start < 0:
        return False

    for i in range(3):
        if a[r_start - i][c_start + i] != ch:
            return False
        
    return True



# tests voor in_a_row_3_east
a = create_a(3, 4, 'XXOXXXOOOOOO')
assert not in_a_row_3_east('X', 0, 0, a)
assert in_a_row_3_east('O', 2, 1, a)
assert not in_a_row_3_east('X', 2, 1, a)
assert not in_a_row_3_east('O', 2, 2, a)

# tests voor in_a_row_3_south
a = create_a(4, 4, 'XXOXXXOXXOO OOOX')
assert in_a_row_3_south('X', 0, 0, a)
assert not in_a_row_3_south('O', 2, 2, a)
assert not in_a_row_3_south('X', 1, 3, a)
assert not in_a_row_3_south('O', 42, 42, a)

# tests voor in_a_row_3_southeast
a = create_a(4, 4, 'XOOXXXOXX XOOOOX')
assert in_a_row_3_southeast('X', 1, 1, a)
assert not in_a_row_3_southeast('X', 1, 0, a)
assert in_a_row_3_southeast('O', 0, 1, a)
assert not in_a_row_3_southeast('X', 2, 2, a)
print_2d(a)

# tests voor in_a_row_3_northeast
a = create_a(4, 4, 'XOXXXXOXXOXOOOOX')
assert in_a_row_3_northeast('X', 2, 0, a)
assert in_a_row_3_northeast('O', 3, 0, a)
assert not in_a_row_3_northeast('O', 3, 1, a)
assert not in_a_row_3_northeast('X', 3, 3, a)


def in_a_row_n_east(ch, r_start, c_start, a, n):
    """ check if there are n characters in a row of ch 
        to the east of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows or r_start < 0:
        return False
    if c_start > cols - n or c_start < 0:
        return False

    for i in range(n):
        if a[r_start][c_start + i] != ch:
            return False
        
    return True


def in_a_row_n_south(ch, r_start, c_start, a, n):
    """ check if there are n characters in a row of ch 
        to the south of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows - n or r_start < 0:
        return False
    if c_start > cols or c_start < 0:
        return False

    for i in range(n):
        if a[r_start + i][c_start] != ch:
            return False
        
    return True


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """ check if there are n characters in a row of ch 
        to the southeast of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows - n or r_start < 0:
        return False
    if c_start > cols - n or c_start < 0:
        return False

    for i in range(n):
        if a[r_start + i][c_start + i] != ch:
            return False
        
    return True


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """ check if there are n characters in a row of ch 
        to the northeast of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])


    if r_start > rows or r_start < 0:
        return False
    if c_start + n > cols or c_start < 0:
        return False

    for i in range(n):
        pos = a[r_start - i][c_start + i]
        if pos != ch:
            return False
        
    return True

# tests voor in_a_row_n_east
a = create_a(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
assert in_a_row_n_east('O', 1, 1, a, 4)
assert in_a_row_n_east('O', 1, 3, a, 2)
assert not in_a_row_n_east('X', 3, 2, a, 4)
assert in_a_row_n_east('O', 4, 0, a, 5)


# tests voor in_a_row_n_south
a = create_a(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
assert not in_a_row_n_south('X', 0, 0, a, 5)
assert in_a_row_n_south('O', 1, 1, a, 4)
assert not in_a_row_n_south('O', 0, 1, a, 6)
assert in_a_row_n_south('X', 4, 3, a, 1)


# # tests voor in_a_row_n_southeast
a = create_a(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
assert in_a_row_n_southeast('X', 1, 1, a, 4)
assert not in_a_row_n_southeast('O', 0, 1, a, 3)
assert in_a_row_n_southeast('O', 0, 1, a, 2)
assert not in_a_row_n_southeast('X', 3, 0, a, 2)


# # tests voor in_a_row_n_northeast
a = create_a(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
assert in_a_row_n_northeast('X', 4, 0, a, 5)
assert in_a_row_n_northeast('O', 4, 1, a, 4)
assert not in_a_row_n_northeast('O', 2, 0, a, 2)
assert not in_a_row_n_northeast('X', 0, 3, a, 1)