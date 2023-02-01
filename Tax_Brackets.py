#use bracketed system to determine taxes to be paid

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

        brackets = [bracket1, bracket2, bracket3, bracket4, bracket5]
        tax_paid =0

        for bracket in brackets:
            if salary > bracket.ul:
                tax_paid += (bracket.ul - bracket.ll) * bracket.rate
                salary -= (bracket.ul - bracket.ll)
            else:
                tax_paid += (salary-bracket.ll) * bracket.rate
                break
        return tax_paid

salary = 45000
taxes = format(Bracket(0,0,0).tax_paid(salary), '.2f')
leftover = format(salary - float(taxes), '.2f')
monthly = format(float(leftover)/12, '.2f')
weekly = format(float(monthly)/4, '.2f')

print(f'''\nYou will pay ${taxes} in taxes \n 
this will leave you with ${leftover} annually \n
which is ${monthly} per month or ${weekly} per week \n''')


