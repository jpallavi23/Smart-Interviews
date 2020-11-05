'''
Given N, check whether it is a Narcissistic number or not. A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits

Input Format
Input contains a integer - N.

Constraints
0 <= N <= 109

Output Format
Print "Yes" if the number is Narcissistic number, "No" otherwise.

Sample Input 0
8208

Sample Output 0
Yes

Explanation 0
84 + 24 + 04 + 84 = 8208
'''

n = int(input())
temp = n
len_n = 0

while temp > 0:
    len_n += 1
    temp = temp // 10

n_sum = 0
temp = n
while temp > 0:
    rem = temp % 10
    n_sum += rem ** len_n
    temp = temp // 10

if n_sum == n:
    print("Yes")
else:
    print("No")