// For question go to
// https://www.interviewbit.com/problems/number-of-1-bits/

int numSetBits(unsigned int A) {
    int count = 0;
    while(A != 0) {
        if((A & 1) == 1) {
            count ++;
        }
        A >>= 1;
    }
    return count;
}