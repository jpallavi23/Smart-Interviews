'''
Check whether a given number is Armstrong number.

Input Format
Input contains a integer - N.

Constraints
0 <= N <= 109

Output Format
Print "Yes" if the number is Armstrong number, "No" otherwise.

Sample Input 0
153

Sample Output 0
Yes

Explanation 0
13 + 53 + 33 = 153
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