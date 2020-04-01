#include <bits/stdc++.h>

using namespace std;

string twoStrings(string s1, string s2) {
    int i;
    vector<bool> chars = vector<bool>(26);
    for(i = 0; i < s1.length(); i ++){
        if(!chars[s1[i]-97]){
            chars[s1[i]-97] = true;
        }
    }
    for(i = 0; i < s2.length(); i ++){
        if(chars[s2[i]-97]){
            return "YES";
        }
    }
    return "NO";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s1;
        getline(cin, s1);

        string s2;
        getline(cin, s2);

        string result = twoStrings(s1, s2);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
