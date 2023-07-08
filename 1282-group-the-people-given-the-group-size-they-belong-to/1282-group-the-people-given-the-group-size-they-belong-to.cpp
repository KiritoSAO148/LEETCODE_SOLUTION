class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> ans;
        unordered_map<int, vector<int>> mp;
        
        for (int i = 0; i < groupSizes.size(); ++i){
            int key = groupSizes[i];
            if (mp.count(key)) mp[key].push_back(i);
            else mp[key] = vector<int>{i};
            if (mp[key].size() == groupSizes[i]){
                ans.push_back(mp[key]);
                mp.erase(key);
            }
        }
        
        return ans;
    }
};