lines = []
with open('AOC_7Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]
  
#---------GLOBAL VARIABLES---------
listOfHands = []

for line in lines:
  (hand, bid) = line.split()
  listOfHands.append([hand, int(bid)])

#---------FIRST PUZZLE SOLUTION---------
def firstTaskFunction():
  import functools

  cardList = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
  cardList.reverse()

  def sortingFunct(currentHand, nextHand):
    currentCount, nextCount = [max(map(hand.count, hand))- len(set(hand)) for hand in [currentHand[0], nextHand[0]]]

    if currentCount == nextCount:
      for j in range(5):
        currentCardValue, nextCardValue = [cardList.index(hand[j]) for hand in [currentHand[0], nextHand[0]]]
        
        if (currentCardValue == nextCardValue): continue
        else: return 1 if currentCardValue > nextCardValue else -1
    else:
      return 1 if currentCount > nextCount else -1

  sortedHands = sorted(listOfHands, key=functools.cmp_to_key(sortingFunct))

  firstTaskResult = 0

  for i in range(len(sortedHands)):
    firstTaskResult += (i+1) * sortedHands[i][1]

  return firstTaskResult
    
print(firstTaskFunction())

#---------SECOND PUZZLE SOLUTION---------
def secondTaskFunction():
  import functools
  
  cardList = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
  cardList.reverse()

  def sortingFunct(currentHand, nextHand):
    pseudoCurrentHand = 'AAAAA' if currentHand[0] == 'JJJJJ' else currentHand[0].replace('J', '')
    pseudoNextHand = 'AAAAA' if nextHand[0] == 'JJJJJ' else nextHand[0].replace('J', '')
    currentCount, nextCount = [max(map(hand.count, hand)) - len(set(hand)) for hand in [pseudoCurrentHand, pseudoNextHand]]

    if not currentHand[0] == 'JJJJJ' and 'J' in currentHand[0]:
      howManyJ = currentHand[0].count('J')
      currentCount += howManyJ

    if not nextHand[0] == 'JJJJJ' and 'J' in nextHand[0]:
      howManyJ = nextHand[0].count('J')
      nextCount += howManyJ

    if currentCount == nextCount:
      for j in range(5):
        currentCardValue, nextCardValue = [cardList.index(hand[j]) for hand in [currentHand[0], nextHand[0]]]

        if (currentCardValue == nextCardValue): continue
        else: return 1 if currentCardValue > nextCardValue else -1
    else:
      return 1 if currentCount > nextCount else -1

  sortedHands = sorted(listOfHands, key=functools.cmp_to_key(sortingFunct))

  secondTaskResult = 0

  for i in range(len(sortedHands)):
    secondTaskResult += (i+1) * sortedHands[i][1]
    
  return secondTaskResult

print(secondTaskFunction())