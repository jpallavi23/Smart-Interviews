# For question go to:
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-rotation-of-matrix

def print_matrix(matrix_elements):
    for itr in range(len(matrix_elements)):
        for ctr in range(len(matrix_elements)):
            print(str(matrix_elements[itr][ctr]), end = " ")
        print()

def rotate(matrix_elements, n_size):
    for itr in range(n_size // 2):
        for ctr in range(itr, n_size - itr - 1):
            temp = matrix_elements[itr][ctr]
            matrix_elements[itr][ctr] = matrix_elements[n_size - 1 - ctr][itr]
            matrix_elements[n_size - 1 - ctr][itr] = matrix_elements[n_size - 1 - itr][n_size - 1 - ctr]
            matrix_elements[n_size - 1 - itr][n_size - 1 - ctr] = matrix_elements[ctr][n_size - 1 - itr]
            matrix_elements[ctr][n_size - 1 - itr] = temp

if __name__ == "__main__":
    no_of_test_cases = int(input())
    itr = 0
    while(itr < no_of_test_cases):
        matrix_elements = []
        n_size = int(input())
        for _ in range(n_size):
            matrix_elements.append(list(map(int, input().rstrip().split())))
        rotate(matrix_elements, n_size)

        print("Test Case #{}:".format(itr + 1))
        print_matrix(matrix_elements)

        itr += 1