from FourDayPuzzle_Hoinkas import *
import unittest

lines = []
#Change txt file name to your input
with open('AOC_4Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

firstCase = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
             'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
             'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
             'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
             'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
             'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

#Change firstPuzzleSolution() in 60 line with your function name after importing it beforehand
def yourFirstSolution(lines):
  return firstPuzzleSolution(lines)

class TestFirstSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourFirstSolution(lines),firstPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourFirstSolution(firstCase), 13)

#Change secondPuzzleSolution() in 79 line with your function name after importing it beforehand
def yourSecondSolution(lines):
  return secondPuzzleSolution(lines)

class TestSecondSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourSecondSolution(lines),secondPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourSecondSolution(firstCase), 30)

if __name__ == '__main__':
  unittest.main()