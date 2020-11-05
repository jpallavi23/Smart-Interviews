'''
Given a matrix of size N x M. Print whether it is a sparse matrix. A matrix containing 0 value in more than half of its elements, then it is called a sparse matrix.

Input Format
First line of input contains N, M - size of the matrix. Its followed by N lines each containing M intergers - elements of the matrix.

Constraints
1 <= N, M <= 100
0 <= ar[i] <= 109

Output Format
Print "Yes" if given matrix is Sparse matrix, otherwise print "No".

Sample Input 0
2 3
5 0 0
0 8 0

Sample Output 0
Yes
'''

n_rows, m_cols = map(int, input().split())
matrix_elements = []
count = 0
for itr in range(0, n_rows):
    matrix_elements.append(list(map(int, input().split())))
    for ctr in range(0, m_cols):
        if matrix_elements[itr][ctr] == 0:
            count += 1

if count > ((n_rows * m_cols) / 2):
    print("Yes")
else:
    print("No")