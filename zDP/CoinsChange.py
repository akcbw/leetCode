"""

coinsChange(coinsList, change) = min{1+ coinsChange(coinsList, change-coin)} (coin in coinsList)

"""

def coinsChange(coinsList, change):
    if change in coinsList:
        return 1
    else:
        maxValue = change
        for coin in coinsList:
            if change >= coin:
                amount = coinsChange(coinsList, change - coin)
                if amount <= maxValue:
                    maxValue = amount
        return 1 + maxValue


def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins


def coinsChangeWithMemory(coinsList, change, changeMap):
    if change in coinsList:
        changeMap[change] = 1
        return 1
    else:
        if change in changeMap :
            amount = changeMap[change]
            return amount
        else:
            maxValue = change
            for coin in coinsList:
                if change >= coin:
                    amount = coinsChangeWithMemory(coinsList, change - coin,changeMap)
                    if amount <= maxValue:
                        maxValue = amount
            changeMap[change] = 1 + maxValue
            return 1 + maxValue

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

def coinChangeDP(coinsList, change, dpTable):
    for i in range(change):
        if i + 1 in coinsList:
            dpTable.append(1)
        else:
            minValue = change
            for coin in [c for c in coinsList if c <= i]:
                amount = 1 + dpTable[i - coin]
                if amount < minValue:
                    minValue = amount
            dpTable.append(minValue)
    return dpTable[change - 1]


if __name__ == '__main__':
    #print(recMC([1, 5, 10, 25], 63))
    #print(coinsChange([1,5,10,25], 63))
    print(recDC([1,5,10,25],63,[0]*64))
    print(coinsChangeWithMemory([1, 5, 10, 25], 63, {}))
    print(recDC([1, 5, 10, 21,25], 63, [0] * 64))
    print(coinsChangeWithMemory([1, 5, 10, 21,25], 63, {}))
    print(coinChangeDP([1, 5, 10, 21, 25], 63, []))