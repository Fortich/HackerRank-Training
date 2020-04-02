#include <bits/stdc++.h>

using namespace std;

int sherlockAndAnagrams(string s) {
    map<string, int> anagrams_string;
    for(int i = 1; i < s.size(); i++){
        for (int j = 0; j < s.size()-(i-1); j++){
            for (int k = j + 1; k < s.size()-(i-1); k++){
                string substring1 = s.substr(j, i);
                string substring2 = s.substr(k, i);
                sort(substring1.begin(), substring1.end());
                sort(substring2.begin(), substring2.end());
                bool equal = true;
                for(int i = 0; i < substring1.size(); i++){
                    if(substring1[i] != substring2[i]){
                        equal = false;
                        break;
                    }
                }
                if(equal){
                    anagrams_string[substring1]++;
                }
            }
        }
    }
    int count = 0;
    for(auto const& imap: anagrams_string){
        count += imap.second;
    }
        
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        int result = sherlockAndAnagrams(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
