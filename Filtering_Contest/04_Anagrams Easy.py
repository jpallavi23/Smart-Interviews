# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-check-anagrams

no_of_test_cases = int(input())
iter = 1
while iter <= no_of_test_cases:
    string1, string2 = list(map(str, input().split()))
    if sorted(string1) == sorted(string2):
        print("True")
    else:
        print("False")
    iter += 1