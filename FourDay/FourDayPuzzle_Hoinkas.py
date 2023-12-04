lines = []
with open('AOC_4Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------First PUZZLE SOLUTION---------
firstTaskResult = 0

for line in lines:
  twoCardsList = line.split(': ')[1].split('|')
  twoCardsList = [cardList.strip() for cardList in twoCardsList]
  
  winningCardList = list(map(int, filter(None, twoCardsList[0].split(' '))))
  guessingCardList = list(map(int, filter(None, twoCardsList[1].split(' '))))

  numberOfWinningCards = len(list(set(winningCardList).intersection(guessingCardList)))

  if numberOfWinningCards > 0:
    firstTaskResult += 2**(numberOfWinningCards-1)

print(firstTaskResult)

#---------Second PUZZLE SOLUTION---------
import re
gameDict = {}
gameWins = {}

for line in lines:
  gameAndCardList = line.split(': ')
  numberOfGame = int(re.findall(f"\d+", gameAndCardList[0])[0])
  twoCardsList = [cardList.strip() for cardList in gameAndCardList[1].split('|')]
  gameDict[numberOfGame] = 1
  
  winningCardList = list(map(int, filter(None, twoCardsList[0].split(' '))))
  guessingCardList = list(map(int, filter(None, twoCardsList[1].split(' '))))

  numberOfWinningCards = len(list(set(winningCardList).intersection(guessingCardList)))
  gameWins[numberOfGame] = numberOfWinningCards

for i in range(1, len(gameDict.keys())):
  for j in range(1, gameWins[i]+1):
    gameDict[i+j] += gameDict[i]

secondTaskResult = sum(gameDict.values())
print(secondTaskResult)