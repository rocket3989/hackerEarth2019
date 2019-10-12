#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    
    long tc, n, occ, preLen, rot;
    char test;
    
    cin >> tc;
    
    while(tc--){
        rot = 0;
        cin >> n >> occ >> preLen >> test;
        char* arr = new char[n];
        
        for(long i = 0; i < n; i++)
            cin >> arr[i];
            
        for(long i = 0; i < preLen; i++){
            if(arr[i] == test)
                occ--;
        }
        
        while(true){
            if(occ <= 0){
                cout << rot << '\n';
                break;
            }
            if(rot > n){
                cout << -1 << '\n';
                break;
            }
            if(arr[n - rot - 1] == test)
                occ--;
                
            if(arr[(n + preLen - rot - 1) % n] == test)
                occ++;  
            
            rot++;
        }
        delete [] arr;
        
    }
    return 0;
}