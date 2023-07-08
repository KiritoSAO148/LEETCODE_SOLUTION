class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        int n = score.size(), m = score[0].size();
        for (int i = 0; i < n - 1; ++i){
            for (int j = i + 1; j < n; ++j){
                if (score[i][k] < score[j][k]){
                    for (int l = 0; l < m; ++l){
                        swap(score[i][l], score[j][l]);
                    }
                }
            }
        }
        return score;
    }
};