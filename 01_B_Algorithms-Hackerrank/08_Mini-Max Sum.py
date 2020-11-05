# For question go to:
# https://www.hackerrank.com/challenges/mini-max-sum/problem

arr = sorted(list(map(int, input().split())))
arr_sum = sum(arr)
minValue = arr_sum - max(arr)
maxValue = arr_sum - min(arr)

print(minValue, maxValue)