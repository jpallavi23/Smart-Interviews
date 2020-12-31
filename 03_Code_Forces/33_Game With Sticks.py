# https://codeforces.com/problemset/problem/451/A

n, m = map(int, input().split())
n = min(n, m)
if(n % 2 == 0):
    print("Malvika")
else:
    print("Akshat")