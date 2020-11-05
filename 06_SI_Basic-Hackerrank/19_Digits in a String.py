'''
Given a string, check if it contains only digits.

Input Format
Input contains a string - S.

Constraints
1 <= len(S) <= 100

Output Format
Print "Yes" if string contains only digits, "No" otherwise.

Sample Input 0
123456786543

Sample Output 0
Yes
'''

string = input()
temp = 0
for _ in string:
    if _ in '1234567890':
        continue
    else:
        temp = 1
        break

if temp == 0:
    print("Yes")
else:
    print("No")