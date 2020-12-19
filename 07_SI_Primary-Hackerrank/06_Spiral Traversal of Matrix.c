// For question go to:
// https://www.hackerrank.com/contests/smart-interviews/challenges/si-spiral-traversal-of-matrix

#include <stdio.h>
#include <stdlib.h>

void spiralPrint(int e_row, int e_col, int a[e_row][e_col]) {
    int itr, s_row = 0, s_col = 0;
    while(s_row < e_row && s_col < e_col) {
        for(itr = s_col; itr < e_col; itr++)
            printf("%d ", a[s_row][itr]);
        s_row++;
        for(itr = s_row; itr < e_row; itr++)
            printf("%d ", a[itr][e_col - 1]);
        e_col--;
        if(s_row < e_row) {
            for(itr = e_col - 1; itr >= s_col; itr--)
                printf("%d ", a[e_row - 1][itr]);
            e_row--;
        }
        if(s_col < e_col) {
            for(itr = e_row - 1; itr >= s_row; itr--)
                printf("%d ", a[itr][s_col]);
            s_col++;
        }
    }
}
int main() {
    int no_of_testcases;
    scanf("%d", &no_of_testcases);
    while(no_of_testcases > 0) {
        int size;
        scanf("%d",&size);
        int arr[size][size];
        for(int itr = 0; itr < size; itr++) {
            for(int ctr = 0; ctr < size; ctr++) {
                scanf("%d", &arr[itr][ctr]);
            }
        }
        spiralPrint(size, size, arr);
        printf("\n");
        no_of_testcases--;
    }
    return 0;
}
