# For question go to:
# https://www.hackerrank.com/challenges/picking-numbers/problem

array_size = int(input())
array_elements = list(map(int, input().split()))

count_picks = []
for itr in array_elements:
    count_picks.append(array_elements.count(itr) + array_elements.count(itr + 1))

print(max(count_picks))