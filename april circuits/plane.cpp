#include <bits/stdc++.h>
#define ull unsigned long long
#define MOD 1000000007
using namespace std;

ull N, M, val;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    
    vector<ull> planes;
    multiset<ull> groups;
    
    for(int i = 0; i < N; i++){
        cin >> val;
        groups.insert(val);
    }
    
    for(int i = 0; i < M; i++){
        cin >> val;
        planes.push_back(val);
    }
    
    sort(planes.begin(), planes.end());
    
    ull trips = -1, last = -1, planesEnd = -1;
    
    while (!groups.empty()){
        trips += 2;
        
        for(ull i = M - 1; i != planesEnd; --i){
            auto it = groups.upper_bound(planes[i]);
            if(it == groups.begin()){
                planesEnd = i;
                break;
            }
            it--;
                
            groups.erase(it);
            
        }
        
        if (last == groups.size()){
            trips = -1;
            break;
        }
        
        last = groups.size();
    }
    
    cout << trips << endl;
}

