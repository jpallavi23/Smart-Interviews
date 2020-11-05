'''
Given sides of a triangle, check whether the triangle is valid.

Input Format
Input contains three integers A, B, C - Sides of the triangle.

Constraints
1 <= A, B, C <= 109

Output Format
Print "Yes" if you can construct a triangle with the given three sides, "No" otherwise.

Sample Input 0
4 3 5

Sample Output 0
Yes
'''

s1, s2, s3 = map(int, input().split())

if (s1 + s2 <= s3) or (s1 + s3 <= s2) or (s2 + s3 <= s1):
    print("No")
else:
    print("Yes")