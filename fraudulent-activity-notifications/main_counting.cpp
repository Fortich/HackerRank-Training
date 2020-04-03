#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the activityNotifications function below.
int activityNotifications(vector<int> expenditure, int d) {
    vector<int> countvector(201);
    int i, j, k, l, m;
    int count = 0;
    for(i = 0; i < d; i++){
        countvector[expenditure[i]]++;
    }
    for(; i < expenditure.size(); i++){
        if(d%2){
            k = 0;
            for(j = 0; j < countvector.size(); j++){
                if(countvector[j]>0){
                    k+=countvector[j];
                    if(k == (d/2)+1 || k > (d/2)+1){
                        if(expenditure[i] >= 2*(j)){
                            count++;
                        }
                        break;
                    }
                }
            }
        } else {
            k = 0;
            l = 0;
            for(j = 0; j < countvector.size()+1; j++){
                if(countvector[j]>0){
                    k += countvector[j];
                    if((k==(d/2) || k > (d/2)) && l == 0){
                        l = j;
                    }
                    if(k==(d/2)+1 || k > (d/2)){
                        if(expenditure[i] >= (l+j)){
                            count++;
                        }
                        break;
                    }
                }
                
            }
        }
        countvector[expenditure[i]]++;
        countvector[expenditure[i-d]]--;
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
