#include <bits/stdc++.h>
using namespace std;

const long N = 100000001;

char *sieve;


void get_primes(unsigned long max){
    sieve = new char[max/8+1];
    memset(sieve, 0xFF, (max/8+1) * sizeof(char));
    for(unsigned long x = 2; x <= max; x++)
        if(sieve[x/8] & (0x01 << (x % 8)))
            for(unsigned long j = 2*x; j <= max; j += x)
                sieve[j/8] &= ~(0x01 << (j % 8));
}


int main() {
    get_primes(N);
    int tc, n, a;
    cin >> tc;
    while(tc--){
        cin >> n;
        int count = 0;
        while(n--){
            cin >> a;
            if(sieve[a/8] & (0x01 << (a % 8)))
                count++;
        }
        cout << count << '\n';
    }
    cout << flush;
    
}