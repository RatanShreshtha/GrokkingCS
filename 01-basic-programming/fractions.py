class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    @staticmethod
    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


f1 = Fraction(3, 4)
print(f1)
f2 = Fraction(1, 2)
print(f2)
f3 = f1 + f2
print(f3)
print(f3 == f1)


fibonacci_lookups = {}

def fibonacci_memoization(n):

    if n in fibonacci_lookups:
        return fibonacci_lookups[n]

    if n < 2:  # base case
        fibonacci_lookups[n] = n
        return fibonacci_lookups[n]

    fibonacci_lookups[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)

    return fibonacci_lookups[n]


fibonacci_table = [0, 1]

def fibonacci_tabulation(n):

    for i in range(2, n):
        fib_num = fibonacci_table[i - 1] + fibonacci_table[i - 2]
        fibonacci_table.append(fib_num)
    
    return fibonacci_table[n]


n = 510
fibonacci_memoization(n)

fibonacci_memoization_lru_cache(n)
