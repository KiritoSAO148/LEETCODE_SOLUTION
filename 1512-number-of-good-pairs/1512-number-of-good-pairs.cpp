class Solution {
public:
    int last (vector<int>& a, int l, int r, int x){
        int res = -1;
        while (l <= r){
            int m = (l + r) / 2;
            if (a[m] == x){
                res = m;
                l = m + 1;
            }
            else if (a[m] > x) r = m - 1;
            else l = m + 1;
        }
        return res;
    }
    
    int numIdenticalPairs(vector<int>& a) {
        int cnt = 0, n = a.size();
        sort(a.begin(), a.end());
        for (int i = 0; i < n - 1; ++i){
            int res = last(a, i + 1, n - 1, a[i]);
            if (res != -1) cnt += res - i;
        }
        return cnt;
    }
};