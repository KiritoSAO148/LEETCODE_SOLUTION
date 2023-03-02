class Solution {
public:
    vector<int> runningSum(vector<int>& a) {
        int n = a.size();
        vector<int>res(n);
        res[0] = a[0];
        for (int i = 1; i < n; ++i) res[i] = res[i - 1] + a[i];
        return res;
    }
};