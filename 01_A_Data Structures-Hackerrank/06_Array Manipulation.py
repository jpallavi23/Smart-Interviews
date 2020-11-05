# For question go to:
# https://www.hackerrank.com/challenges/crush/problem

from collections import Counter

size_of_array, no_of_operations = map(int,input().split())
array_elements = [list(map(int,input().split())) for _ in range(no_of_operations)]

count = Counter()
for a,b,k in array_elements:
    count[a] += k
    count[b + 1] -= k

arraySum = 0
maxArraySum = 0
for itr in sorted(count)[:-1]:
    arraySum += count[itr]
    maxArraySum = max(maxArraySum, arraySum)

print(maxArraySum)