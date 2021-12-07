#
# wk7ex5.py - Aan de slag met lussen!
#
# Naam: Michel Gerding
#

def fac(n):
	""" Loop-based factorial function
		Argument: a nonnegative integer, n
		Return value: the factorial of n
	"""
	result = 1                 # beginwaarde; lijkt op een basisgeval
	for x in range(1, n + 1):  # herhaal van 1 tot en met n
		result = result * x    # pas het resultaat aan door keer x te doen
	return result              # merk op dat dit NA de lus is!

#
# Tests voor de lus-versie van de faculteit
#
assert fac(0) == 1
assert fac(5) == 120

def power(b, p):
	""" loop-based power function
		arguments:  a integer, b
					a possitive integer, p
		Return value: b to the power p
	"""
	if p == 0:
		return 1
	else:
		result = b
		for i in range(p-1):
			result *= b
		return result

assert power(5, 2) == 25
assert power(2, 5) == 32
assert power(42, 0) == 1
assert power(0, 42) == 0
assert power(0, 0) == 1

def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # of result += e
    return result

# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42

def summed_odds(L):
	""" loop-based function to sum all odd numbers in a list
		Argument: a list of intigers, L
		Return value: the sum of all odd intigers of L
	"""
	result = 0
	for i in L:
		if i%2:
			result += i	
	return result

assert summed_odds([4, 5, 6]) == 5
assert summed_odds(range(3, 10)) == 24
assert summed_odds([]) == 0
assert summed_odds([1, 3, 5]) == 9


import random

def count_guesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 tot en met 99
    num_guesses = 1                          # we hebben nu 1 keer geraden
    while guess != hidden:
        guess = random.choice(range(0, 100)) # opnieuw raden!
        num_guesses += 1                     # 1 toevoegen aan het aantal pogingen
    return num_guesses

def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])

def until_a_repeat(high):
	"""
		this is a loop based function that keeps a list of guesed numbers
		until a number is guessed twice. using the function unique to check
		if there are repeat numbers. it also uses a while loop
		Argument: a number, high
		Return value: the number of guesses needed until repaeated number is found
	"""
	guesses = []
	guess = random.choice(range(0, high))
	while guess not in guesses:
		guesses.append(guess)
		guess = random.choice(range(0, high))
	return len(guesses)