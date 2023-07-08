class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        unordered_map<int, int> mp1, mp2;
        for (int i = 0; i < n; ++i){
            int cnt = 0;
            for (int j = 0; j < m; ++j) cnt += grid[i][j] == 1;
            mp1[i] = cnt;
        }
        for (int i = 0; i < m; ++i){
            int cnt = 0;
            for (int j = 0; j < n; ++j) cnt += grid[j][i] == 1;
            mp2[i] = cnt;
        }
        vector<vector<int>>v;
        for (int i = 0; i < n; ++i){
            vector<int>tmp;
            for (int j = 0; j < m; ++j) tmp.push_back(mp1[i] + mp2[j] - (n - mp1[i]) - (m - mp2[j]));
            v.push_back(tmp);
        }
        return v;
    }
};