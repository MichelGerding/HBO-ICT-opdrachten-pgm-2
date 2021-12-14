# wk10ex3.py
#
# Naam: Michel Gerding
#


# functie #1


def create_dictionary(filename):
    """ create a markov chain from the text in a file """
    d = {}
    pw = '$'
    with open(filename, 'r') as f:
        words = f.read().split()
        for nw in words:
            w = nw

            if pw not in d:
                d[pw] = [w]
            else:
                d[pw] += [w]

            pw = '$' if nw[-1] in '.!?' else w

    return d


# assert create_dictionary('./assert1.txt') == {'$': ['Ik', 'Ik'], 'Ik': ['lust', 'eet'], 'lust': ['spam'], 'eet' : ['taart']}
assert create_dictionary('./assert1.txt') == {'$': ['A', 'A', 'B', 'C'], 'A': ['B', 'B', 'C.'], 'B': ['A.', 'C.', 'A'], 'C': ['C', 'C.']}
assert create_dictionary('./assert2.txt') == {'krijg': ['toch'], 'voor': ['de'],'wil': ['taarten', '42'],'toch': ['spam'],'Ik': ['wil', 'krijg', 'wil'],'spam': ['en'],'42': ['en', 'taarten!'],'$': ['Ik', 'Ik', 'Ik'],'taarten': ['en', 'voor'],'de': ['vakantie?'],'en': ['42', 'spam.', 'taarten']}


# functie #2
#
from random import choice 
def generate_text(d, n):
    """ generate a text out of markov chain d with length n"""
    word = '$'
    words = []
    for i in range(n-1):
        nw = choice(d[word])

        words += [nw]
        word = nw

        if nw[-1] in '.!?' or \
            len(d[nw]) == 0:
            word = '$'

    return ' '.join(words)

print(generate_text(create_dictionary('./tekst.txt'), 500))
#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""
O carve not for one, one of happier be it steal sweet respect, Then were to thee. I all your day doth cover And shalt wane so fair a poet's rage, And from me worthy of single wilt prove none'. This were to those gold candles fixed in fresh numbers to thy noon: Unlooked for his middle age, A dearer birth than you are No longer yours, than thou art now appear, But from thy help, by night and look upon my well-contented day, When lofty trees I tell o'er The bounteous largess given thee lie. Duty so sweetly chide thee, Lest my self, but their style I'll read, his for love, to some mother. When thou art old, So shall be the stormy gusts of heaven shines, And night my bootless cries, And then return in hue all silvered o'er The region cloud thou thy worth and thine eyes my rhyme. Shall I for limbs with friends possessed, Desiring this to flow) For to those blots that calls thee this glutton be, Die single and more rich gems: With sun and her blood, Make sweet self at that tells the disgrace: Even for store, Harsh, featureless, and truth. Presume not live? Lo thus by mutual ordering; Resembling sire, and moon, with friends possessed, Desiring this disgrace: Nor shall in thy glory live: Look in my love hath masked him bring forth Eternal numbers number all thy self in heaven's sun one respect, Though thou be termed a tomb Which like to rehearse? And every pen, Reserve them say with spites yet canst not for their age) Be as thy self were some mother. Then can I do sing: Whose strength's abundance am debarred the world, or more hath more praise thee? If the thanks if not persuade me now. Full many a tomb Which time that we must go, Since sweets war upon my love, yea take them I scorn to make That I have drawn thy brav'ry in their art, They draw no form another, Whose fresh ornament, And wear their age) Be not love's strength seem to show me I abide) Intend a jewel (hung in disgrace with frost and more blessed than hate's known injury. For beauty's doom and beauty of my soul's imaginary sight Presents thy self for this, Authorizing thy deceased lover: Compare them for one, Sings this (Time's pencil) or wit, Or to come If it were to be thy self a poet's rage, And puts apparel on thee, Or ten times refigured thee: Then beauteous niggard why dost him for my drooping eyelids open wide, Looking on himself such art now converted are restored, and women's pleasure, Mine be blamed, if thou no quiet find. And there reigns love and confounds In thy good turns eyes my bones with too excellent, For never-resting time leads summer on my love, thou wilt prove me. As he that which he died and cures not made when in my lovers gone, Beauty o'er-snowed and

"""
#
#