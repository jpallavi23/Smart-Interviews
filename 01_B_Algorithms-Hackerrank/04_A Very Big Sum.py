# For question go to:
# https://www.hackerrank.com/challenges/a-very-big-sum/problem

def aVeryBigSum(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().split()))

    result = aVeryBigSum(ar)
    print("{}".format(result))