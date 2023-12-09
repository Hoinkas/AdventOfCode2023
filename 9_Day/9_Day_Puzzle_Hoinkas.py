lines = []
with open('AOC_9_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]
  
#---------FIRST PUZZLE SOLUTION---------
def firstPuzzleSoltion(lines):
  import numpy as np

  firstTaskResult = 0

  for line in lines:
    numbers = [[int(num) for num in line.split()]]

    while any(numbers[-1]):
      numbers.append(list(np.diff(numbers[-1])))

    firstTaskResult += sum(diff[-1] for diff in numbers)

  return firstTaskResult

print(firstPuzzleSoltion(lines))

#---------SECOND PUZZLE SOLUTION---------
def secondPuzzleSoltion(lines):
  import numpy as np

  secondTaskResult = 0

  for line in lines:
    numbers = [[int(num) for num in line.split()]]
    numbers[0].reverse()

    while any(numbers[-1]):
      numbers.append(list(np.diff(numbers[-1])))

    secondTaskResult += sum(diff[-1] for diff in numbers)

  return secondTaskResult

print(secondPuzzleSoltion(lines))