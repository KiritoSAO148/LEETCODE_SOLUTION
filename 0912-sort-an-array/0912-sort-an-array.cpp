class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        map <int, int> mp;
        vector <int> res;
        for (int x : nums) mp[x]++;
        for (auto it : mp){
            for (int i = 0; i < it.second; ++i) res.push_back(it.first);
        }
        return res;
    }
};