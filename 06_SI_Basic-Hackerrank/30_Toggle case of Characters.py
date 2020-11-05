'''
Given a string, toggle case of each character in the given string.

Input Format
Input contains a string - S.

Constraints
1 <= len(S) <= 100

Output Format
Print the toggled string.

Sample Input 0
abdBd

Sample Output 0
ABDbD
'''

print(input().swapcase())

# string = input()
# toggled = ""

# for char in range(len(string)):
#     if (string[char] >= 'a' and string[char] <= 'z'):
#         toggled += string[char].upper()
#     elif (string[char] >= 'A' and string[char] <= 'Z'):
#         toggled += string[char].lower()
#     else:
#         toggled += string[char]

# print(toggled)