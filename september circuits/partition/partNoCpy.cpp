#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define min(a,b) (a < b ? a : b)
#define min3(a,b,c) (a < b ? a < c ? a : c : b < c ? b : c)
#define MOD 1000000007

unordered_map<int,unordered_map<int,ull>> dp[5000];
int prefix[5000] = {0};
int n;
string vals;

int main(){
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    

    cin >> n >> vals;


    for(int i = 0; i < n; i++)
        prefix[i + 1] = prefix[i] + vals[i] - '0'; 

    for(int i = 0; i < n; i++)
        dp[n - i - 1] = {{min(i, n - i - 1), {{min(prefix[n] - prefix[n - i - 1], n - i - 1), 1}}}};
    

    for(int column = n - 1; column >= 0; column--){
        if (vals[column] == '0'){
            dp[n].clear();
            continue;
        }
        
        auto colRef = &dp[column];
        

        int top = min(n - column - 1, column);
        auto last = colRef -> find(top);
        
        vector<pair<int,unordered_map<int, ull>>> seen;
        seen.push_back(*last);

        for(int row = top; row >= 0; row--){
            
            if (row != top){
                auto rowRef = colRef -> find(row);
                if(rowRef != colRef -> end()){
                    seen.push_back(*rowRef);
                }
            }
            
            
            int related = column - row - 1;
            if (vals[related] == '0')
                continue;
                
            int diff = prefix[column] - prefix[related];

            if (related >= 0){

                auto relDictRef = &(dp[related][min(row, related)]);

                for(auto dictSeen : seen){
                    for(auto kvPair : dictSeen.second){
                        if (kvPair.first < diff)
                            continue;

                        int check = min3(kvPair.first, diff, related);
                    
                        ull* ref = &(relDictRef -> emplace(check, 0).first -> second);
                        *ref = (*ref + kvPair.second) % MOD;   

                    }

                }
            }

            

        }
        if (column != 0)
            dp[n].clear();

    }
    
    // for (int row = 0; row < n; row ++){
    //     for (int col = 0; col < n; col++){
    //         bool printed = false;
    //         if (dp[col].size() > row){
    //             for (auto kv : dp[col][row]){
    //                 printed = true;
    //                 cout << kv.first << ' ' << kv.second << "    ";
    //             }
    //         }
    //         if(!printed)
    //             cout << "       ";
    //     }
    //     cout << endl;
    // }
    
    cout << dp[0][0][0] << endl;
    
}


