class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int ans = 0;
        while (k--){
            int top = nums.back();
            ans += top;
            nums.pop_back();
            nums.push_back(top + 1);
        }
        return ans;
    }
};