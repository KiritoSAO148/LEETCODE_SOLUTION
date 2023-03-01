class Solution {
public:
    int countPrimes(int n) {
        int p[n + 1];
        for (int i = 0; i <= n; ++i) p[i] = 1;
        //p[0] = p[1] = 0;
        for (int i = 2; i <= sqrt(n); ++i){
            if (p[i] == 1){
                for (int j = i * i; j <= n; j += i) p[j] = 0;
            }
        }
        int cnt = 0;
        for (int i = 2; i < n; ++i) if (p[i] == 1) ++cnt;
        return cnt;
    }
};