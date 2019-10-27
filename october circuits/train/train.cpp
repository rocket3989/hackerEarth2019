#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;

struct Train{
    Train(){}
    Train(int _source, int _dest, int _time, int _cost, int _period, int _id){
        source = _source;
        dest = _dest;
        time = _time;
        cost = _cost;
        period = _period;
        eval = -1;
        id = _id;
    }
    int source, dest, time, cost, period, id;
    ull eval;
};

int n, m, A, B;

vector<vector<Train>> trainsFrom;


ull findPath(int city, int time, set<int>& visited){

    if (city == n) return 0;

    ull bestCost = ULLONG_MAX;
    Train bestTrain(1,1,1,1,1,1);
    visited.insert(city);

    for (auto &train : trainsFrom[city]){
        if (visited.find(train.dest) != visited.end()) continue;

        if (train.eval == -1){
            ull trainCost = findPath(train.dest, time + train.time,  visited);
            train.eval = trainCost + A * train.time + B * train.cost;
        }
        
        ull waitCost = (time % train.period) * A;

        if (train.eval + waitCost < bestCost){
            bestCost = train.eval + waitCost;
            bestTrain = train;
        }
        
    }
    visited.erase(city);
    return bestCost;
}


void traversePath(int city, int time, set<int>& visited){

    if (city == n) return;

    ull bestCost = ULLONG_MAX;
    Train bestTrain(1,1,1,1,1,1);
    visited.insert(city);

    for (auto &train : trainsFrom[city]){
        if (visited.find(train.dest) != visited.end()) continue;

        ull waitCost = (time % train.period) * A;

        if (train.eval + waitCost < bestCost){
            bestCost = train.eval + waitCost;
            bestTrain = train;
        }
        
    }
    cout << bestTrain.id << ' ';
    traversePath(bestTrain.dest, time + bestTrain.time, visited);
    visited.erase(city);
}



// n, m, A, B = [int(x) for x in input().split()]


// trainsFrom = [[] for i in range(n + 1)]

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m >> A >> B;

    trainsFrom.resize(n + 1);

    int source, dest, time, cost, period, id;

    for(int i = 0; i < m; i++){
        cin >> source >> dest >> time >> cost >> period;
        
        if (source != dest) 
            trainsFrom[source].push_back(Train(source, dest, time, cost, period, i + 1));

    }
    set<int> visited;
    visited.insert(1);

    findPath(1, 0, visited);

    // cout << costOf << endl;
    traversePath(1, 0, visited);

    // for(auto a: bestFrom){
    //     cout << a.first << ' ' << a.second << endl;
    // }

    // while(currCity != n){
    //     cout << bestTrainFrom[currCity].id << ' ';
    //     currCity = bestTrainFrom[currCity].dest;
    // }
    
    cout << endl;

}