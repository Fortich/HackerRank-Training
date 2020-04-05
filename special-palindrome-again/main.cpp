#include <bits/stdc++.h>

using namespace std;

long substrCount(int n, string s) {
    int i, j;
    long curr, curr2, count=0;
    bool flag, flag2;
    for(i = 0; i < s.length();){
        curr = 0;
        curr2 = 0;
        flag = true;
        flag2=true;
        for(j = i; j < s.length(); j++){
            if(s[i] == s[j]){
                if(flag){
                    curr++;
                } else {
                    curr2++;
                    if(flag2){
                        count++;
                    }
                }
            } else{
                if(flag){
                    flag = !flag;
                } else {
                    break;
                }
            }
            if(curr == curr2){
                flag2 = false;
            }
        }
        count += (curr*(curr+1))/2;
        i += curr;
    }
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    long result = substrCount(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
