# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-sum-of-pairs

no_of_test_cases = int(input())
iter = 1

while iter <= no_of_test_cases:
    size, key = map(int, input().split())
    array = list(map(int, input().split()))
    temp = 0
    for itr in range(0, size):
        for jtr in range(0, size):
            if itr != jtr and array[itr] + array[jtr] == key:
                print("True")
                temp = 1
                break
        if temp == 1:
            break
    else:
        print("False")
    iter += 1