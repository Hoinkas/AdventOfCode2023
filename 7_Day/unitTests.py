from SeventhDayPuzzle_Hoinkas import *
import unittest

lines = []
#Change txt file name to your input
with open('AOC_7Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#Cases provided by LxsterGames
#https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
firstCase = ['JJJJJ 37',
             'AAAAA 61']

secondCase = ['Q2KJJ 13',
             'Q2Q2Q 19',
             'T3T3J 17']

thirdCase = ['2345A 1',
             'Q2KJJ 13',
             'Q2Q2Q 19',
             'T3T3J 17',
             'T3Q33 11',
             '2345J 3',
             'J345A 2',
             '32T3K 5',
             'T55J5 29',
             'KK677 7',
             'KTJJT 34',
             'QQQJA 31',
             'JJJJJ 37',
             'JAAAA 43',
             'AAAAJ 59',
             'AAAAA 61',
             '2AAAA 23',
             '2JJJJ 53',
             'JJJJ2 41',]

#Change firstPuzzleSolution() in 20 line with your function name after importing it beforehand
def yourFirstSolution(lines):
  return firstPuzzleSolution(lines)

class TestFirstSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourFirstSolution(lines),firstPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourFirstSolution(firstCase), 159)
    self.assertEqual(yourFirstSolution(secondCase), 104)
    self.assertEqual(yourFirstSolution(thirdCase), 6592)

#Change secondPuzzleSolution() in 32 line with your function name after importing it beforehand
def yourSecondSolution(lines):
  return secondPuzzleSolution(lines)

class TestSecondSolution(unittest.TestCase):
  def test_given_case(self):
    self.assertEqual(yourSecondSolution(lines),secondPuzzleSolution(lines))
  
  def test_community_cases(self): 
    self.assertEqual(yourSecondSolution(firstCase), 159)
    self.assertEqual(yourSecondSolution(secondCase), 104)
    self.assertEqual(yourSecondSolution(thirdCase), 6839)

if __name__ == '__main__':
  unittest.main()
