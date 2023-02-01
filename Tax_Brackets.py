#use bracketed system to determine taxes to be paid
#current brackets are for puerto rico
#adjust and add/subtract for your local tax codes

import math

class Bracket:

    def __init__(self, ll, ul, rate) -> None:
        self.ll = ll
        self.ul = ul
        self.rate = rate

    def tax_paid(self, salary):

        bracket1 = Bracket(0, 9000, 0)
        bracket2 = Bracket(9000, 25000, 0.07)
        bracket3 = Bracket(25000, 41500, 0.14)
        bracket4 = Bracket(41500, 61500, 0.25)
        bracket5 = Bracket(61500, math.inf, 0.33)

        brackets = [bracket5, bracket4, bracket3, bracket2, bracket1]
        tax_paid = 0

        for bracket in brackets:
            if bracket.ll < salary <= bracket.ul:
                tax_paid += (salary - bracket.ll) * bracket.rate
            elif salary > bracket.ul:
                tax_paid += (bracket.ul - bracket.ll) * bracket.rate

        return tax_paid

salary = 85000
bracket = Bracket(0,0,0)
taxes = bracket.tax_paid(salary)
leftover = salary - taxes
monthly = leftover/12
weekly = monthly/4

print(f'''\nYou will pay ${taxes: .2f} in taxes \n 
this will leave you with ${leftover: .2f} annually \n
which is ${monthly: .2f} per month or ${weekly: .2f} per week \n''')


