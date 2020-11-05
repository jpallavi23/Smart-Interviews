# For question go to:
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

size, key = map(int, input().split())
array_of_size = list(map(int, input().split()))

itr = 0
count = 0
while itr < size:
    ctr = itr + 1
    while ctr < size:
        if itr < ctr and ((array_of_size[itr] + array_of_size[ctr]) % key == 0):
            count += 1
        ctr += 1
    itr += 1

print(count)