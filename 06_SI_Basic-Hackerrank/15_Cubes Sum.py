'''
Given positive integer - N, print the sum of cubes of 1st N natural numbers.

Input Format
Input contains a positive integer - N.

Constraints
1 <= N <= 102

Output Format
Print the sum of cubes of 1st N natural numbers.

Sample Input 0
4

Sample Output 0
100
'''

n = int(input())
cube_sum = 0
for _ in range(n+1):
    cube = _ ** 3
    cube_sum += cube

print(cube_sum)