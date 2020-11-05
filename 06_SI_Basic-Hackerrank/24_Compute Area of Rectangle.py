'''
Given the length and breadth of the rectangle. Print area of the rectangle.

Input Format
Input contains two positive integers L - length of the rectangle and B - breadth of the rectangle.

Constraints
1 <= L, B <=109

Output Format
Print area of the rectangle.

Sample Input 0
5 8

Sample Output 0
40
'''

length, breadth = map(int, input().split())
area_of_rect = length * breadth
print(area_of_rect)