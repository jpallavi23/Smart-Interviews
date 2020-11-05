'''
Given non-negative integer - N, print the sum of digits of the given number.

Input Format
Input contains non-negative integer - N.

Constraints
0 <= length(N) <= 103

Output Format
Print the sum of digits of the given number.

Sample Input 0
164

Sample Output 0
11
'''

n = int(input())
sum_n = 0

while n > 0:
    rem = n % 10
    sum_n += rem
    n = int(n // 10)

print(sum_n)