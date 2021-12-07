import random
import math

def throw_dart():
    """ Throw a dart randomly between x,y -1 and 1. and check if 
        it is inside a circle with radius 1. we chek if it is in the 
        circle by calculating if the distance to the circle is less then 1
        using the pythagoream theorum. as the radius is always 1 we dont need to 
        get the square root of the radius squared is also 1
        Returns: a random coord
    """

    x, y = random.uniform(-1, 0), random.uniform(-1, 0)

    y = abs(x)**2 + abs(x)**2
    return y <= 1

def for_pi(n):
    """ aproximate pi by throwing darts for n times
        it loops for n times and tests how many darts 
        hit the circle and then devides it by the total
        count and multiplies that by 4
        Argument: n amount of darts to throw. 
        Return: aproximated pi
    """
    count = 0
    for i in range(n):
        if throw_dart():
            count += 1

        print(f'{count} raak van {i} worpen dus pi is {count/(i+1)*4}')
    return 4 * (count/ float(n))



def while_pi(error):
    """test how many darts it takes to approximate pi to a certain error value
    Argument: error: how close we nee to be to pi to stop
    Retrun: amount of darts to come close enough to pi
    
    """

    hits = 0
    throws = 0
    pi = 0
    while abs(pi - math.pi) > error:
        if throw_dart():
            hits += 1
        
        throws += 1
        pi = 4 * (hits / throws)

        print(f'{hits} raak van {throws} worpen dus pi is {pi}')

    return throws
