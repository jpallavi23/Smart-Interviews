# For question go to:
# https://www.hackerrank.com/challenges/plus-minus/problem

n = int(input())
arr = list(map(int, input().split()))
positive_count = negative_count = zero_count = 0

for i in arr:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1
    elif i == 0:
        zero_count += 1

print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(positive_count/n, negative_count/n, zero_count/n))