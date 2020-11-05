# For question go to:
# https://www.hackerrank.com/contests/smart-interviews-gcet-2021-a/challenges/si-number-of-valid-subarrays

def validSubarrays(arr, n): 
    dictonary = dict() 
    sum_arr = 0
    iter = 0

    while iter < n:
        sum_arr += (-1 if (arr[iter] == 0) else arr[iter]) 
        if dictonary.get(sum_arr): 
            dictonary[sum_arr]+=1
        else: 
            dictonary[sum_arr]=1
        iter += 1
      
    count = 0
    iter = 0
    for itr in dictonary: 
        if dictonary[itr] > 1: 
            count += ((dictonary[itr] * int(dictonary[itr] - 1)) / 2) 
      
    if dictonary.get(0): 
        count += dictonary[0] 

    return int(count) 



no_of_test_cases = int(input())
iter = 1
while iter <= no_of_test_cases:
    size = int(input())
    array = list(map(int, input().split()))
    array_size = len(array)
    print(validSubarrays(array, array_size))
    iter += 1