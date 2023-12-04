lines = []
with open('AOC_3Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

import re, pandas as pd, numpy

def checkOverlaping(charIndex, number: re.Match):
  if number.start() >= charIndex-3 and number.end() <= charIndex+3:
    firstInterval = pd.Interval(charIndex-1, charIndex+1)
    secondInterval = pd.Interval(number.start(), number.end(), closed='left')

    return secondInterval.overlaps(firstInterval)

# #---------FIRST PUZZLE SOLUTION---------
def firstPuzzleSolution(lines):
  firstTaskResult = 0
  specialCharDictList = []

  for i in range(len(lines)):
    #List of special characters
    specialCharsInRow = re.finditer(f"[^\w\s.]", lines[i])
    charsDict = {}

    for specialChar in specialCharsInRow:
      if len(specialChar.group(0))> 0: 
        charsDict[int(specialChar.start())] = specialChar.group(0)
    
    specialCharDictList.append(charsDict)

  for row in range(len(specialCharDictList)):
    for charIndex in specialCharDictList[row]:
      for j in range(-1,2):
        if 0 <= row+j < len(specialCharDictList):
          specialNumsInRow = re.finditer(f"\d+", lines[row+j])
          firstTaskResult += sum([int(specialNum.group(0)) for specialNum in specialNumsInRow if(checkOverlaping(charIndex, specialNum))])
              
  return firstTaskResult
# print(firstPuzzleSolution(lines))
#---------Second PUZZLE SOLUTION---------
def secondPuzzleSolution(lines):
  secondTaskResult = 0
  specialCharDictList = []

  for i in range(len(lines)):
    #List of special characters
    specialCharsInRow = re.finditer(f"[*]", lines[i])
    charsDict = {}

    for specialChar in specialCharsInRow:
      if len(specialChar.group(0))> 0: 
        charsDict[int(specialChar.start())] = specialChar.group(0)
    
    specialCharDictList.append(charsDict)

  for row in range(len(specialCharDictList)):
    for charIndex in specialCharDictList[row]:
      numbersToMultiply = []
      for j in range(-1,2):
        if 0 <= row+j < len(specialCharDictList):
          specialNumsInRow = re.finditer(f"\d+", lines[row+j])

          for specialNum in specialNumsInRow:
            if(checkOverlaping(charIndex, specialNum)):
              numbersToMultiply.append(int(specialNum.group(0)))

      if(len(numbersToMultiply)>1):
        secondTaskResult += numpy.prod(numbersToMultiply)
              
  return secondTaskResult
print(secondPuzzleSolution(lines))