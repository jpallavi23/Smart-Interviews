# For question go to:
# https://www.hackerrank.com/challenges/array-left-rotation/problem

no_of_integers, no_of_left_rotations = map(int, input().split())
array_elements = list(map(int, input().split()))

left_rotated_array = array_elements[(no_of_left_rotations % no_of_integers):] + array_elements[:(no_of_left_rotations % no_of_integers)]

for itr in left_rotated_array:
    print(itr, end=' ')