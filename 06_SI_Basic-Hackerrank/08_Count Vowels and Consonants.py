'''
Given a string, print count of vowels and consonants of the string.

Input Format
Input contains a string of upperscase and lowercase characters - S.

Constraints
1 <= len(S) <= 100

Output Format
Print count of vowels and consonants for the given string, separated by space.

Sample Input 0
abxbbiaaspw

Sample Output 0
4 7
'''

string = input().lower()
vowels = consonants = 0
for _ in string:
    if _ in 'aeiou':
        vowels += 1
    else:
        consonants += 1
print(f"{vowels} {consonants}")