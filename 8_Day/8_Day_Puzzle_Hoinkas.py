lines = []
with open('AOC_8_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]
  
#---------FIRST PUZZLE SOLUTION---------
def firstPuzzleSolution(lines):
  import re

  instructions = [0 if line == 'L' else 1 for line in [*lines[0]]]
  allSteps = {names[0]: (names[1], names[2]) for line in lines[2:] for names in [re.findall(r"(\w{3})", line)]}

  currentStep = 'AAA'
  numberOfTurn = 0

  while not currentStep == 'ZZZ':
    goLeftOrRight = instructions[numberOfTurn % len(instructions)]
    currentStep = allSteps[currentStep][goLeftOrRight]
    numberOfTurn += 1
    
  return numberOfTurn
print(firstPuzzleSolution(lines))

#---------SECOND PUZZLE SOLUTION---------
def secondPuzzleSolution(lines):
  import re, math

  instructions = [0 if line == 'L' else 1 for line in [*lines[0]]]
  allSteps = {names[0]: [names[1], names[2]] for line in lines[2:] for names in [re.findall(r"(\w{3})", line)]}

  starterSteps = [step for step in allSteps.keys() if step.endswith('A')]
  stepsToChange = starterSteps.copy()
  steps = {}

  numberOfTurn = 0

  while len(steps) < len(starterSteps):
    goLeftOrRight = instructions[numberOfTurn % len(instructions)]

    for i, step in enumerate(stepsToChange):
      stepsToChange[i] = allSteps[step][goLeftOrRight]

      if stepsToChange[i].endswith('Z') and step not in steps:
        steps[starterSteps[i]] = [numberOfTurn + 1, step]

    numberOfTurn += 1

  result = math.lcm(*[item[0] for item in steps.values()])

  return result
print(secondPuzzleSolution(lines))