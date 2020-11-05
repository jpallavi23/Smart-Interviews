# For question go to:
# https://www.hackerrank.com/challenges/magic-square-forming/problem

square_matrix = []

for _ in range(3):
    square_matrix.append(list(map(int, input().strip().split())))

possiblePermutations = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], 
                        [[6, 1, 8], [7, 5, 3], [2, 9, 4]], 
                        [[4, 9, 2], [3, 5, 7], [8, 1, 6]], 
                        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
                        [[8, 3, 4], [1, 5, 9], [6, 7, 2]], 
                        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
                        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
                        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

min_cost = 45
for itr in possiblePermutations:
    cost = 0
    for ctr in range(3):
        for ktr in range(3):
            cost += abs(itr[ctr][ktr] - square_matrix[ctr][ktr])
    min_cost = min(min_cost, cost)

print(min_cost)