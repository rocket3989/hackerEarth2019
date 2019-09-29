#include<bits/stdc++.h>
using namespace std;

int main(){
    set<int> setTest;

    setTest.insert(1);
    setTest.insert(2);
    setTest.insert(3);
    setTest.insert(4);
    setTest.insert(5);

    auto start = setTest.upper_bound(6-1);
    if (start == setTest.end())
        start = setTest.begin();
    cout << *start <<endl;
}