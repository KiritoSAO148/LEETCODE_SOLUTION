class Solution {
public:
    int compress(vector<char>& v) {
        int n = v.size(), i = 0, idx = 0;
        while (i < n){
            int cnt = 1;
            while (i + cnt < n && v[i + cnt] == v[i]) ++cnt;
            v[idx++] = v[i];
            if (cnt > 1){
                for (char x : to_string(cnt)) v[idx++] = x;
            }
            i += cnt;
        }
        return idx;
    }
};