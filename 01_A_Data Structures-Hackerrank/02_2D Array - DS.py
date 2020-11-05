# For question go to:
# https://www.hackerrank.com/challenges/2d-array/problem

array_elements = []

hourglass_sum = []
for _ in range(6):
    array_elements.append(list(map(int, input().rstrip().split())))

# print(array_elements)

for itr in range(6 - 2):
    for ctr in range(6 - 2):
        hourglass_sum.append(array_elements[itr][ctr] + array_elements[itr][ctr + 1] + array_elements[itr][ctr + 2]
                                                    + array_elements[itr + 1][ctr + 1] +
                            array_elements[itr + 2][ctr] + array_elements[itr + 2][ctr + 1] + array_elements[itr + 2][ctr + 2])

print(max(hourglass_sum))