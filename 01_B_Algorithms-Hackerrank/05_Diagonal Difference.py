# For question go to:
# https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input())
i = diag_diff = 0

while i < n:
    arr = input().split()
    diag_diff += int(arr[i])-int(arr[-(i+1)])
    i += 1

print(abs(diag_diff))