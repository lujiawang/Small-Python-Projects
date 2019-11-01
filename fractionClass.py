from math import gcd


class Fraction:

    # the constructor for the Fraction class
    # n is the numerator
    # d is the denominator
    # The constructor should create a Fraction object that is reduced
    def __init__(self, n, d=None):
        if d == None and '.' not in n:
            l = n.split('/')
            n = int(l[0])
            d = int(l[1])
        elif d == None and '.' in n:
            l = n.split('.')
            length = len(l[1])
            n = int(l[0]) * 10 ** length + int(l[1])
            d = 10 ** length

        g = gcd(n, d)
        if g is not 1:
            n //= g
            d //= g
        if d < 0:
            d = -d
            n = -n
        if d == 0:
            print('ERROR INPUT')
            exit()
        self.numerator = n
        self.denominator = d

    # Returns a string representation of self. This is needed to print Fractions using print().
    def __str__(self):
        if self.denominator is not 1:
            return str(self.numerator) + '/' + str(self.denominator)
        else:
            return str(self.numerator)

    # Returns a string representation of self. This is needed to print Fractions in a list correctly.
    def __repr__(self):
        return str(self)

    # If f is a Fractions, then ~f returns a Fraction that is the
    # reciprocal of f
    def __invert__(self):
        return Fraction(self.denominator, self.numerator)

    # If f is a Fractions, then -f returns a Fraction that is the
    # negation of f.
    def __neg__(self):
        return Fraction(-1 * self.numerator, self.denominator)

    # If f and g are Fractions, then f + g returns a Fraction that is the
    # sum of f and g
    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    # If f and g are Fractions, then f * g returns a Fraction that is the
    # sum of f and g
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    # If f and g are Fractions, then f - g returns a Fraction that is the
    # difference of f and g

    # You should implement this method without calling the constructor
    def __sub__(self, other):
        return self + (-other)

    # If f and g are Fractions, then f / g returns a Fraction that is the
    # quotient of f and g

    # You should implement this method without calling the constructor.
    def __truediv__(self, other):
        return self * (~other)

    # Returns true if self < other. False otherwise
    def __lt__(self, other):
        return self.numerator / self.denominator < other.numerator / other.denominator

    # Returns true if self == other.  False otherwise
    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    # Returns true if self <= other.  False otherwise
    def __le__(self, other):
        return self.numerator / self.denominator <= other.numerator / other.denominator

    # Returns the absolute value of self. If f is a Fraction, this is called as abs(f).
    def __abs__(self):
        if self.numerator < 0:
            return -self
        else:
            return self

    ##Returns a string representation of self as a mixed number. For example, 12/5 as a mixed number is "2 2/5".
    def mixed_number(self):
        if self.numerator < 0:
            self.numerator = -self.numerator
            num = self.numerator // self.denominator
            num2 = self.numerator % self.denominator
            self.numerator = -self.numerator
            return '-' + str(num) + ' ' + str(num2) + '/' + str(self.denominator)
        else:
            num = self.numerator // self.denominator
            return str(num) + ' ' + str(self.numerator % self.denominator) + '/' + str(self.denominator)


# If you finish and test all of the methods above, you should modify  __init__ so that it can be passed a string
# representation of a fraction, such as "14/102". To do this, modify the definition of __init__ as shown below,

# __init__(self, n, d = None):


# In your code, check to see if d is None. If it is, then n holds the string represenation. If d is not None,
# then n and d are integers representing the numerator and denominator respectively.

# If you finish this part, you should then modify your code so that the string can represnt a number with
# a decimal. For example, "12.354".


a = Fraction("1/3")
print(a)
a
