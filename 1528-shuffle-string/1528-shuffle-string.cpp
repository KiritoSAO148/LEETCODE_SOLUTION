class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        int n = indices.size();
        vector<char>a(n);
        for (int i = 0; i < indices.size(); ++i){
            a[indices[i]] = s[i];
        }
        string ans = "";
        for (char x : a) ans += x;
        return ans;
    }
};