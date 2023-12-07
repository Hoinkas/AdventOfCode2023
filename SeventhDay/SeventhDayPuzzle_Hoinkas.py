lines = []
with open('AOC_7Day_Quest.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

#---------FIRST PUZZLE SOLUTION---------
def firstTaskFunction():
  from collections import Counter
  import functools

  cardList = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
  listOfHands = []

  for line in lines:
    (hand, bid) = line.split()
    listOfHands.append((hand, int(bid)))

  def sortingFunct(currentCard, nextCard):
    occCurrent = Counter(currentCard[0])
    occNext = Counter(nextCard[0])

    currentVaues = sorted(list(occCurrent.values()), reverse=True)
    nextValues = sorted(list(occNext.values()), reverse=True)

    smallerListLeng = min([len(currentVaues), len(nextValues)])

    for i in range(smallerListLeng):
      if (currentVaues[i] == nextValues[i]):
        if(i == smallerListLeng-1): break
        else: continue
      else: return 1 if currentVaues[i] > nextValues[i] else -1

    for j in range(5):
      currentIndex = cardList.index(currentCard[0][j])
      nextIndex = cardList.index(nextCard[0][j])
      
      if (currentIndex == nextIndex): continue
      else: return 1 if currentIndex < nextIndex else -1

  sortedHands = sorted(listOfHands, key=functools.cmp_to_key(sortingFunct))
  print(sortedHands)

  firstTaskResult = 0

  for i in range(len(sortedHands)):
    firstTaskResult += (i+1) * sortedHands[i][1]

  return firstTaskResult
    
print(firstTaskFunction())

#---------SECOND PUZZLE SOLUTION---------

# print (secondTaskResult)