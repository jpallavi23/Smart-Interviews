# For question go to:
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

height_of_each_letter = list(map(int, input().split()))
word = input()

count = 0
length = []
for itr in range(0, len(word)):
    count = ord(word[itr]) - 97
    length.append(height_of_each_letter[count])

print(max(length) * len(word))