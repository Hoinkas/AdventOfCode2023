lines = []
with open('AOC_9_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FUNCTIONS---------
import numpy as np

def lineSplit(line):
  return [int(num) for num in line.split()]

def proposedSolution(inputPoints):
  points = [inputPoints]

  while any(points[-1]):
    points.append(list(np.diff(points[-1])))

  return sum(diff[-1] for diff in points)
  
def interpolationSolution(points):
  result = 0
  xPoint = len(points)
    
  for i, y in enumerate(points):
    p = 1
    for j in range(len(points)):
      if i != j: p *= (xPoint - j)/(i - j)
    result += y * p

  return round(result)

#---------FIRST PUZZLE SOLUTION---------
def firstPuzzleSoltion(lines):
  firstTaskResult = sum(proposedSolution(lineSplit(line)) for line in lines)
  firstTaskResultWithInterpolation = sum(interpolationSolution(lineSplit(line)) for line in lines)

  return firstTaskResult, firstTaskResultWithInterpolation

print(firstPuzzleSoltion(lines))

#---------SECOND PUZZLE SOLUTION---------
def secondPuzzleSoltion(lines):
  secondTaskResult = sum(proposedSolution(lineSplit(line)[::-1]) for line in lines)
  secondTaskResultWithInterpolation = sum(interpolationSolution(lineSplit(line)[::-1]) for line in lines)

  return secondTaskResult, secondTaskResultWithInterpolation

print(secondPuzzleSoltion(lines))