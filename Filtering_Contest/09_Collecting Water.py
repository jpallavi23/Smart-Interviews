# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-collecting-water

x = int(input())

while x > 0:
    x -= 1

    length = int(input())
    li = list(map(int, input().split()))
    list1, list2 = [0]*length, [0]*length
    result, list1[0]= 0, li[0]
 
    i = 1
    while i < length:
        list1[i] = max(list1[i-1], li[i])
        i += 1

    list2[length-1] = li[length-1]

    for i in range(length - 2, -1, -1):
        list2[i] = max(list2[i + 1], li[i])

    i = 0
    while i < length:
        result += min(list1[i], list2[i]) - li[i]
        i += 1

    print(result)