
def maxProfit(priceList):
    if not priceList:
        return 0
    profitList = len(priceList) * [0]
    for i in range(len(priceList)):
        if i > 0 and priceList[i] > priceList[i-1]:
            maxProfit = 0
            for j in range(i):
                diffPrice = priceList[i] - priceList[j]
                if diffPrice > maxProfit:
                    maxProfit = diffPrice
                else:
                    continue
            profitList[i] = maxProfit
    return max(profitList)

if __name__ == '__main__':
    print(maxProfit([]))