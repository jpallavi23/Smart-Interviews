# For question go to:
# https://www.hackerrank.com/challenges/time-conversion/problem

time = input().upper().split(":")

time[0] = int(time[0])%12
if "PM" in time[-1] and [0]:
    time[0]+=12
time[0] = '%02d' % time[0]

print(":".join(time)[:-2])