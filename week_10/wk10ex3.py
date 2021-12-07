# wk10ex3.py
#
# Naam: Michel Gerding
#


# functie #1
#
def create_dictionary(filename):
    with open(filename, 'r') as f:
        woorden = ''.join(f.readlines()).split(' ')
        word_dict = {}

create_dictionary('./tekst.txt')


# functie #2
#
def generate_text(d, n):
    pass


#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""



"""
#
#