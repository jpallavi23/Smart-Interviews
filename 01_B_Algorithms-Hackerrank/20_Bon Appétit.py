# For question go to:
# https://www.hackerrank.com/challenges/bon-appetit/problem

no_of_items, key = map(int, input().split())
array_of_items = list(map(int, input().split()))
charged = int(input())

array_of_items.pop(key)

array_sum = sum(array_of_items)

if charged != (array_sum/2):
    print(int(charged - (array_sum/2)))
else:
    print("Bon Appetit")