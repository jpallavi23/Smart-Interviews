# For question go to:
# https://www.hackerrank.com/challenges/apple-and-orange/problem

s, t = list(map(int, input().split()))
a, b = list(map(int, input().split()))
m, n = list(map(int, input().split()))
m_a = list(map(int, input().split()))
n_b = list(map(int, input().split()))

location_m = []
location_n = []
count_m_a = 0
count_n_b = 0

for iter in m_a:
    location_m.append(a + iter)
for iter in n_b:
    location_n.append(b + iter)

# print('{}\n{}'.format(location_m,location_n))

for iter in location_m:
    if iter >= s and iter <= t:
        count_m_a += 1
    else:
        continue
for iter in location_n:
    if iter >= s and iter <= t:
        count_n_b += 1
    else:
        continue

print("{}\n{}".format(count_m_a, count_n_b))