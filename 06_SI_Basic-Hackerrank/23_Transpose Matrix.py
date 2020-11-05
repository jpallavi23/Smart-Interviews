'''
Given a matrix of size N x M. Print transpose of the matrix.

Input Format
First line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints
1 <= N, M <= 100
-109 <= ar[i] <= 109

Output Format
Print the transposed matrix.

Sample Input 0
2 2
5 -1
19 8

Sample Output 0
5 19
-1 8
'''

n, m = map(int, input().split())
arr = []

for _ in range(1, n+1):
    arr.append(list(map(int, input().split())))

result = map(list, zip(*arr))
for transpose in result:
   print(*transpose)