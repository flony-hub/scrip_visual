#include <iostream>
#include <math.h>
using namespace std;

float ramanujan(int depth){
    int base = 6;
    int multiplo = 1;
    float sum;
    while (depth>0)
    {        
        sum = (multiplo+depth)*sqrt(base+depth);
        ramanujan(depth-1);
    }
    return sum + sqrt(6);
}

int main() {
    float total = ramanujan(0);
    cout << total;
    return 0;
}