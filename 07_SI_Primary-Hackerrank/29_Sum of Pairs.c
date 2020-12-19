// For question go to
// https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-pairs

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

void merge(int a[], int lo, int mid, int hi) {
    int temp[hi-lo+1];
    int p1=lo, p2=mid+1;
    int idx=0;
    while(p1 <= mid && p2 <= hi){
        if(a[p1] <= a[p2])
            temp[idx++] = a[p1++];
        else
            temp[idx++] = a[p2++];
    }
    while(p1<=mid)
        temp[idx++] = a[p1++];
    while(p2<=hi)
        temp[idx++] = a[p2++];
    for(int i=0;i<hi-lo+1;i++)
        a[lo+i] = temp[i];
    for(int i=0;i<hi;i++) {
        
    }
}
void mergeSort(int a[], int lo, int hi) {
    if(lo == hi)
        return;
    int mid = (lo+hi)/2;
    mergeSort(a, lo, mid);
    mergeSort(a, mid+1, hi);
    merge(a, lo, mid, hi);
}
bool BSR(int ar[], int n, int k, int lo, int hi) {
    if(lo > hi)
        return false;
    int mid = (lo+hi)/2;
    if(ar[mid] == k)
        return true;
    if(ar[mid] < k)
        return BSR(ar, n, k, mid+1, hi);
    return BSR(ar, n, k, lo, mid-1);
}
bool checkSumOfPairs(int a[], int n, int k) {
    mergeSort(a, 0, n-1);
    for(int i=0;i<n;i++) {
        if(BSR(a, n, k-a[i], i+1, n-1))
            return true;
    }
    return false;
}
int main() {
    int ntc = 0;
    scanf("%d", &ntc);
    while(ntc!=0) {
        int n,k;
        scanf("%d %d", &n, &k);
        int a[n];
        for(int i=0;i<n;i++) {
            scanf("%d", &a[i]);
        }
        int flag = checkSumOfPairs(a, n, k);
        if(flag == 1)
            printf("True");
        else
            printf("False");
        printf("\n");
        ntc--;
    }
    return 0;
}