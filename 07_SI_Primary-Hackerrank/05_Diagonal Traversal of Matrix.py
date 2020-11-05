# For question go to:
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-diagonal-traversal-of-matrix   

if __name__ == "__main__":
    no_of_test_cases = int(input())
    while(no_of_test_cases > 0):
        sumd = 0
        matrix_elements = []
        n_size = int(input())
        for _ in range(n_size):
            matrix_elements.append(list(map(int, input().rstrip().split())))

        ktr = 0
        size = n_size - 1
        flag = n_size
        if(n_size == 1):
            print(matrix_elements[0][0])
        else:
            d_sum = []
            while(not(size < 0)):
                itr = ktr
                for ctr in range(size, n_size):
                    sumd += matrix_elements[itr][ctr]
                    if(itr == n_size and ctr == n_size):
                        ktr += 1
                        n_size -=1
                        size = flag - 1
                    itr += 1
                d_sum.append(sumd)
                sumd = 0
                size -= 1

            n_size = flag
            ktr = 1
            size = 0
            while(not(ktr > flag - 1)):
                itr = ktr
                for ctr in range(size, n_size - 1):
                    sumd += matrix_elements[itr][ctr]
                    itr += 1
                d_sum.append(sumd)
                sumd = 0
                n_size -= 1
                ktr += 1
            
            for itr in d_sum:
                print(itr, end = " ")
            print()
            
        no_of_test_cases -= 1