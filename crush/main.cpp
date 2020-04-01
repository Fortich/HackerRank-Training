#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

struct node
{
    long value;
    int index;
    struct node *next;
    struct node *previus;
};

long arrayManipulation(int n, vector<vector<int>> queries) {
    vector<vector<int>> compiled;
    for(int i = 0; i < queries.size(); i++){
        vector<int> query1;
        vector<int> query2;
        query1.push_back(queries[i][0]);
        query1.push_back(queries[i][2]);
        query2.push_back(queries[i][1]+1);
        query2.push_back(-queries[i][2]);
        compiled.push_back(query1);
        compiled.push_back(query2);
    }
    sort(compiled.begin(), compiled.end(),
          [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[0] < b[0];
    });
    long max_long = 0;
    long count = 0;
    for (int i = 0; i < compiled.size(); i++){
        count += compiled[i][1];
        if (count > max_long && compiled[i][0] != compiled[i + 1][0]){
            max_long = count;
        }
    }
    return max_long;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nm_temp;
    getline(cin, nm_temp);

    vector<string> nm = split_string(nm_temp);

    int n = stoi(nm[0]);

    int m = stoi(nm[1]);

    vector<vector<int>> queries(m);
    for (int i = 0; i < m; i++) {
        queries[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> queries[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    long result = arrayManipulation(n, queries);

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
