lines = []
with open('AOC_11_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]
  
#---------FIRST PUZZLE SOLUTION---------
def firstTaskResult(lines):
  import re

  oldGalaxies = []
  mapOfSky = []

  for i, line in enumerate(lines):
    mapOfSky.append(list(line))

    foundGalaxies = re.finditer(r'#', line)
    [oldGalaxies.append((i, galaxy.start())) for galaxy in foundGalaxies]

  galaxies = oldGalaxies.copy()
  valueToExpand = 1

  addValue = 0
  for i in range(len(mapOfSky)):
    if all(galaxyY != i for galaxyY, _ in oldGalaxies):
      galaxiesToRelocate = [galaxy for galaxy in galaxies if galaxy[0] >= i+addValue]
      
      for galaxy in galaxiesToRelocate:
        galaxies.remove(galaxy)
        galaxies.append((galaxy[0] + valueToExpand, galaxy[1]))
    
      addValue += 1

  addValue = 0
  for j in range(len(mapOfSky[0])):
    if all(galaxyX != j for _, galaxyX in oldGalaxies):
      galaxiesToRelocate = [galaxy for galaxy in galaxies if galaxy[1] >= j+addValue]
      
      for galaxy in galaxiesToRelocate:
        galaxies.remove(galaxy)
        galaxies.append((galaxy[0], galaxy[1] + valueToExpand))

      addValue += 1

  distance = 0
  pairSet = set()

  for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies):
      if (g1,g2) not in pairSet and (g2,g1) not in pairSet and i != j:
        #Manhattan distance |a1-b1| + |a2-b2|
        distance += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
        pairSet.add((g1,g2))

  return distance

print(firstTaskResult(lines))

