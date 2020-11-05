'''
Given N, print the sum of squares of 1st N natural numbers.

Input Format
Input contains positive integer - N.

Constraints
1 <= N <= 103

Output Format
Print the sum of squares of 1st N natural numbers.

Sample Input 0
15

Sample Output 0
1240
'''

n = int(input())
sq_sum = 0
for _ in range(n+1):
    sq = _ ** 2
    sq_sum += sq

print(sq_sum)