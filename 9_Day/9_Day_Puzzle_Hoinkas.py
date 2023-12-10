import time

lines = []
with open('AOC_9_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FUNCTIONS---------
import numpy as np

def proposedSolution(points):
  while any(points[-1]):
    points.append(list(np.diff(points[-1])))

  result = sum(diff[-1] for diff in points)
  return result
  
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
  firstTaskResult = 0

  for line in lines:
    points = [[int(num) for num in line.split()]]
    firstTaskResult += proposedSolution(points)
  
  return firstTaskResult

start = time.time()
print(firstPuzzleSoltion(lines))
end = time.time()
print(f'First task without interpolation: {round((end-start)*1000,2)}ms')

#---------FIRST PUZZLE SOLUTION WITH LAGRANGE INTERPOLATION---------
def firstPuzzleSoltionWithInterpolation(lines):
  firstTaskResult = 0

  for line in lines:
    points = [int(num) for num in line.split()]
    firstTaskResult += interpolationSolution(points)

  return firstTaskResult

start = time.time()
print(firstPuzzleSoltionWithInterpolation(lines))
end = time.time()
print(f'First task with interpolation: {round((end-start)*1000,2)}ms')

#---------SECOND PUZZLE SOLUTION---------
def secondPuzzleSoltion(lines):
  secondTaskResult = 0

  for line in lines:
    points = [[int(num) for num in line.split()][::-1]]
    secondTaskResult += proposedSolution(points)

  return secondTaskResult

start = time.time()
print(secondPuzzleSoltion(lines))
end = time.time()
print(f'Second task without interpolation: {round((end-start)*1000,2)}ms')

#---------SECOND PUZZLE SOLUTION WITH LAGRANGE INTERPOLATION---------
def secondPuzzleSoltionWithInterpolation(lines):
  secondTaskResult = 0

  for line in lines:
    points = [int(num) for num in line.split()][::-1]
    secondTaskResult += interpolationSolution(points)

  return secondTaskResult

start = time.time()
print(secondPuzzleSoltionWithInterpolation(lines))
end = time.time()
print(f'Second task with interpolation: {round((end-start)*1000,2)}ms')