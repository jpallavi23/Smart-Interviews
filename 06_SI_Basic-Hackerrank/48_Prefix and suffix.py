'''
Given a string, compute the length of longest prefix string which is same as the suffix of the string, the length of the prefix or suffix string must be less than the given input string.

Input Format
Input contains a string - S.

Constraints
1 <= len(S) <= 100

Output Format
Print length of longest prefix string which is same as suffix of the string.

Sample Input 0
smartintsmart

Sample Output 0
5
'''

string = input()

lenght_of_string = len(string)
for _ in range(lenght_of_string - 1, 0, -1):
    prefix = string[0: _]
    suffix = string[lenght_of_string - _: lenght_of_string]
    if(prefix == suffix):
        print(_)
        break
else:
    print(0)