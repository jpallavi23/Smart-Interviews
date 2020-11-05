# For question go to:
# https://www.hackerrank.com/challenges/kangaroo/problem

x1, v1, x2, v2 = list(map(int, input().split()))

if x1 + v1 == x2 + v2:
    print("YES")
    exit(0)
if v1 > v2 and x1 < x2:
    while (x2 - x1) % (v2 - v1) == 0:
        print("YES")
        break
    else:
        print("NO")
else:
    print("NO")