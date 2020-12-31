# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-triple-trouble

def check(arr, size):
    res = 0
    for itr in range(0, 32):
        sum_of_setBits = 0
        x = (1 << itr)
        for ctr in range(0, size):
            if(arr[ctr] & x):
                sum_of_setBits = sum_of_setBits + 1
        if((sum_of_setBits % 3) != 0):
            res = res | x
    return res

if __name__ == "__main__":
    no_of_testcases = int(input())
    while no_of_testcases > 0:
        size = int(input())
        array = list(map(int,input().strip().split()))[:size]
        print(check(array, size))
        no_of_testcases -= 1