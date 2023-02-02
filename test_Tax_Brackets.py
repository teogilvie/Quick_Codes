import unittest
import Tax_Brackets

class TestTaxBrackets(unittest.TestCase):

    def test_tax_paid(self):
        result = Tax_Brackets.Bracket(0,0,0).tax_paid(100000)
        if result < 100000:
            testcase = 1
        else:
            testcase = 0
        self.assertEqual(testcase, 1)

if __name__ == '__main__':
    unittest.main()