# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-compute-a-power-b

no_of_test_cases = int(input())

M = 1e9 + 7
while(no_of_test_cases > 0):
    a, b = map(int, input().split())
    power = 1
    itr = a
    while(b != 0):
        if((b & 1) == 1):
            power = (power * itr) % M
        itr = (itr * itr) % M
        b >>= 1
    print(int(power))

    no_of_test_cases -= 1