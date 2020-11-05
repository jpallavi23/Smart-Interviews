'''
Given a number - N, reverse the number.

Input Format
Input contains a integer - N.

Constraints
-1018<= N <= 1018

Output Format
Print the reversed number.

Sample Input 0
1344

Sample Output 0
4431
'''

n = int(input())
rev_n = 0

if n < 0:
    print('-', end="")
    n = abs(n)

while n > 0:
    rem = n % 10
    rev_n = rev_n * 10 + rem
    n = int(n // 10)

print(rev_n)