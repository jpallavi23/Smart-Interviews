# For question go to:
# https://www.hackerrank.com/challenges/utopian-tree/problem

no_of_test_cases = int(input())

for itr in range(no_of_test_cases):
    no_of_cycles = int(input())
    if no_of_cycles == 0:
        print(1)
    elif no_of_cycles % 2 == 0:
        print(int(2 ** ((no_of_cycles / 2) + 1) - 1))
    else:
        print(int(2 ** ((no_of_cycles + 3) / 2) - 2))