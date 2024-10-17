lines = []
with open('AOC_2Day_Quest.txt', 'r', encoding='utf-8') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
import re
rules = {"red": 12, "green": 13, "blue": 14}
firstTaskResult = 0

for line in lines:
  matches = re.finditer(r"(\d+) ({'|'.join(rules.keys())})", line)
  isGameValid = all(int(match.group(1)) <= rules[match.group(2)] for match in matches)

  if isGameValid:
    numberOfGame = int(re.search(r"Game (\d+)", line).group(1))
    firstTaskResult += numberOfGame

print(firstTaskResult)

#---------SECOND PUZZLE SOLUTION---------
import numpy as np
secondTaskResult = 0

for line in lines:
  gameMinValuesDict = {"red": 0, "green": 0, "blue": 0}

  for color in gameMinValuesDict.keys():
    valuesOfColor = re.finditer(r"(\d+) {color}", line)
    gameMinValuesDict[color] = max(int(value.group(1)) for value in valuesOfColor)
  
  multipliedMaxValues = np.prod(list(gameMinValuesDict.values()))
  secondTaskResult += multipliedMaxValues

print(secondTaskResult)