# For question go to:
# https://www.codechef.com/OCT20B/problems/CHEFEZQ

no_of_test_cases = int(input())

while no_of_test_cases > 0:
    n, k = map(int, input().split())
    arr = [int(ip) for ip in input().split()]
    sum_arr = sum(arr)
    flag = 0

    for itr in range(n - 1):
        if(arr[itr] < k):
            flag = 1
            q_day = itr
            break
        arr[itr + 1] += (arr[itr] - k)
    
    if(flag == 1):
        print(int(q_day + 1))
    else:
        q_day = (sum_arr / k) + 1
        print(int(q_day))
    no_of_test_cases -= 1