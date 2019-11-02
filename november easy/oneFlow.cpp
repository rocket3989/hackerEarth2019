#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;

namespace std {
template <> struct hash<std::pair<int, int>> {
    inline size_t operator()(const std::pair<int, int> &v) const {
        std::hash<int> int_hasher;
        return int_hasher(v.first) ^ int_hasher(v.second);
    }
};

}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int tc, N, M, u, v;

    for (int test = 0; test < tc; test++){
        cin >> N >> M;

        unordered_map<int, vector<int>> outNode;
        unordered_map<int, vector<int>> inNode;

        unordered_set<pair<int, int>> edgeSet;

        bool fail = false;

        if (M < N)
            cout << "No";

        else{
            for(int count = 0; count < M; count++){
                cin >> u >> v;
                if (u == v) continue;

                if(edgeSet.find(make_pair(u, v)) != edgeSet.end())
                    fail = true;
                
                edgeSet.insert(make_pair(u, v));
                
                outNode.emplace(v);

                for(auto &a : outNode[v]){
                    if(edgeSet.find(make_pair(u, a)) != edgeSet.end())
                        fail = true;
                    if(u != a)
                        edgeSet.insert(make_pair(u, a));
                }
                
                inNode.emplace(u);

                for(auto &a : inNode[u]){
                    if(edgeSet.find(make_pair(a, v)) != edgeSet.end())
                        fail = true;
                    if(a != v)
                        edgeSet.insert(make_pair(a, v));
                }
                if(fail){
                    cout << "No";
                    break;
                }
                
                outNode.emplace(u);
                outNode[u].push_back(v);

                inNode.emplace(v);
                inNode[v].push_back(u);

                
            }
            if (!fail){
                if(edgeSet.size() == N * (N - 1))
                    cout << "Yes";
                else 
                    cout << "No";
            }
        }
        cout << '\n';
    }
}
