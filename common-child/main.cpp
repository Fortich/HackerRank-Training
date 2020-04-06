#include <bits/stdc++.h>

using namespace std;

int commonChild(string s1, string s2) {
    vector<vector<int>> mem(s1.length()+1, vector<int>(s1.length()+1));
    for (int i = 0; i < s1.length(); i++) {
        for (int j = 0; j < s1.length(); j++){
            if(s1[i]==s2[j]){
                mem[i+1][j+1] = mem[i][j] + 1;
            } else {
                mem[i+1][j+1] = max(mem[i][j+1],mem[i+1][j]);
            }
        }
    }
    return mem[s1.length()][s1.length()];
}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = commonChild(s1, s2);

    fout << result << "\n";

    fout.close();

    return 0;
}
