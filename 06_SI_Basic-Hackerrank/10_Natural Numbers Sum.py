'''
Given positive integer - N, print the sum of 1st N natural numbers.

Input Format
Input contains a positive integer - N.

Constraints
1 <= N <= 104

Output Format
Print the sum of 1st N natural numbers.

Sample Input 0
4

Sample Output 0
10
'''

n = int(input())
sum_n = 0
for _ in range(n+1):
    sum_n += _
print(sum_n)