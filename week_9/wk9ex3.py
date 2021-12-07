import math


def p_sum(l):
    """count all entries in a list"""
    tot = 0
    for i in l:
        tot += i
    return tot

def p_max(l):
    """ get max of a list
    """
    curr_max =l[0]
    for i in l[1:]:
        if i > curr_max:
            curr_max = i

    return curr_max


def p_avg(l):
    """ get average of list
    """
    total = 0

    for i in l:
        total += i
    return total / len(l)


def p_max(l):
    """get max of a list together with its index"""
    max= l[0]
    ind = 0
    for i, val in enumerate(l):
        if val > max:
            max = val
            ind = i
    return max, ind

def get_new_list():
    """ ask the user for a new list and 
        parse it without using eval
    """
    user_inp = input('Voer een nieuwe lijst in: ')

    array = []
    curr_string = ''
    for c in user_inp:
        if c.isdigit():
            curr_string += c
        else:
            if len(curr_string) > 0:
                array.append(int(curr_string))
            curr_string = ''

    return array

def print_list(arr):
    """ print the given list in a specific style
    """
    days = len(arr)
    max_price = p_max([len('{:.2f}'.format(i)) for i in arr])

    days_len = len(str(days))
    len_of_max_price = max_price
    
    days_str_len = days_len if days_len > 3 else 3
    prices_len = len_of_max_price if len_of_max_price > 5 else 5
    format_str = '{0: >'+ str(days_str_len) + '}   {1: >' + str(prices_len) + '}'
    print(format_str.format('Dag', 'Prijs'))
    print('-'*days_str_len + ' -' + '-'*prices_len)
    
    format_str = '{0: >'+ str(days_str_len) + '}   {1: >' + str(prices_len) + '.2f}'
    for i in range(days):
        print(format_str.format(i, arr[i]))


    
def st_dev(l):
    """get the standart deviation of a list
    """    
    n = len(l)
    avg = p_sum(l) / n

    return math.sqrt(p_sum([(x - avg) **2 for x in l]) / n)

def min_ind(l):
    """get the index of the lowest number in a list"""
    min = l[0]
    ind = 0
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
            ind = i

    return ind
def max_diff_ind(a):
    """calculate the max differnce and return the indexes"""
    max_diff = a[1] - a[0]
    min_ind, max_ind = 0, 1
    for i in range( 0, len(a) ):
        for j in range( i+1, len(a) ):
            if(a[j] - a[i] > max_diff):
                max_diff = a[j] - a[i]
                min_ind, max_ind = i, j
    return min_ind, max_ind

def invest_strat(l):
    """get the optimal investing strat"""
    min_ind, max_ind = max_diff_ind(l)

    print(f'''Je TRI investeringsstrategie is om

Te kopen op dag {min_ind}  voor prijs {l[min_ind]}
Te verkopen op dag {max_ind}  voor prijs 3{l[max_ind]}

Dit geeft een totale winst van {l[max_ind] - l[min_ind]}''')




def menu():
    return """(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen"""

def main ():
    current_list = [20, 10, 30]
    while True:
        print(menu() +  '\n')
        user_input = input('Maak je keuze: ')

        # parse user input to int
        try:
            user_choice = int(user_input)
            if not (user_choice in [0,1,2,3,4,5,6,9]):
                print('Ik heb die keuze niet verstaan. Probeer opnieuw')
                continue
        except ValueError:
            print('Ik heb die keuze niet verstaan. Probeer opnieuw')
            continue

        # keuzes
        if user_choice == 9:
            break
        elif user_choice == 0:
            current_list = get_new_list()
        elif user_choice == 1:
            if len(current_list) > 0:
                print('De huidige lijst is leeg')
            else:
                print_list(current_list)
        elif user_choice == 2:
            print(f'de gemiddelde prijs is {p_avg(current_list)}')
        elif user_choice == 3:
            print(f'de standaarrtafwijking is {st_dev(current_list)}')
        elif user_choice == 4:
            min = min_ind(current_list)
            print(f'Het minimun is {current_list[min]} op dag ')
        elif user_choice == 5:
            max = max()
        elif user_choice == 6:
            invest_strat(current_list)

    print('Tot later')

