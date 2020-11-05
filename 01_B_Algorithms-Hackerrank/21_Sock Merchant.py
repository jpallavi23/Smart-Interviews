# For question go to:
# https://www.hackerrank.com/challenges/sock-merchant/problem

no_of_socks = int(input())
sock_colors = sorted(list(map(int, input().split())))
colors = set(sock_colors)

count_pairs = 0
for _ in colors:
    count_pairs += sock_colors.count(_) // 2

print(count_pairs)