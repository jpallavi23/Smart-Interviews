'''
Find a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format
First line of input contains size of the array - N and second line contains the elements of the array.

Constraints
2 <= N <= 100
0 <= ar[i] <= 109

Output Format
Print the duplicate element from the given array.

Sample Input 0
6
5 4 10 9 21 10

Sample Output 0
10
'''

size_of_array = int(input())
array_elements = list(map(int, input().split()))
count = {}

for _ in array_elements:
    if _ in count:
        print(_)
        exit()
    else:
        count[_] = 1