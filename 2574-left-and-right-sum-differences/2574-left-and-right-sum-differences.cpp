class Solution {
public:
    vector<int> leftRigthDifference(vector<int>& nums) {
        int n = nums.size();
        vector<int>left(n), right(n);
        left[0] = right[0] = 0;
        for (int i = 0; i < n - 1; ++i) left[i + 1] = nums[i] + left[i];
        for (int i = 0; i < n - 1; ++i) right[i + 1] = nums[n - i - 1] + right[i];
        reverse(right.begin(), right.end());
        vector<int>ans;
        for (int i = 0; i < n; ++i) ans.push_back(abs(left[i] - right[i]));
        return ans;
    }
};