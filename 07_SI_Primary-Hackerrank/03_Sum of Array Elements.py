# For question go to:
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-array-elements

def simpleArraySum(ar):
    sum = 0
    for obj in ar:
        sum += obj
    return sum

if __name__ == '__main__':
    no_of_test_cases = int(input())
    iter = 1

    while iter <= no_of_test_cases:
        ar_count = int(input())
        ar = list(map(int, input().split()))
        result = simpleArraySum(ar)
        print(result)
        iter += 1