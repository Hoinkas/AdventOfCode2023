lines = []
with open('AOC_2Day_Quest.txt', 'r', encoding='utf-8') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
import re
rules = {"red": 12, "green": 13, "blue": 14}
firstTaskResult = 0

for line in lines:
  colorsAndValues = re.finditer(f"(\d+) ({'|'.join(rules.keys())})", line)
  isGameValid = all(int(draw.group(1)) <= rules[draw.group(2)] for draw in colorsAndValues)

  if isGameValid:
    numberOfGame = int(re.search(f"Game (\d+)", line).group(1))
    firstTaskResult += numberOfGame

print(firstTaskResult)

#---------SECOND PUZZLE SOLUTION---------
import numpy
secondTaskResult = 0

for line in lines:
  gameMinValuesDict = {"red": 0, "green": 0, "blue": 0}

  for color in gameMinValuesDict.keys():
    valuesOfColor = re.finditer(f"(\d+) {color}", line)
    gameMinValuesDict[color] = max(int(value.group(1)) for value in valuesOfColor)
  
  multipliedMaxValues = numpy.prod(list(gameMinValuesDict.values()))
  secondTaskResult += multipliedMaxValues

print(secondTaskResult)