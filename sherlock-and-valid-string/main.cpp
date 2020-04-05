#include <bits/stdc++.h>

using namespace std;

string isValid(string s) {
    int i;
    vector<int> letters(26);
    for(i = 0; i < s.length(); i++){
        letters[s[i]-97]++;
    }
    int actual = 0;
    bool flag = true;
    for(i = 0; i < 26; i++){
        if(letters[i] != actual){
            if(letters[i] == 0){
                continue;
            } else {
                if(actual == 0){
                    actual = letters[i];
                } else {
                    if(int(abs(letters[i] - actual))==1){
                        if(flag){
                            flag = false;
                        } else {
                            return "NO";
                        }
                    } else {
                        if(letters[i] == 1){
                            if(flag){
                                flag = false;
                            } else {
                                return "NO";
                            }
                        } else  {
                            return "NO";
                        }
                    }
                }
            }
        }
    }
    return "YES";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = isValid(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
