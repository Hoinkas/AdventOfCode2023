lines = []
with open('AOC_11_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]
  
#---------PUZZLE SOLUTION---------
def relocateGalaxies(galaxies, axis, mapOfSky, valueToExpand, oldGalaxies):
  valueToExpand = valueToExpand - 1 if valueToExpand != 1 else valueToExpand
  addValue = 0
  lenghtToCheck = len(mapOfSky) if axis == 0 else len(mapOfSky[0])

  for i in range(1, lenghtToCheck-1):
    if all(galaxy[axis] != i for galaxy in oldGalaxies):
      galaxiesToRelocate = [galaxy for galaxy in galaxies if galaxy[axis] > i+addValue]
      
      for galaxy in galaxiesToRelocate:
        galaxies.remove(galaxy)

        expandInYAxis = valueToExpand if axis == 0 else 0
        expandInXAxis = valueToExpand if axis == 1 else 0
        galaxies.append((galaxy[0] + expandInYAxis, galaxy[1] + expandInXAxis))

      addValue += valueToExpand
    
  return galaxies

def taskResult(lines, valueToExpand):
  import re

  oldGalaxies = []
  mapOfSky = []

  for i, line in enumerate(lines):
    mapOfSky.append(list(line))

    foundGalaxies = re.finditer(r'#', line)
    [oldGalaxies.append((i, galaxy.start())) for galaxy in foundGalaxies]

  galaxies = oldGalaxies.copy()

  galaxies = relocateGalaxies(galaxies, 0, mapOfSky, valueToExpand, oldGalaxies)
  galaxies = relocateGalaxies(galaxies, 1, mapOfSky, valueToExpand, oldGalaxies)

  distance = 0

  for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
      #Manhattan distance |a1-b1| + |a2-b2|
      distance += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

  return distance

print(taskResult(lines, 1))
print(taskResult(lines, 1000000))