# For question to go
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-print-hollow-diamond-pattern

no_of_test_cases = int(input())
iter = 1

while iter <= no_of_test_cases:
    size_n = int(input())
    count = size_n - 1
    count = count / 2
    print("Case #{}:".format(iter))
    for itr in range(size_n):
        for jtr in range(size_n):
            if itr + jtr == count or jtr - itr == count or itr - jtr == count or itr + jtr == (count*3):
                print("*", end = "")
            else:
                print(end = " ")
        print()
    iter += 1