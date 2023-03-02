class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int cnt = 0;
        for (auto it : items){
            if (ruleKey == "type" && it[0] == ruleValue) ++cnt;
            else if (ruleKey == "color" && it[1] == ruleValue) ++cnt;
            else if (ruleKey == "name" && it[2] == ruleValue) ++cnt;
        }
        return cnt;
    }
};