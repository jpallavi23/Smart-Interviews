# For question go to:
# https://www.hackerrank.com/challenges/migratory-birds/problem

size = int(input())
array = sorted(list(map(int, input().split())))

count = {}
for itr in array:
    if itr in count:
        count[itr] += 1
    else:
        count[itr] = 1

print(max(count, key = count.get))