"""

coinsChange(coinsList, change) = min{1+ coinsChange(coinsList, change-coin)} (coin in coinsList)

"""


def coinsChange(coinsList, change):
    if change in coinsList:
        return 1
    else:
        minvalue = 1
        for coin in coinsList:
            if change >= coin:
                amount = coinsChange(coinsList, change - coin)
                if amount <= minvalue:
                    minvalue = amount
            else:
                break
    return 1 + minvalue


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



if __name__ == '__main__':
    print(recMC([1, 5, 10, 25], 37))
    print(coinsChange([1,5,10,25], 37))