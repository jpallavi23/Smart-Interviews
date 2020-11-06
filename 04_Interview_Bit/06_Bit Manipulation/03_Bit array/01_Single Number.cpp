// For question go to
// https://www.interviewbit.com/problems/single-number/

int Solution::singleNumber(const vector<int> &A) {
    if(A.size() == 0){
        return 0;
    }
        
    int number = A[0];
    for(int i = 1; i < A.size(); i++){
        number = number ^ A[i];
    }
        
    return number;
}