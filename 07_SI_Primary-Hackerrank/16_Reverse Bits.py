# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-reverse-bits

no_of_test_cases = int(input())

while(no_of_test_cases > 0):
    size_n = int(input())
    num = 0
    for itr in range(32):
        num <<= 1
        num |= size_n & 1
        size_n >>= 1
    print(num)

    no_of_test_cases -= 1