'''
Given a String, compress the given string. See example for more details.

Input Format
Input contains string of lowercase and uppercase characters - S.

Constraints
1 <= len(S) <= 100

Output Format
Print the compressed string.

Sample Input 0
aaaBBBBhhhekkL

Sample Output 0
a3B4h3e1k2L1

Explanation 0
In the given string, a is repeating for 3 times - after compression a3.
Similarly, B is repeating for 4 times - B4
h is repeating for 3 times - h3
e is repeating for 1 times - e1
k is repeating for 2 times - k2
L is repeating for 1 times - L1
'''

string = input()

temp = {}
compressed_string = ""
for _ in string:
    if _ in temp:
        temp[_] += 1
    else:
        temp[_] = 1

for character, count in temp.items():
    compressed_string += str(character) + str(count)

print(compressed_string)