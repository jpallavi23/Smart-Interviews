'''
Given a matrix of size N x M. Print column-wise sum, separated by a newline.

Input Format
The first line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints
1 <= N, M <= 100
-106 <= ar[i] <= 106

Output Format
Print the column wise sum, separated by newline.

Sample Input 0
2 2
5 -1
19 8

Sample Output 0
24
7
'''

n, m = map(int, input().split())
arr = []

for _ in range(1, n+1):
    arr.append(list(map(int, input().split())))

for col in range(len(arr[0])):
    sum_col = 0
    for row in range(len(arr)):
        sum_col += arr[row][col]
    print(sum_col)