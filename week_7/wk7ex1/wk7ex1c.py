#
# wk7ex1c.py - uniekheid controleren  (voor de random-number generator in Hmmm)
#    De functie test(s) staat hier al in (onderaan).
#
# Naam:
#
# Je plakt je 100 getallen in deze triple-quoted string:
NUMBERS = """
85
88
51
74
57
0
3
66
89
72
15
18
81
4
87
30
33
96
19
2
45
48
11
34
17
60
63
26
49
32
75
78
41
64
47
90
93
56
79
62
5
8
71
94
77
20
23
86
9
92
35
38
1
24
7
50
53
16
39
22
65
68
31
54
37
80
83
46
69
52
95
98
61
84
67
10
13
76
99
82
25
28
91
14
97
40
43
6
29
12
55
58
21
44
27
70
73
36
59
42
"""


def unique(L):
    """
    This should be your uniqueness-tester, written for week 7
    Usually, it uses the recursive pattern:

    if ...      # handle base case
    elif ...    # check whether L[0] re-appears
    else ...    # otherwise...
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
       return unique(L[1:])



def test(s):
    """test accepts a triple-quoted string, s,
       containing one number per line. Then, test
       returns True if those numbers are all unique
       (or if s is empty); otherwise it returns False
    """
    s = s.strip()                 # haal alle spaties aan het begin en eind van s weg
    list_of_strings = s.split()   # splits s op elke spatie en nieuwe regel
    # print("list_of_strings is", list_of_string)
    list_of_integers = [int(s) for s in list_of_strings]  # converteer ze allemaal naar ints
    # print("list_of_integers is", list_of_integers)
    return unique(list_of_integers)


# Uitproberen!
result = test(NUMBERS)
print("\nTest op uniekheid:  Het resultaat is", result)
