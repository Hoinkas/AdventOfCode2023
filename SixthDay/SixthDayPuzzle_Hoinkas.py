lines = []
with open('AOC_6Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
import re, numpy

numbersList = [re.findall(r"(\d+)", line) for line in lines]
timesList = list(map(int, [time for time in numbersList[0]]))
recordList = list(map(int, [time for time in numbersList[1]]))

racesWinsList = []

for raceNumber in range(len(timesList)):
  winsCount = 0
  for pressTime in range(timesList[raceNumber]):
    timeLeft = timesList[raceNumber] - pressTime
    reachedDistance = timeLeft * pressTime

    if reachedDistance > recordList[raceNumber]: winsCount += 1

  racesWinsList.append(winsCount)

firstTaskResult = numpy.prod(racesWinsList)

print (firstTaskResult)

#---------SECOND PUZZLE SOLUTION---------
import re

numbersList = [re.findall(r"(\d+)", line) for line in lines]
timeOfRace = int(''.join([time for time in numbersList[0]]).replace(" ", ""))
recordOfRace = int(''.join([time for time in numbersList[1]]).replace(" ", ""))

secondTaskResult = 0

for pressTime in range(timeOfRace):
  timeLeft = timeOfRace - pressTime
  reachedDistance = timeLeft * pressTime

  if reachedDistance > recordOfRace: secondTaskResult += 1

print (secondTaskResult)