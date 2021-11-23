// Add up all numbers n below 1000 where n divisible by 3 or 5

#include <iostream>
using namespace std;

int sum_to_n(int n){
    return n*(n+1)/2;
}

int main(){
    double res;
    int n3 = 999/3;
    int n5 = 999/5;
    int n15 = 999/15;
    res = 3*sum_to_n(n3) + 5*sum_to_n(n5) - 15*sum_to_n(n15);
    cout << res;
    return res;
}
