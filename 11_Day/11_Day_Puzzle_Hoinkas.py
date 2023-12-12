lines = []
with open('AOC_11_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]
  
#---------FIRST PUZZLE SOLUTION---------
def firstTaskResult(lines):
  import re, numpy as np

  galaxiesBefore = []
  mapOfSky = []

  for i, line in enumerate(lines):
    mapOfSky.append(list(line))

    foundGalaxies = re.finditer(r'#', line)
    [galaxiesBefore.append((i, galaxy.start())) for galaxy in foundGalaxies]

  addValue = 0
  for i in range(len(mapOfSky)):
    if all(galaxyX != i for galaxyX, _ in galaxiesBefore):
      mapOfSky = np.insert(mapOfSky,i+addValue,'.',axis=0)
      addValue += 1

  addValue = 0
  for j in range(len(mapOfSky[0])):
    if all(galaxyY != j for _, galaxyY in galaxiesBefore):
      mapOfSky = np.insert(mapOfSky,j+addValue,'.',axis=1)
      addValue += 1

  # [print(sky) for sky in mapOfSky]

  galaxies = []

  for i, row in enumerate(mapOfSky):
    foundGalaxies = re.finditer(r'#', ''.join(row))

    for galaxy in foundGalaxies:
      if galaxy: galaxies.append((i, galaxy.start()))

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
