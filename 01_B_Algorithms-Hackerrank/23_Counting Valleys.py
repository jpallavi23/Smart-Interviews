# For question go to:
# https://www.hackerrank.com/challenges/counting-valleys/problem

no_of_steps = int(input())
path_of_steps = input().upper()

sea_level = 0
count_valleys = 0
for itr in path_of_steps:
    if itr == 'U':
        sea_level += 1
        if sea_level == 0:
            count_valleys += 1
    else:
        sea_level -= 1

print(count_valleys)