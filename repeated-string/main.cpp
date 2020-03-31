#include <bits/stdc++.h>

using namespace std;

long repeatedString(string s, long n) {
    long m = s.length();
    long times = n/m;
    long as = 0;
    for (int i = 0; i < m; i ++){
        as += (s[i] == 'a' ? 1 : 0);
    }
    as = as*times;
    for (int i = 0; i < n%m; i++){
        as += (s[i] == 'a' ? 1 : 0);
    }
    return as;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
