#use bracketed system to determine taxes to be paid
#current brackets are for us federal single filings
#adjust and add/subtract for your local tax codes

import math

class Bracket:

    def __init__(self, ll, ul, rate) -> None:
        self.ll = ll
        self.ul = ul
        self.rate = rate

    def tax_paid(self, salary):

        bracket1 = Bracket(0, 11000, 0.10)
        bracket2 = Bracket(11001, 44725, 0.12)
        bracket3 = Bracket(44726, 95375, 0.22)
        bracket4 = Bracket(95376, 182100, 0.24)
        bracket5 = Bracket(182101, 231250, 0.32)
        bracket6 = Bracket(231250, 578125, 0.35)
        bracket7 = Bracket(578126, math.inf, 0.37)

        brackets = [bracket7, bracket6, bracket5, bracket4, bracket3, bracket2, bracket1]
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
percent = (taxes/salary)*100
leftover = salary - taxes
monthly = leftover/12
weekly = monthly/4

print(f'''\nYou will pay ${taxes: .2f} in taxes \n
this is {percent: .2f}% of your total salary\n 
this will leave you with ${leftover: .2f} annually \n
which is ${monthly: .2f} per month or ${weekly: .2f} per week \n''')


