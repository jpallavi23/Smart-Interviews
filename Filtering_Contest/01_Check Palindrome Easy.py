# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-check-palindrome

def check(string):
    if string == string[::-1]:
        print("Yes")
    else:
        print("No")

no_of_test_cases = int(input())
iter = 1
while iter <= no_of_test_cases:
    size = int(input())
    string = input()
    check(string)
    iter += 1