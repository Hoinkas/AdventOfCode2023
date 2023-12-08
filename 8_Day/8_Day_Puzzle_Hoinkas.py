lines = []
with open('AOC_8_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]
  
#---------FIRST PUZZLE SOLUTION---------
def firstPuzzleSolution(lines):
  import re

  instructions = [0 if line == 'L' else 1 for line in [*lines[0]]]
  allSteps = {}

  for line in lines[2:]:
    allNames = re.findall(r"(\w{3})", line)
    allSteps[allNames[0]] = (allNames[1], allNames[2])

    # ({stepName: (leftStep, rightStep)} for stepName, leftStep, rightStep in re.findall(r"(\w{3})", line) for line in lines[2:])

  currentStep = 'AAA'
  numberOfStep = 0

  while not currentStep == 'ZZZ':
    goLeftOrRight = instructions[numberOfStep % len(instructions)]
    currentStep = allSteps[currentStep][goLeftOrRight]
    numberOfStep += 1
    
  return numberOfStep
# print(firstPuzzleSolution(lines))

#---------SECOND PUZZLE SOLUTION---------

# print(secondPuzzleSolution(lines))