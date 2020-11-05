'''
Given a matrix of size N x M. Print row-wise sum, separated by a newline.
Note: Try to solve this without declaring/storing the matrix.

Input Format
First line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints
1 <= N, M <= 100
-106 <= ar[i] <= 106

Output Format
Print the row-wise sum, separated by a newline.

Sample Input 0
2 3
5 -1 3
19 8 -5

Sample Output 0
7
22
'''

n, m = map(int, input().split())
arr = []

for _ in range(1, n+1):
    arr.append(list(map(int, input().split())))

for row in range(len(arr)):
    sum_row = 0
    for col in range(len(arr[0])):
        sum_row += arr[row][col]
    print(sum_row)