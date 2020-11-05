'''
Print sum of all odd elements in an array.

Input Format
Input contains 2 lines, first line contains integer N - the size of the array and second line contains array elements.

Constraints
1 <= N <= 102
-106 <= ar[i] <= 106

Output Format
Print sum of all odd elements.

Sample Input 0
5
6 9 8 4 3

Sample Output 0
12
'''
size = int(input())
array = list(map(int, input().split()))
odd_sum = 0

for item in array:
    if item % 2 == 1:
        odd_sum += item

print(odd_sum)