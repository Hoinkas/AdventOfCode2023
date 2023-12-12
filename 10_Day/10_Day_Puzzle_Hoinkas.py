matrix = []
with open('AOC_10_Day_Quest.txt') as f:
  l = f.readlines()
  matrix = [entry.strip() for entry in l]

#---------FUNCTIONS---------
def returnPoints(matrix, pipesDict, neighborsPoints):
  import re

  startingPosition = next(((i, match.start()) for i, row in enumerate(matrix) if (match := re.search(r"S", row))), (0, 0))

  points = []
  sY = startingPosition[0]
  sX = startingPosition[1]

  for point in neighborsPoints:
    i, j = point

    if(0 <= sY+i < len(matrix) and 0 <= sX+j < len(matrix[0]) and matrix[sY+i][sX+j] != '.'):
      currentSymbol = matrix[sY+i][sX+j]
      pipesNextY, pipesNextX = [pipesDict[currentSymbol][i][iterat+1] for i, iterat in enumerate(point)]

      if(pipesNextY != '' and pipesNextX != ''): points.append((sY+i,sX+j))
  
  return points, sY, sX

#---------DEFAULT VARIABLES---------
#Rules for each type of pipe telling where the next pipe is
pipesDict = {
  '-': [['',0,''],[2,'',-2]],
  '|': [[2,'',-2],['',0,'']],
  '7': [['',1,-1],[1,-1,'']],
  'J': [[1,-1,''],[1,-1,'']],
  'L': [[1,-1,''],['',1,-1]],
  'F': [['',1,-1],['',1,-1]]
}

#Get all pipes connected to starting point
neighborsPoints = [[-1,0],[0,-1],[0,1],[1,0]]

#---------FIRST PUZZLE SOLUTION---------
def firstTaskSolution(matrix):
  points, sY, sX = returnPoints(matrix, pipesDict, neighborsPoints)

  furthestPoint = 1
  previousPoints = [(sY,sX), (sY,sX)]

  while points[0] != points[1]:
    furthestPoint += 1

    for i, route in enumerate(points):
      pointsDifference = (previousPoints[i][0] - route[0], previousPoints[i][1] - route[1])
      
      currentSymbol = matrix[route[0]][route[1]]
      pipeCalc = pipesDict[currentSymbol]
      prevPoint = previousPoints[i]

      pipesNextY, pipesNextX = [pipeCalc[i][diff+1] for i, diff in enumerate(pointsDifference)]
      nextCoordY, nextCoordX = (prevPoint[0] + pipesNextY, prevPoint[1] + pipesNextX)

      points[i] = (nextCoordY, nextCoordX)

      previousPoints[i] = route

  return furthestPoint

print(firstTaskSolution(matrix))

def secondTaskSolution(matrix):
  points, sY, sX = returnPoints(matrix, pipesDict, neighborsPoints)
  
  points = [(sY, sX), points[0]]

  while True:
    pointsDifference = (points[-2][0] - points[-1][0], points[-2][1] - points[-1][1])
    
    currentSymbol = matrix[points[-1][0]][points[-1][1]]
    pipeCalc = pipesDict[currentSymbol]

    pipesNextY, pipesNextX = [pipeCalc[i][diff+1] for i, diff in enumerate(pointsDifference)]
    
    nextCoordY, nextCoordX = (points[-2][0] + pipesNextY, points[-2][1] + pipesNextX)
    newPoint = (nextCoordY, nextCoordX)

    if(newPoint == (sY,sX)): break
    points.append(newPoint)
  
  # Shoelace formula
  # A = 1/2 * sum(xi * yi+1 - yi * xi+1)

  # Pick's theorem
  # A = i + points/2 - 1    i - interior points
  # i = A - points/2 + 1

  sumOfPoints = 0
  howManyPoints = len(points)

  for i in range(howManyPoints):
    nextIndex = (i+1) % howManyPoints
    sumOfPoints += points[i][1] * points[nextIndex][0] - points[i][0] * points[nextIndex][1]

  result = round((sumOfPoints/2) - howManyPoints/2 + 1)

  return result

print(secondTaskSolution(matrix))