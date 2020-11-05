# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-finding-frequency

size = int(input())
array = list(map(int, input().split()))

no_of_test_cases = int(input())
itr = 0
check = {}
while itr < size:
    if array[itr] in check:
        check[array[itr]] += 1
    else:
        check[array[itr]] = 1
    itr += 1

itr = 0
while itr < no_of_test_cases:
    num = int(input())
    if num in check:
        print(check[num])
    else:
        print(0)
    itr += 1