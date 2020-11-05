# For question go to
# https://www.hackerrank.com/contests/smart-interviews/challenges/si-repeated-numbers

def merge(array, low, mid, high):
    temp = [high - low + 1]
    p1 = low
    p2 = mid + 1
    idx = 0
    while(p1 <= mid and p2 <= high):
        if(array[p1] <= array[p2]):
            temp[idx] = array[p1]
            idx += 1
            p1 += 1
        else:
            temp[idx] = array[p2]
            idx += 1
            p2 += 1
    while(p1 <= mid):
        temp[idx] = array[p1]
        idx += 1
        p1 += 1
    while(p2 <= high):
        temp[idx] = array[p2]
        idx += 1
        p2 += 1
    for itr in range(high - low + 1):
        array[low + itr] = temp[itr]

def mergeSort(array, low, high):
    if(low == high):
        return
    mid = (low + high) / 2
    mergeSort(array, low, mid)
    mergeSort(array, mid + 1, high)
    merge(array, low, mid, high)

if __name__ == "__main__":
    no_of_test_cases = int(input())
    while no_of_test_cases:
        array_size = int(input())
        array = list(map(int, input().split()))
        mergeSort(array, 0, array_size - 1)
        for itr in range(array_size):
            if array[itr] == array[itr + 1]:
                print(array[itr], end = " ")
        print()
        no_of_test_cases -= 1