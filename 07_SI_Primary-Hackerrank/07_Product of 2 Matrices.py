# For question go to:
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-product-of-2-matrices

no_of_test_cases = int(input())

while(no_of_test_cases > 0):
    arr1_n1, arr1_m1 = map(int, input().split())
    arr1 = []
    for _ in range(arr1_n1):
        arr1.append(list(map(int, input().rstrip().split())))
    
    arr2_n2, arr2_m2 = map(int, input().split())
    arr2 = []
    for _ in range(arr2_n2):
        arr2.append(list(map(int, input().rstrip().split())))
    
    product_res = [[sum(x * y for x, y in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]
    
    for itr in range(0, arr1_n1):
        for ctr in range(0, arr2_m2):
            print(product_res[itr][ctr], end = " ")
        print()
    
    no_of_test_cases -= 1