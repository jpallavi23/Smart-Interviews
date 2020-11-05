'''
Given a String, print all the letters present at odd index followed by the letters present at even index.

Input Format
Input contains a string - S.

Constraints
1 <= len(S) <= 100

Output Format
Print letters present at odd index followed by the letters present at even index.

Sample Input 0
afdg5tg

Sample Output 0
fgtad5g
'''

string = input()

odd = ""
even = ""
for _ in range(len(string)):
    if _ % 2 == 0:
        even += string[_]
    else:
        odd += string[_]

print("{}".format(odd+even))