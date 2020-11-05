'''
Given a sentence and a character, count occurrence of the given character in the sentence. All characters in the sentence are lower case.

Input Format
First line of input contains a sentence - S and second line of input contains a lowercase character - ch.

Constraints
1 <= len(S) <= 100
'a' <= ch <= 'z'

Output Format
Print count of the given character in the sentence.

Sample Input 0
You're a good person.
o

Sample Output 0
4
'''

sentence = input().lower()
key = input().lower()
count = 0
for _ in sentence:
    if _ == key:
        count += 1
    else:
        continue
print(count)