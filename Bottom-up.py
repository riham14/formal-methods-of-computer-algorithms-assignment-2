from datetime import datetime

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
lengths = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

dataSizes = [10, 100, 1000, 10000, 100000]
times = [0] * len(dataSizes)

n = len(lengths)
def BottomUp(prices, n):
    arr = [0] * (n+1)
    arr[0] = 0
    for i in range(1, n+1):
        maxx = -1000
        for j in range(i):
            maxx = max(maxx, prices[j] + arr[i-j-1])
        arr[i] = maxx
    return arr[n]


#print(BottomUp(prices, n))

def AnalyzeAlgorithm(prices, dataSizes):
    for i in range(0, 5):
        print(i)
        time1 = datetime.now()
        #print(len(prices*dataSizes[i]))
        BottomUp(prices*dataSizes[i], dataSizes[i])
        time2 = datetime.now()
        times[i] = time2-time1
        print(time2-time1)

AnalyzeAlgorithm(prices, dataSizes)
print("Data Sizes: ", dataSizes)
print("Times: ", times)
