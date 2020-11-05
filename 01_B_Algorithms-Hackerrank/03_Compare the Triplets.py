# For question go to:
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for ind in range(0,3):
        if a[ind] > b[ind]:
            a_points += 1
        elif a[ind] < b[ind]:
            b_points += 1
        else:
            continue
    return (a_points,b_points)


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = compareTriplets(a, b)
    print("{} {}".format(result[0],result[1]))