lines = []
with open('AOC_4Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------First PUZZLE SOLUTION---------
def firstPuzzleSolution(lines):
  firstTaskResult = 0

  for line in lines:
    twoCardsList = map(str.strip(), line.split(': ')[1].split('|'))
    winningCardList, guessingCardList = [map(int, cardList.split()) for cardList in twoCardsList]

    numberOfWinningCards = len(list(set(winningCardList).intersection(guessingCardList)))
    if numberOfWinningCards > 0: firstTaskResult += 2**(numberOfWinningCards-1)
  
  return firstTaskResult

print(firstPuzzleSolution(lines))

#---------Second PUZZLE SOLUTION---------
def secondPuzzleSolution(lines):
  import re
  gameDict = {}
  gameWins = {}

  for line in lines:
    game, cards = line.split(': ')
    numberOfGame = int(re.search(r"\d+", game).group())
    gameDict[numberOfGame] = 1

    twoCardsList = map(str.strip(), cards.split('|'))
    winningCardList, guessingCardList = [map(int, cardList.split()) for cardList in twoCardsList]

    numberOfWinningCards = len(list(set(winningCardList).intersection(guessingCardList)))
    gameWins[numberOfGame] = numberOfWinningCards

  for i in range(1, len(gameDict.keys())):
    for j in range(1, gameWins[i]+1):
      gameDict[i+j] += gameDict[i]

  return sum(gameDict.values())

print(secondPuzzleSolution(lines))
