# For question go to:
# https://www.hackerrank.com/challenges/arrays-ds/problem

array_size = int(input())
array_elements = list(map(int, input().split()))

print(*array_elements[::-1])