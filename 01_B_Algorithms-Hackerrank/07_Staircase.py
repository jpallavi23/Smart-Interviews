# For question go to:
# https://www.hackerrank.com/challenges/staircase/problem

size = int(input())
i = j = 1
count = 2 * size - 2
while i < size+1:
    for j in range(i, size):
        print(end=" ")
    count = count - 2
    for j in range(1, i + 1):
        print("#", end="")
    i += 1
    print("")