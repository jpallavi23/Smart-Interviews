'''
Given a string, check if it contains only vowels.

Input Format
Input contains a string of lowercase and uppercase characters- S.

Constraints
1 <= len(S) <= 100

Output Format
Print "Yes" if string contains only vowels, "No" Otherwise.

Sample Input 0
askhtwsflk

Sample Output 0
No
'''

string = input().lower()
temp = 0
for _ in string:
    if _ in 'aeiou':
        continue
    else:
        temp = 1
        break
if temp == 1:
    print("No")
else:
    print("Yes")