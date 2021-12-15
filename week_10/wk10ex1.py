#
# wk10ex1.py
#
# naam: Michel Gerding
#

# Eerst de klassedefinitie
# Hieronder definiëren we een aantal handige objecten van het type Date
#  +++ bewaar die en/of voeg je eigen toe! +++


class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # de constructor heet altijd __init__ !
    def __init__(self, day, month, year):
        """Construct a Date with the given day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    # de "afdruk"-functie heet altijd __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
        return s

    # Hier is een voorbeeld van een "methode" van de klasse Date:
    def is_leap_year(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        """Returns a new object with the same day, month, year
        as the calling object (self).
        """
        dnew = Date(self.day, self.month, self.year)
        return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way, we don't need to use the awkward
            d.equals(d2) syntax...
        """
        return self.equals(d2)

    def is_before(self, d2):
        """check if current object is after date object d2
        """
        if self.year < d2.year:
            return True
        elif self.year == d2.year and self.month < d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and self.day < d2.day:
            return True
        else:
            return False

    def __lt__(self, d2):
        """ override > opperator to check if current object is after date object d2 """
        return self.is_before(d2)

    def is_after(self, d2):
        """ check if current object is after date object d2 """
        if self.year > d2.year:
            return True
        elif self.year == d2.year and self.month > d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and self.day > d2.day:
            return True
        else:
            return False

    def __gt__(self, d2):
        """ override > opperator to check if current object is after date object d2 """
        return self.is_after(d2)

    def tomorrow(self):
        """ convert current object to hold tommorws date"""
        days = [0,31, 28+self.is_leap_year(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # check if day is the last in the month
        if days[self.month] == self.day:
            # is last of month so set day to 1
            self.day = 1

            if self.month == 12:
                self.month = 1 
                self.year += 1
            else:
                self.month += 1
            # modulo month with 12 and then add 1
        else:
            self.day += 1

    def yesterday(self):
        """convert current class to the previus day"""
        days = [0,31, 28+self.is_leap_year(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.day == 1:
            if self.month == 1:
                self.year -= 1
                self.month = 12
                self.day = 31
            else:
                self.month -= 1
                self.day = days[self.month]
        else:
            self.day -= 1

    def add_n_days(self, n):
        """add a n amount of days by calling self.tommorow"""
        for i in range(n):
            self.tomorrow()
            print(self)
    
    def sub_n_days(self,n): 
        """subtract a n amount of days by calling self.yesterday"""

        for i in range(n):
            self.yesterday()
            print(self)

    def __iadd__(self, n):
        """override the + opperater to call add_n_days"""
        self.add_n_days(n)
        return self

    def __isub__(self, n):
        """ override the - opperator to call sub_n_days"""
        self.sub_n_days(n)
        return self

    def diff(self, d2):
        """Calculate the differnce between 2 days"""
        days_diff = 0
        self_cp = self.copy()
        d2_cp = d2.copy()

        lower, higher, id = (self_cp, d2_cp, "self") if self < d2 else (d2_cp, self_cp, "d2")

        while higher > lower:
            lower.tomorrow()
            days_diff += 1

        if id == 'self':
            days_diff *= -1
        

        return days_diff

    def __sub__(self, d2):
        """override - opperator to get the differnce between 2 dates"""
        return self.diff(d2)

    def dow(self):
        """ get the day of the week """
        # get total amount of days since 0,0,0
        current_day = self.diff(Date(1,1,1))
        return [
            "Monday", 
            "Tuesday", 
            "Wednesday", 
            "Thursday", 
            "Friday", 
            "Saturday", 
            "Sunday"][current_day % 7]


#
# vergeet niet je code voor de klasse Date HIERBOVEN toe te voegen; in de klassedefinitie
#


#
# een aantal datums om mee te werken...
#
# Het handige van ze hier plaatsen is dat ze elke keer dat de software uitgevoerd
#   wordt ze opnieuw gedefinieerd worden (en dat is nodig om te testen!)
#

d = Date(12, 6, 2021)    # Vandaag?
d2 = Date(21, 12, 2021)   # Kerstvakantie
ny = Date(1, 1, 2022)   # Nieuwjaar
nd = Date(1, 1, 2030)   # Nieuw decennium
nc = Date(1, 1, 2100)   # Nieuwe eeuw
graduation = Date(12, 7, 2025)   # Pas dit zelf aan!
vacation = Date(18, 7, 2022)     # Dit ook ~ zomervakantie!
sm1 = Date(28, 10, 1929)    # Krach aandelenbeurs
sm2 = Date(19, 10, 1987)    # Nog een beurskrach: Maandagen in okt. zijn gevaarlijk...


# Tests for date.is_before
assert (d < d2) == True
assert (d < ny) == True
assert (d < graduation) == True
assert (d < vacation) == True
assert (d < sm1) == False
assert (d < sm2) == False
assert (d < nd) == True
assert (d < nc) == True
assert (d < d) == False

# Tests for date.is_after 
assert (d > d2) == False
assert (d > ny) == False
assert (d > graduation) == False
assert (d > vacation) == False
assert (d > sm1) == True
assert (d > sm2) == True
assert (d > nd) == False
assert (d > nc) == False
assert (d > d) == False

# tests for date.tomorrow
nd = Date(12, 6, 2021);     nd.tomorrow()
nd2 = Date(31, 12, 2021);   nd2.tomorrow()
nd3 = Date(31, 1, 2022);    nd3.tomorrow()
nd4 = Date(1, 1, 2100);     nd4.tomorrow()

assert (nd == Date(13, 6, 2021))
assert (nd2 == Date(1, 1, 2022))
assert (nd3 == Date(1, 2, 2022))
assert (nd4 == Date(2, 1, 2100))

# tests for date.yesterday
nd = Date(12, 6, 2021);     nd.yesterday()
nd2 = Date(1, 1, 2022);     nd2.yesterday()
nd3 = Date(1, 2, 2022);     nd3.yesterday()
nd4 = Date(2, 1, 2100);     nd4.yesterday()

assert (nd == Date(11, 6, 2021))
assert (nd2 == Date(31, 12, 2021))
assert (nd3 == Date(31, 1, 2022))
assert (nd4 == Date(1, 1, 2100))

# tests for date.add_n_days
# nd = Date(12, 6, 2021);     nd.add_n_days(10)
# nd2 = Date(31, 12, 2021);   nd2.add_n_days(10)
nd3 = Date(31, 1, 2022);    nd3.add_n_days(10)
nd4 = Date(1, 1, 2100);     nd4.add_n_days(10)


assert (nd == Date(22, 6, 2021))
assert (nd2 == Date(10, 1, 2022))
assert (nd3 == Date(10, 2, 2022))
assert (nd4 == Date(11, 1, 2100))

# tests for Date.sub_n_days
nd = Date(12, 6, 2021);     nd.sub_n_days(10)
nd2 = Date(1, 1, 2022);     nd2.sub_n_days(10)
nd3 = Date(1, 2, 2022);     nd3.sub_n_days(10)
nd4 = Date(2, 1, 2100);     nd4.sub_n_days(10)

assert (nd == Date(2, 6, 2021))
assert (nd2 == Date(22, 12, 2021))
assert (nd3 == Date(22, 1, 2022))
assert (nd4 == Date(23, 12, 2099))

# tests for date.diff and __sub__

nd1 = Date(2, 12, 2020)
nd2 = Date(2, 12, 2020)
nd3 = Date(19, 7, 2021)
nd4 = Date(1, 12, 2019)
nd5 = Date(15, 3, 2020)
assert nd1.diff(Date(1, 1, 1899)) == 44530
assert nd2.diff(Date(1, 1, 2100)) == -28884
assert nd3.diff(nd1) == 229
assert nd1.diff(nd3) == -229
assert nd5.diff(nd4) == 105

# tests for date.dow
assert nd1.dow() == "Wednesday"
assert nd2.dow() == "Wednesday"
assert nd3.dow() == "Monday"
assert nd4.dow() == "Sunday"
assert nd5.dow() == "Sunday"