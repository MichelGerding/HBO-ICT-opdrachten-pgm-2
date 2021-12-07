# wk8ex1.py
# Practicum 8
#
# Naam:
#

# laat deze importregel staan...
from png import *


#
# een testfunctie...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300, 200)  # maak een afbeelding met width=300, height = 200

    # Geneste lussen!
    for r in range(200):  # lust over de rijen met lusvariabele r
        for c in range(300):  # lust over de kolommen met c
            if c == r:
                im.plot_point(c, r, (255, 0, 0))
            # else:
            #    im.plot_point( c, r, (255,0,0))

    im.save_file()

#
# zet je functies van Practicum 8 hieronder neer:
#
def mult(c, n):
    """Mult uses only a loop and addition
       to multiply c by the positive integer n
    """
    result = 0
    for i in range(n):
        result += c
    return result

assert mult(3, 5) == 15
assert mult(3, 6) == 18
assert mult(3, 7) == 21
assert mult(3, 8) == 24
assert mult(3, 9) == 27
assert mult(3, 10) == 30

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z = 0
    for i in range(n):
        z = (z ** 2) + c
    return z

assert update(1, 3) == 5
assert update(-1, 3) == -1
assert update(1, 10) == 3791862310265926082868235028027893277370233152247388584761734150717768254410341175325352026
assert update(-1, 10) == 0

def in_mset(c,n):
    """in_mset accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
       Then, it returns
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0 + 0j
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

assert in_mset(0 + 0j, 25) == True
assert in_mset(3 + 4j, 25) == False
assert in_mset(0.3 + -0.5j, 25) == True
assert in_mset(-0.7 + 0.3j, 25) == False
assert in_mset(0.42 + 0.2j, 25) == True
assert in_mset(0.42 + 0.2j, 50) == False 

def we_want_this_pixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0 or row % 10 == 0:
        return True
    else:
        return False

    """
        als je de lijn `if col % 10 == 0 and row % 10 == 0`
        naar `if col % 10 == 0 or row % 10 == 0` aanpast
        dan krijg je horizonaal en verticale lijnen ipv stippen
    """

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # maak een lus om wat pixels te tekenen

    for col in range(width):
        for row in range(height):
            if we_want_this_pixel(col, row):
                image.plot_point(col, row)

    # we hebben door alle pixels gelust; nu schrijven we het bestand

    image.save_file()

def scale(pix, pix_max, float_min, float_max):
    """arguments:
           pix, the CURRENT pixel column (or row)
           pix_max, the total # of pixel columns
           float_min, the min floating-point value
           float_max, the max floating-point value
       returns values: the floating-point value that
           corresponds to pix
    """
    if pix == 0:
        return float_min
    elif pix == pix_max:
        return float_min
    else:
        return float_min + ((pix / pix_max) * (float_max - float_min))

# tests for scale
assert scale(100, 300, -2.0, 1.0) == -1.0
assert scale(100, 200, -2.0, 1.0) == -0.5
assert scale(25, 300, -2.0, 1.0) == -1.75


def mset():
    """
        Create a image with dimensions 300*200 
        of the mandelbrot set
    """
    NUM_ITER = 100  # aantal updates
    XMIN = -2.0   # de kleinste waarde voor de reële coördinaat
    XMAX = 1.0    # de grootste waarde voor de reële coördinaat
    YMIN = -1.0   # de kleinste waarde voor de imaginaire coördinaat
    YMAX = 1.0    # de grootste waarde voor de imaginaire coördinaat
    
    width = 1200
    height = 800
    image = PNGImage(width, height)

    # maak een lus om wat pixels te tekenen

    for col in range(width):
        for row in range(height):
            # Gebruik scale twee keer:
            #   één keer om het reële deel van c te bepalen (x)
            x = scale(col, width, XMIN, XMAX)
            #   één keer om het imaginaire deel van c te bepalen (y)
            y = scale(row, height, YMIN, YMAX)
            # DAARNA ken je c toe, kies je n en test je:
            c = x + y*1j
            if in_mset(c, NUM_ITER):
                image.plot_point(col, row, gen_color(col, row, height, width))
            else:
                image.plot_point(col, row, (255,255,255))

    # we hebben door alle pixels gelust; nu schrijven we het bestand
    image.save_file()

def gen_color(x, y, height, width):
    """
        generate a column for given x,y coord
    """

    return int(scale(x, width, 55,255)), int(scale(y, height, 55,255)), int(scale(x+y, height+width, 55,255)) 

mset()
