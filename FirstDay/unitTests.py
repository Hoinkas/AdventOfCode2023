from FirstDayPuzzle_Hoinkas import *
import unittest

lines = []
#Change txt file name to your input
with open('AOC_1Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#Cases created by tipx2
#https://www.reddit.com/r/adventofcode/comments/189hjm2/comment/kbr77w8/?utm_source=reddit&utm_medium=web2x&context=3
firstCase = ['36twonine']
secondCase = ['3nqqgfone']
thirdCase = ['mkfone4ninefour']
fourthCase = ['kgnprzeight7nine']

fifthCase = ['oneight1']

#Change firstPuzzleSolution() in 21 line with your function name after importing it beforehand
def yourFirstSolution(lines):
  return firstPuzzleSolution(lines)

class TestFirstSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourFirstSolution(lines),firstPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourFirstSolution(firstCase), 36)
    self.assertEqual(yourFirstSolution(secondCase), 33)
    self.assertEqual(yourFirstSolution(thirdCase), 44)
    self.assertEqual(yourFirstSolution(fourthCase), 77)
    self.assertEqual(yourFirstSolution(fifthCase), 11)

#Change secondPuzzleSolution() in 36 line with your function name after importing it beforehand
def yourSecondSolution(lines):
  return secondPuzzleSolution(lines)

class TestSecondSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourSecondSolution(lines),secondPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourSecondSolution(firstCase), 39)
    self.assertEqual(yourSecondSolution(secondCase), 31)
    self.assertEqual(yourSecondSolution(thirdCase), 14)
    self.assertEqual(yourSecondSolution(fourthCase), 89)
    self.assertEqual(yourSecondSolution(fifthCase), 11)

if __name__ == '__main__':
  unittest.main()