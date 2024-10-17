lines = []
with open('AOC_5Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
# stringsOfMatches = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]
# indexesOfMatches = [lines.index(pharse) for pharse in stringsOfMatches]

# # seedsList = map(int, lines[0].split(': ')[1].split())
# seedsList = [70]
# seedToSoilList = lines[seedToSoilIndex+1:soilToFertilizerIndex-1]
# soilToFertilizerList = lines[soilToFertilizerIndex+1:fertilizerToWaterIndex-1]
# fertilizerToWaterList = lines[fertilizerToWaterIndex+1:waterToLightIndex-1]
# waterToLightList = lines[waterToLightIndex+1:lightToTempratureIndex-1]
# lightToTempratureList = lines[lightToTempratureIndex+1:temperatureToHumidityIndex-1]
# temperatureToHumidityList = lines[temperatureToHumidityIndex+1:humidityToLocationIndex-1]
# humidityToLocationList = lines[humidityToLocationIndex+1:]

# def looper(listToCheck, number):
#   for xToY in listToCheck:
#     destination, source, rg = map(int, xToY.split())

#     if source <= number <= source+rg:
#       return destination + number-source
  
#   return number

# seedToSoilResult = [looper(seedToSoilList, seed) for seed in seedsList]
# soilToFertilizerResult = [looper(soilToFertilizerList, seed) for seed in seedToSoilResult]
# fertilizerToWaterResult = [looper(fertilizerToWaterList, seed) for seed in soilToFertilizerResult]
# waterToLightResult = [looper(waterToLightList, seed) for seed in fertilizerToWaterResult]
# lightToTempratureResult = [looper(lightToTempratureList, seed) for seed in waterToLightResult]
# temperatureToHumidityResult = [looper(temperatureToHumidityList, seed) for seed in lightToTempratureResult]
# humidityToLocationResult = [looper(humidityToLocationList, seed) for seed in temperatureToHumidityResult]

# secondTaskResult = min(humidityToLocationResult)
# print(secondTaskResult)

#---------SECOND PUZZLE SOLUTION---------
import re

stringsOfMatches = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]
indexesOfMatches = [lines.index(pharse) for pharse in stringsOfMatches]

# lines[index +1: indexesOfMatches[i+1]-1] for i, index in enumerate(indexesOfMatches)

matchesDict = {}
lengthOfMatches = len(indexesOfMatches)

for i in range(lengthOfMatches-1):
  startIndex = indexesOfMatches[i]+1
  endIndex = indexesOfMatches[i+1]-1 if i < lengthOfMatches else lengthOfMatches-1

  matchesDict[i] = [list(map(int, line.split())) for line in lines[startIndex:endIndex]]

def returnResultOfMatching(seedNumber):
  currentResult = seedNumber

  for matchRule in matchesDict.values():
    for xToY in matchRule:
      destination, source, rg = xToY

      if source <= currentResult <= source+rg:
        currentResult = destination + currentResult-source
        break

  return currentResult

seedsRangeList = lines[0].split(': ')[1]
seedsList = [(start, start+end) for start, end in map(lambda x: map(int, x.split()), re.findall(r"(\d+ \d+)", seedsRangeList))]
seedsList = sorted(seedsList)

minSeed, maxSeed = [min(seedsList[0]), max(seedsList[1])]
minValue = maxSeed

seedNumber = minSeed
whichRange = 0

while seedNumber < maxSeed:
  resultOfMatching = returnResultOfMatching(seedNumber)

  if(minValue > resultOfMatching):
    minValue = resultOfMatching
  
    print(f"{seedNumber-minSeed}/{maxSeed-minSeed} {round((seedNumber-minSeed)/(maxSeed-minSeed)*100,2)}%")
  
  if(whichRange+1 < len(seedsList) and (seedNumber == seedsList[whichRange][1] or (seedNumber >= seedsList[whichRange+1][0]))):
    seedNumber = seedsList[whichRange+1][0]
    whichRange += 1
  else: seedNumber += 1

print('WON----------------------')
print(minValue)