'''
Implement linear search. Given an array, search key in the array. If key not found print "-1", otherwise print the index of the array.

Input Format
First line of input contains two integers N and K. N is the size of array and K is the key. Second line contains array elements.

Constraints
1 <= N <= 102
0 <= ar[i] <= 109

Output Format
print the index of key.

Sample Input 0
5 15
-2 -19 8 15 4

Sample Output 0
3
'''

size, key = map(int, input().split())
arr = list(map(int, input().split()))
temp = 0
for i in range(size):
    if arr[i] == key:
        temp = 1
        break
    else:
        continue
if temp: print(i)
else: print('-1')