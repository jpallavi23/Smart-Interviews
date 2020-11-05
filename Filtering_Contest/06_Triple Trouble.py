# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-triple-trouble

def find(array, size):
    itr = 0
    check = {}
    while itr < size:
        if array[itr] in check:
            check[array[itr]] += 1
        else:
            check[array[itr]] = 1
        itr += 1

    for k, v in check.items():
        if v == 1:
            print(k)
            break
        

no_of_test_cases = int(input())
iter = 1
while iter <= no_of_test_cases:
    size = int(input())
    array = list(map(int, input().split()))
    find(array, size)
    iter += 1