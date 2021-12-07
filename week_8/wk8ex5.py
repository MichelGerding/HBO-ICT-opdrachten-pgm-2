def print_rect(width, height, symbol):
    """ print a rectabgle of width * height out of the character symbol
        Arguments:  width: a integer
                    height: a integer
                    symbol: a charater
    """

    res = ''
    for _ in range(height):
        for _ in range(width):
            res += symbol + ' '
        res += '\n'
    
    print(res)
# print_rect(4, 6, '%')

def print_triangle(width, symbol, right_side_up):
    """ print a triangle of width for a certain symbol.
        if right side up is true it will put the smallest side up
        Arguments:  width: a integer
                    symbol: a charater
                    right_side_up: a boolean
    """
    
    rng = range(1, width+1) if right_side_up else range(width, 0, -1)
    for w in rng:
        for i in range(w):
            print(symbol, end=' ' if w-1 != i else '\n')


def print_bumps(num, symbol1, symbol2):
    """ print num amount of in size increasing bumps with switching symbols
        Arguments:  num: a integer
                    symbol1: a charater
                    symbol2: a charater
    """

    for i in range(1,num+1):
        # print(i)
        print_triangle(i, symbol1, True)
        print_triangle(i, symbol2, False)
    
# print_bumps(4, '%', '#')

def print_diamond(width, symbol):
    """ print a diamond shape with a width out of a given character
        Arguments:  width: a integer
                    symbol: a charater
    """
    total_width = width + (width-1)

    for i in list(range(1, width)) + list(range(width, 0, -1)):
        left_spaces = total_width - (i +2)
        s = ' '*left_spaces
        for _ in range(i):
            print(_)
            s += symbol + ' '

        print(s)
# print_diamond(3, '&')
def print_striped_diamond(width, sym1, sym2):
    """ print a striped diamond with a width out of a given character
        Arguments:  width: a integer
                    sym1: a charater
                    sym2: a charater
    """
    li =[]

    for i in range(width):
        lin = []
        for j in range(width):
            # s += str(i%2)
            lin.append(sym1 if i % 2 == 0 else sym2)
        li.append(lin)

    # rotate array by 45 deg and fill with spaces
    ctr = 0
    while(ctr < 2 * width-1):
        print(" "*abs(width-ctr-1), end ="")
        lst = []
        for i in range(width):
            for j in range(width):
                if i + j == ctr:
                    lst.append(li[i][j])
 
        # Printing Diagonal
        print(*lst)
        ctr += 1

# print_striped_diamond(7, '.', '%')

def print_crazy_striped_diamond(width, sym1, sym2, sym1_width, sym2_width):
    """ print a striped diamond with a width out of a given character
        Arguments:  width: a integer
                    sym1: a charater
                    sym2: a charater
                    sym1_width: a int greater then 0
                    sym2_width: a int greater then 0
    """
    li =[]
    lines = 0
    curr_sym1 = True

    for i in range(width):
        lin = []
        for j in range(width):
            # s += str(i%2)
            lin.append(sym1 if curr_sym1 else sym2)

        lines += 1
        if lines >= (sym1_width if curr_sym1 else sym2_width):
            curr_sym1 = not curr_sym1
            lines = 0

        li.append(lin)

    # rotate array by 45 deg and fill with spaces
    ctr = 0
    while(ctr < 2 * width-1):
        print(" "*abs(width-ctr-1), end ="")
        lst = []

        for i in range(width):
            for j in range(width):
                if i + j == ctr:
                    lst.append(li[i][j])
 
        # Printing Diagonal
        print(*lst)
        ctr += 1

# print_crazy_striped_diamond(7, '.', '%', 2, 1)