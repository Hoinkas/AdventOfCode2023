#Importing file with input
lines = []
with open('AOC_1Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
#Importing re for faster finding specific words/digits in lines
import re

def firstPuzzleSolution(lines):
  firstTaskResult = 0

  for line in lines:
    numbersInLine = [int(match) for match in re.findall(r"\d", line)]
    numbersToAdd = numbersInLine[0] * 10 + numbersInLine[-1]
    firstTaskResult += numbersToAdd

  return firstTaskResult
print(firstPuzzleSolution(lines))

  #---------SECOND PUZZLE SOLUTION---------
def secondPuzzleSolution(lines):
  translator = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

  secondTaskResult = 0

  for line in lines:
    results = re.findall(r"(?=(\d|{'|'.join(translator.keys())}))", line)
    translatedList = [int(item) if item.isdigit() else translator[item] for item in results]
    numbersToAdd = translatedList[0] * 10 + translatedList[-1]
    secondTaskResult += numbersToAdd
  
  return secondTaskResult
print(secondPuzzleSolution(lines))

##Kudos to naalty post in reddit for showing code with re usage which I implemented in 26 line in my file - https://www.reddit.com/r/adventofcode/comments/1883ibu/comment/kbiu5bo/?utm_source=reddit&utm_medium=web2x&context=3
##Kudos to girafon for advice of returning two parsed digits in line 15, 28 and how to simplyfy switching key-value function to simple dict[key] one in line 27 - https://www.reddit.com/r/adventofcode/comments/1883ibu/comment/kbj1tqf/
