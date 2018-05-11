prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
lengths = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

n = len(lengths)
def TopBottom(prices, n):
    arr = [-1000] * n
    arr[0] = 0
    maxProfit = MaxProfit(prices, n, arr)
    return maxProfit

def MaxProfit(prices, n, arr):
    if(n ==0):
        maxx = 0
    else:
        maxx = -1000
    for i in range(0, n):
        maxx = max(maxx, prices[i] + MaxProfit(prices, n-i-1, arr))
    arr[n-1] = maxx
    return arr[n-1]


print(TopBottom(prices, n))