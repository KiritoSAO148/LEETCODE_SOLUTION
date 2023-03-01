class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s = strs[0];
        int ans = INT_MAX;
        for (int i = 1; i < strs.size(); ++i){
            int j = 0;
            while (j < strs[i].size() && strs[i][j] == s[j]) ++j;
            ans = min(ans, j);
        }
        return s.substr(0, ans);
    }
};