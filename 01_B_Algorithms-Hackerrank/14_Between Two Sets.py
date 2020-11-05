# For question go to:
# https://www.hackerrank.com/challenges/between-two-sets/problem

n, m = list(map(int, input().split()))
n_a = list(map(int, input().split()))
m_b = list(map(int, input().split()))

countInt = 0
iter = 1

while iter <= 100:
    if all(iter % num1 == 0 for num1 in n_a):
        if all(num2 % iter == 0 for num2 in m_b):
            countInt += 1
    iter += 1

print(countInt)