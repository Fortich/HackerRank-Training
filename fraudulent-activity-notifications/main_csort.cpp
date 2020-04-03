#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int activityNotifications(vector<int> expenditure, int d) {
    int count = 0;
    vector<int> subvector(d);
    int i, j, k, mem;
    for(i = 0; i < d; i++){
        subvector[i] = expenditure[i];
    }
    sort(subvector.begin(), subvector.end());
    for(; i < expenditure.size(); i++){
        if(d%2){
            if(expenditure[i] >= 2*(subvector[(d/2)])){
                count++;
            }
            
        } else {
            if(expenditure[i] >= 2*((subvector[(d/2)-1]+subvector[(d/2)])/2.0)){
                count++;
            }
        }
        for(j = 0; j < d; j++){
            if(subvector[j]==expenditure[i-d]){
                subvector[j]=expenditure[i];
                if(j != d-1 && subvector[j] > subvector[j+1]){
                    for(k = j; k < d - 1; k++){
                        if(subvector[k] > subvector[k+1] ) {
                            mem = subvector[k];
                            subvector[k] = subvector[k+1];
                            subvector[k + 1] = mem;
                        } else {
                            break;
                        }
                    }
                } 
                if(j != 0 && subvector[j] < subvector[j-1]) {
                    for(k = j; k > 0; k--){
                        if(subvector[k] < subvector[k-1] ){
                            mem = subvector[k];
                            subvector[k] = subvector[k-1];
                            subvector[k-1] = mem;
                        } else {
                            break;
                        }
                    }
                }
                break;
            }
        }
    }
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nd_temp;
    getline(cin, nd_temp);

    vector<string> nd = split_string(nd_temp);

    int n = stoi(nd[0]);

    int d = stoi(nd[1]);

    string expenditure_temp_temp;
    getline(cin, expenditure_temp_temp);

    vector<string> expenditure_temp = split_string(expenditure_temp_temp);

    vector<int> expenditure(n);

    for (int i = 0; i < n; i++) {
        int expenditure_item = stoi(expenditure_temp[i]);

        expenditure[i] = expenditure_item;
    }

    int result = activityNotifications(expenditure, d);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
