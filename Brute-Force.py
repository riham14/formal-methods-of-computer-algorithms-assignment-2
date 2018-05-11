from datetime import datetime

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
lengths = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
dataSizes = [10, 20, 30, 40, 50]
n = len(dataSizes)
print(n)
def rodCutting(prices, n):
    maxPrice = 0
    for i in range(0, n):
        #print(i)
        price = prices[i] + rodCutting(prices, n-i-1)
        #print(price)
        maxPrice = max(maxPrice, price)

    #print("maxPrice", maxPrice)
    return maxPrice

def AnalyzeAlgorithm(prices, dataSizes):
    for i in range(0, 5):
        print(i)
        time1 = datetime.now()
        #print(len(prices*dataSizes[i]))
        rodCutting(prices*dataSizes[i], dataSizes[i])
        time2 = datetime.now()
        print(time2-time1)

AnalyzeAlgorithm(prices, dataSizes)
