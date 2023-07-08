class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int steps = 0, k = capacity;
        for (int i = 0; i < plants.size(); ++i){
            if (plants[i] <= k){
                ++steps;
                k -= plants[i];
            }else{
                steps += 2 * i;
                k = capacity;
                --i;
            }
        }
        return steps;
    }
};