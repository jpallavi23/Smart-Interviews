'''
Find maximum element from the given array of integers.

Input Format
First line of input contains N - the size of the array and second line contains the elements of the array.

Constraints
1 <= N <= 103
-109 <= ar[i] <= 109

Output Format
Print the maximum element of array.

Sample Input 0
5
-2 -19 8 15 4

Sample Output 0
15
'''

size = int(input())
array = list(map(int, input().split()))
max_element = array[0]

for itr in range(1, size):
    if max_element < array[itr]:
        max_element = array[itr]

print(max_element)