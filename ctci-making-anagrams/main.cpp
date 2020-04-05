#include <bits/stdc++.h>

using namespace std;

int makeAnagram(string a, string b) {
    int i, count=0;
    vector<int> letters(26);
    for(i = 0; i < a.length(); i ++){
        letters[a[i]-97]++;
    }
    for(i = 0; i < b.length(); i ++){
        letters[b[i]-97]--;
    }
    for(i=0; i < 26; i++){
        count += abs(letters[i]);
    }
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
