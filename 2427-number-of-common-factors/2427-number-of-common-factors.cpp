class Solution {
public:
    int cnt(int n){
        int c = 0;
        for (int i = 1; i <= sqrt(n); ++i){
            if (n % i == 0){
                ++c;
                if (i != n / i) ++c;
            }
        }
        return c;
    }
    int commonFactors(int a, int b) {
        int g = __gcd(a, b);
        return cnt(g);
    }
};