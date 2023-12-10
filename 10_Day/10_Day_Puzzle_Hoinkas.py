lines = []
with open('AOC_10_Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
import re

startingPosition = (0,0)
matrix = lines

for i, row in enumerate(matrix):
  match = re.search(r"S", row)

  if match:
    startingPosition = (i, match.start())

#Rules for each type of pipe telling where the next pipe is
pipesDict = {
  '-': [['',0,''],[2,'',-2]],
  '|': [[2,'',-2],['',0,'']],
  '7': [['',1,-1],[1,-1,'']],
  'J': [[1,-1,''],[1,-1,'']],
  'L': [[1,-1,''],['',1,-1]],
  'F': [['',1,-1],['',1,-1]]
}

routes = []
sY = startingPosition[0]
sX = startingPosition[1]

#Get all pipes connected to starting point
neighborsPoints = [[-1,0],[0,-1],[0,1],[1,0]]

for point in neighborsPoints:
  i, j = point

  if(0 <= sY+i < len(matrix) and 0 <= sX+j < len(matrix[0]) and matrix[sY+i][sX+j] != '.'):
    currentSymbol = matrix[sY+i][sX+j]
    pipesNextY = pipesDict[currentSymbol][0][i+1]
    pipesNextX = pipesDict[currentSymbol][1][j+1]

    if(pipesNextY != '' and pipesNextX != ''): routes.append((sY+i,sX+j))

furthestPoint = 1
previousPoints = [(sY,sX), (sY,sX)]

while routes[0] != routes[1]:
  furthestPoint += 1

  for i, route in enumerate(routes):
    pointsDifference = (previousPoints[i][0] - route[0], previousPoints[i][1] - route[1])
    currentSymbol = matrix[route[0]][route[1]]

    pipesNextY = pipesDict[currentSymbol][0][pointsDifference[0]+1]
    pipesNextX = pipesDict[currentSymbol][1][pointsDifference[1]+1]

    nextCoordY = previousPoints[i][0] + pipesNextY
    nextCoordX = previousPoints[i][1] + pipesNextX

    routes[i] = (nextCoordY, nextCoordX)
    previousPoints[i] = route

print(furthestPoint)