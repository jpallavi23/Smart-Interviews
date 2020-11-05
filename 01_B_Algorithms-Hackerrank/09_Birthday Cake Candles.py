# For question go to:
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

no_of_candles = int(input())
candles = sorted(list(map(int, input().split())))
tallCandle = max(candles)
countTallCandles = 0
for i in candles:
    if i == tallCandle:
        countTallCandles += 1
print(countTallCandles)