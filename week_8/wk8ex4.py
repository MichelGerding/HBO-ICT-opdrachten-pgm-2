def next(n):
    """ Calculate the next number in conways row
        Argument: n the previus number
    """
    txt = str(n)
    numbers =  ''.join(
        x + ('' if x == nxt else '|') 
            for x, nxt in zip(txt, txt[1:] + txt[-1])
    ).split('|')
    
    next_num = ''
    for i in numbers:
        next_num += f'{len(i)}{i[0]}'

    return int(next_num)

assert next(21) == 1211
assert next(2222) == 42
assert next(312211) == 13112221

def read_it(n):
    """ print the numbers in conways row up to itteration n
        Argument: n number of iterations
    """
    current = 1 
    for _ in range(n):
        print(current)
        current = next(current)
