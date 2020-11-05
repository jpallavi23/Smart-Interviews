'''
Given two matrices A and B of size N x M. Print sum(A+B) of matrices(A, B).
Note: Try solving it by declaring only a single matrix.

Input Format
First line of input contains N, M - size of the matrices. Its followed by 2*N lines each containing M integers - elements of the matrices. First N lines for matrix A and its followed by N lines for matrix B.

Constraints
1 <= N, M <= 100
-106 <= ar[i] <= 106

Output Format
Print sum(A+B) of matrices(A, B).

Sample Input 0
2 3
5 -1 3
19 8 4
4 5 -6
1 -2 12

Sample Output 0
9 4 -3
20 6 16
'''

n, m = map(int, input().split())
arr1 = []
arr2 = []
sum_arr = []
for _ in range(1, n+1):
    arr1.append(list(map(int, input().split())))
for _ in range(1, n+1):
    arr2.append(list(map(int, input().split())))
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(arr1[i][j] + arr2[i][j])
    sum_arr.append(temp)
for i in range(n):
    print(*sum_arr[i])