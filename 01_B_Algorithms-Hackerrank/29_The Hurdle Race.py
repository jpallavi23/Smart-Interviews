# For question go to:
# https://www.hackerrank.com/challenges/the-hurdle-race/problem

no_of_heights, max_jump = map(int, input().split())
heights_range = list(map(int, input().split()))

count = 0
for itr in range(no_of_heights):
    if heights_range[itr] > count:
        count = heights_range[itr]

if count < max_jump:
    print(0)
else:
    print(count - max_jump)