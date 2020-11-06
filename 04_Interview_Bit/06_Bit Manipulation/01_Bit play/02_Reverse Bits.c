// For question go to
// https://www.interviewbit.com/problems/reverse-bits/

unsigned int reverse(unsigned int A) {
    unsigned int num = 0;
    int bits = 31;
    int itr = 0;
    while(A) {
        num += pow(2, 31 - itr) * (A % 2);
        A /= 2;
        itr ++;
    }
    return num;
}