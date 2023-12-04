from ThirdDayPuzzle_Hoinkas import *
import unittest

lines = []
#Change txt file name to your input
with open('AOC_3Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#Cases created by ric2b
#https://www.reddit.com/r/adventofcode/comments/189qyze/comment/kbtg5sd/?utm_source=reddit&utm_medium=web2x&context=3
firstCase = ['........',
             '.24..4..',
             '......*.']
secondCase = ['........',
              '.24$-4..',
              '......*.']
thirdCase = ['11....11',
             '..$..$..',
             '11....11']
fourCase = ['$......$',
            '.1....1.',
            '.1....1.',
            '$......$']
fifthCase = ['$......$',
             '.11..11.',
             '.11..11.',
             '$......$']
sixthCase = ['$11',
             '...',
             '11$',
             '...']
seventhCase = ['$..',
               '.11',
               '.11',
               '$..',
               '..$',
               '11.',
               '11.',
               '..$']
eigthCase = ['11.$.']

#Case created by DERBY_OWNERS_CLUB
#https://www.reddit.com/r/adventofcode/comments/189qyze/comment/kbuhatp/?utm_source=reddit&utm_medium=web2x&context=3
ninthCase = ['.......5......',
              '..7*..*.....4*',
              '...*13*......9',
              '.......15.....',
              '..............',
              '..............',
              '..............',
              '..............',
              '..............',
              '..............',
              '21............',
              '...*9.........']

#Case created by i_have_no_biscuits
#https://www.reddit.com/r/adventofcode/comments/189q9wv/2023_day_3_another_sample_grid_to_use/
tenthCase = ['12.......*..',
             '+.........34',
             '.......-12..',
             '..78........',
             '..*....60...',
             '78.........9',
             '.5.....23..$',
             '8...90*12...',
             '............',
             '2.2......12.',
             '.*.........*',
             '1.1..503+.56']

#Change firstPuzzleSolution() in 60 line with your function name after importing it beforehand
def yourFirstSolution(lines):
  return firstPuzzleSolution(lines)

class TestFirstSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourFirstSolution(lines),firstPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourFirstSolution(firstCase), 4)
    self.assertEqual(yourFirstSolution(secondCase), 32)
    self.assertEqual(yourFirstSolution(thirdCase), 44)
    self.assertEqual(yourFirstSolution(fourCase), 4)
    self.assertEqual(yourFirstSolution(fifthCase), 44)
    self.assertEqual(yourFirstSolution(sixthCase), 22)
    self.assertEqual(yourFirstSolution(seventhCase), 44)
    self.assertEqual(yourFirstSolution(eigthCase), 0)
    self.assertEqual(yourFirstSolution(ninthCase), 108)
    self.assertEqual(yourFirstSolution(tenthCase), 925)

#Change secondPuzzleSolution() in 79 line with your function name after importing it beforehand
def yourSecondSolution(lines):
  return secondPuzzleSolution(lines)

class TestSecondSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourSecondSolution(lines),secondPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourSecondSolution(fifthCase), 0)
    self.assertEqual(yourSecondSolution(ninthCase), 478)
    self.assertEqual(yourSecondSolution(tenthCase), 31600)

if __name__ == '__main__':
  unittest.main()