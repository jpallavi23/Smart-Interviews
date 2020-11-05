# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-print-right-angled-triangle-pattern

no_of_test_cases = int(input())
iter = 1

while iter <= no_of_test_cases:
    size = int(input())
    i = j = 1
    count = 2 * size - 2
    print("Case #{}:".format(iter))
    while i < size+1:
        for j in range(i, size):
            print(end=" ")
        count = count - 2
        for j in range(1, i + 1):
            print("*", end="")
        i += 1
        print("")
    iter += 1