#Importing file with input
lines = []
with open('AOC_1Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
#Importing re for faster finding specific words/digits in lines
import re

firstTaskResult = 0

for line in lines:
  numbersInLine = [int(match) for match in re.findall(r"\d", line)]
  numbersToAdd = int(''.join([str(numbersInLine[0]),str(numbersInLine[-1])]))
  firstTaskResult += numbersToAdd

print(firstTaskResult)

#---------SECOND PUZZLE SOLUTION---------
#Dictionary for every number name with corresponding numbers
translator = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def replaceWordsWithNumbers(textLine):
  for word, initial in translator.items():
    textLine = textLine.replace(word, initial)
  return textLine

secondTaskResult = 0

for line in lines:
  results = re.findall(f"(?=(\d|{'|'.join(translator.keys())}))", line)
  translatedList = [item if item.isdigit() else replaceWordsWithNumbers(item) for item in results]
  numbersToAdd = int(''.join([str(translatedList[0]),str(translatedList[-1])]))
  secondTaskResult += numbersToAdd

print(secondTaskResult)
