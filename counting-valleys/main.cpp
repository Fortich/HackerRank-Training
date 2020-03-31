#include <bits/stdc++.h>

using namespace std;

int countingValleys(int n, string s) {
    int position = 0;
    int valleys = 0;
    for (int i = 0; i < s.length(); i ++){
        if(s[i]=='D' && position == 0){
            valleys++;
        }
        position = position + (s[i] == 'U' ? 1 : -1);
    }
    return valleys;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
