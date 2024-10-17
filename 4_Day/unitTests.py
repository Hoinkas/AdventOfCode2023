from FourDayPuzzle_Hoinkas import *
import unittest

lines = []
#Change txt file name to your input
with open('AOC_4Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

firstCase = ['Card 1: 41 86 17 | 83 86  6',
             'Card 2: 20 16 61 | 61 30 68 ',]
secondCase = ['Card 1:  1 21 | 21  1  3']

#Change firstPuzzleSolution() in 20 line with your function name after importing it beforehand
def yourFirstSolution(lines):
  return firstPuzzleSolution(lines)

class TestFirstSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourFirstSolution(lines),firstPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourFirstSolution(firstCase), 13)
    self.assertEqual(yourFirstSolution(secondCase), 2)

#Change secondPuzzleSolution() in 32 line with your function name after importing it beforehand
def yourSecondSolution(lines):
  return secondPuzzleSolution(lines)

class TestSecondSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourSecondSolution(lines),secondPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourSecondSolution(firstCase), 30)
    self.assertEqual(yourSecondSolution(secondCase), 1)

if __name__ == '__main__':
  unittest.main()
