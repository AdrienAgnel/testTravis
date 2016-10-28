import unittest
import numpy
import itertools

class Calculator:

    def add(self, input=None):
        if input:
            #input = input.split('//')
            #input = [x[1:].split(x[0]) for x in input if len(x)>0]
            #input = itertools.chain(*input)
            input = input.split(',')
            input = [x.split('\n') for x in input]
            input = itertools.chain(*input)
            input = list(input)
            print(input)
            tot = 0
            for element in input:
                tot += int(element)
            return tot
        else:
            return 0

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_noEntry(self):
        self.assertEqual(0,self.calc.add())

    def test_emptyEntry(self):
        self.assertEqual(0,self.calc.add(""))

    def test_oneEntry(self):
        self.assertEqual(1,self.calc.add("1"))

    def test_twoEntry(self):
        self.assertEqual(13,self.calc.add("4,9"))

    def test_unknownEntry(self):
        n = numpy.random.randint(3,99)
        numbersArray = numpy.random.randint(0,10,n)
        tot = numbersArray.sum()
        #test
        self.assertEqual(tot, self.calc.add(','.join(map(str,numbersArray))))

    def test_lineBreak(self):
        self.assertEqual(12, self.calc.add("2\n4,2\n1,3"))


if __name__ == '__main__':
    unittest.main()
