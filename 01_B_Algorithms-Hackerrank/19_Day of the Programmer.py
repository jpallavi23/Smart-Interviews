# For question go to:
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

yr = int(input())

sum_7months = 215
if yr < 1918:
    if yr % 4:
        month_2 = 28
    else:
        month_2 = 29
elif yr > 1918:
    if (yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0:
        month_2 = 29
    else:
        month_2 = 28
else:
    month_2 = 15

date = 256 - (sum_7months + month_2)
print("{}.09.{}".format(date, yr))