class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>>v;
        for (int i = 0; i < n - 2; ++i){
            vector<int>tmp;
            for (int j = 0; j < n - 2; ++j){
                int res = grid[i][j];
                for (int k = 0; k < 3; ++k){
                    for (int l = 0; l < 3; ++l) res = max(res, grid[i + k][j + l]);
                }
                tmp.push_back(res);
            }
            v.push_back(tmp);
        }
        return v;
    }
};