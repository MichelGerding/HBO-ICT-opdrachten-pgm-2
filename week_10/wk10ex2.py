
def in_a_row_n_east(ch, r_start, c_start, a, n):
    """ check if there are n characters in a row of ch 
        to the east of r_start and c_start in 2d array a
    """
    rows = len(a)
    cols = len(a[0])

    if r_start > rows:
        return False
    if c_start > cols - n:
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

    if r_start > rows - n:
        return False
    if c_start > cols:
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

    if r_start > rows - n:
        return False
    if c_start > cols - n:
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


    if r_start > rows:
        return False
    if c_start + n > cols:
        return False

    for i in range(n):
        if a[r_start - i][c_start + i] != ch:
            return False
        
    return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord

        # hier moeten de nummers nog onder gezet worden
        s += '\n'
        for i in range(self.width):
            s += ' '+ str(i%10)
        return s       # het bord is compleet, geef het terug

    def add_move(self, col, ox):
        """place a move in column col for player ox"""
        for i in range(self.height, 0, -1):
            if self.data[i-1][col] == ' ': 
                self.data[i-1][col] = ox
                break

    def clear(self):
        """clear the board"""
        self.data = [[' ']*self.width for row in range(self.height)]

    def set_board(self, move_string):
        """ Accepts a string of columns and places
            alternating checkers in those columns,
            starting with 'X'.

            For example, call b.set_board('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.set_board('000000') to
            see them alternate in the left column.

            move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col):
        """check if a move is valid"""
        if col < 0 or col >= self.width:
            return False
        elif not (self.data[0][col] == ' '): 
            return False
        else:
            return True

    def is_full(self):
        """ chek if the boards spaces all have been filled"""
        for i in range(self.width):
            if self.data[0][i] == ' ':
                return False
        return True

    def del_move(self, col):
        """delete the last move in a column"""
        for i in range(self.height):
            if not (self.data[i][col] == ' '):
                self.data[i][col] = ' '
                break

    def wins_for(self, ox):
        """ check if user ox has won"""
        for i in range(self.height):
            for j in range(self.width):
                field = self.data[i][j]
                if in_a_row_n_south(ox, i, j, self.data, 4):
                    return True
                elif in_a_row_n_east(ox, i, j, self.data, 4):
                    return True
                elif in_a_row_n_northeast(ox, i, j, self.data, 4):
                    return True
                elif in_a_row_n_southeast(ox, i, j, self.data, 4):
                    return True
        return False
                    

    def host_game(self):
        """play the game"""

        print('Welkom bij Vier op een rij!')
        curr_player = 'X'
        while True:
            print('\n\n' + str(self), end='\n\n')

            # get user move
            users_col = -1
            while not self.allows_move(users_col):
                users_col = int(input(f"Keuze van {curr_player}:    "))
            self.add_move(users_col, curr_player)
                

            # check for end of game
            if self.wins_for(curr_player):
                print(f"{curr_player} wint -- Gefeliciteerd!")
                break
            elif self.is_full():
                print('Het was gelijk spel')
                break

            curr_player = 'O' if curr_player == 'X' else 'X'


## tests for add_move
b = Board(7,6)

b.add_move(0, 'X')
b.add_move(0, 'O')
b.add_move(0, 'X')
b.add_move(3, 'O')
b.add_move(4, 'O')
b.add_move(5, 'O')
b.add_move(6, 'O')

assert str(b) == '| | | | | | | |\n| | | | | | | |\n| | | | | | | |\n|X| | | | | | |\n|O| | | | | | |\n|X| | |O|O|O|O|\n---------------\n 0 1 2 3 4 5 6'

# print(b)

# tests for allow board
b = Board(2, 2)

b.add_move(0, 'X')
b.add_move(0, 'O')

# print(b)
assert b.allows_move(-1) == False
assert b.allows_move(0) == False
assert b.allows_move(1) == True
assert b.allows_move(2) == False


# tests for is_full
b = Board(2, 2)
assert b.is_full() == False

b.set_board('0011')
assert b.is_full() == True


# tests for del_move
b = Board(2, 2)

b.set_board('0011')
b.del_move(1)
b.del_move(1)
b.del_move(1)
b.del_move(0)

assert str(b) == '| | |\n|X| |\n-----\n 0 1'


# tests for wins_for
b = Board(7, 6)
b.set_board('00102030')
assert b.wins_for('X') == True
assert b.wins_for('O') == True

b = Board(7, 6)
b.set_board('23344545515')
assert b.wins_for('X') == True
assert b.wins_for('O') == False


b = Board(7,6)
b.host_game()