#include <bits/stdc++.h>
using namespace std;



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // ifstream cin("input.txt");
    // ofstream cout("output.txt");

    int n, parent, currentCost = 0;
    cin >> n;

    vector<set<pair<int, int>>> children(n);

    vector<int> cost(n);

    for(int i = 0; i < n; i++)
        cin >> cost[i];

    for(int i = 1; i < n; i++){
        cin >> parent;
        children[parent - 1].insert(make_pair(cost[i], i));
    }
    

    for(auto parent : children){
        if(parent.size() == 0){
            cout << 0 << '\n';
        }
        else{
            for(auto child : parent){
                cout << child.second + 1 << ' ';
            }
            cout << '\n';
        }
    }
}