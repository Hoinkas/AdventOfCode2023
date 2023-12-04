lines = []
with open('AOC_3Day_Quest.txt', 'r', encoding='utf-8') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

# #---------FIRST PUZZLE SOLUTION---------
import re, pandas as pd

def firstPuzzleSolution(lines):
  firstTaskResult = 0
  specialCharDictList = []
  specialNumDictList = []

  for i in range(len(lines)):
    #List of special characters
    specialCharsInRow = re.finditer(f"[^\w\s.]", lines[i])
    charsDict = {}

    for specialChar in specialCharsInRow:
      if len(specialChar.group(0))> 0: 
        charsDict[int(specialChar.start())] = specialChar.group(0)
    
    specialCharDictList.append(charsDict)

    #List of numbers
    specialNumsInRow = re.finditer(f"\d+", lines[i])
    numDict = {}

    for specialNum in specialNumsInRow:
      if len(specialNum.group(0))> 0:
        numDict[int(specialNum.start())] = int(specialNum.group(0))

    specialNumDictList.append(numDict)

  def checkOverlaping(indexToCheck, indexOfNumber, number):
    firstInterval = pd.Interval(indexToCheck-1, indexToCheck+1, closed='both')
    secondInterval = pd.Interval(indexOfNumber, indexOfNumber + len(str(number)) - 1, closed='both')
    
    return secondInterval.overlaps(firstInterval)

  for row in range(len(specialCharDictList)):
    for charIndex in specialCharDictList[row]:
      for j in range(-1,2):
        if 0 <= row+j < len(specialNumDictList):
          for key, number in specialNumDictList[row+j].items():
            if checkOverlaping(charIndex, key, number):
              firstTaskResult += number
              
  return firstTaskResult
print(firstPuzzleSolution(lines))
#---------Second PUZZLE SOLUTION---------
import re, pandas as pd, numpy

def secondPuzzleSolution(lines):
  secondTaskResult = 0
  specialCharDictList = []
  specialNumDictList = []

  for i in range(len(lines)):
    #List of special characters
    specialCharsInRow = re.finditer(f"[*]", lines[i])
    charsDict = {}

    for specialChar in specialCharsInRow:
      if len(specialChar.group(0))> 0: 
        charsDict[int(specialChar.start())] = specialChar.group(0)
    
    specialCharDictList.append(charsDict)

    #List of numbers
    specialNumsInRow = re.finditer(f"\d+", lines[i])
    numDict = {}

    for specialNum in specialNumsInRow:
      if len(specialNum.group(0))> 0:
        numDict[int(specialNum.start())] = int(specialNum.group(0))

    specialNumDictList.append(numDict)

  def checkOverlaping(indexToCheck, indexOfNumber, number):
    firstInterval = pd.Interval(indexToCheck-1, indexToCheck+1, closed='both')
    secondInterval = pd.Interval(indexOfNumber, indexOfNumber + len(str(number)) - 1, closed='both')
    
    return secondInterval.overlaps(firstInterval)

  for row in range(len(specialCharDictList)):
    for charIndex in specialCharDictList[row]:
      numbersToMultiply = []
      for j in range(-1,2):
        if 0 <= row+j < len(specialNumDictList):
          for key, number in specialNumDictList[row+j].items():
            if checkOverlaping(charIndex, key, number):
              numbersToMultiply.append(number)

      if(len(numbersToMultiply)>1):
        secondTaskResult += numpy.prod(numbersToMultiply)
              
  return secondTaskResult
print(secondPuzzleSolution(lines))