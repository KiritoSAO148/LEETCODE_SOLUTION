class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int r = 0;
        for (int i = digits.size() - 1; i >= 0; --i){
            if (digits[i] == 9){
                digits[i] = 0;
                r = 1;
            }
            else if (digits[i] != 9){
                if (r){
                    digits[i] += r;
                    r = 0;
                    break;
                }
                else {
                    ++digits[i];
                    break;
                }
            }
        }
        if (r){
            reverse(digits.begin(), digits.end());
            int res = digits[digits.size() - 1];
            if (res == 9){
                digits.push_back(0);
                digits.push_back(1);
                reverse(digits.begin(), digits.end());
            }else{
                digits.push_back(res + r);
                reverse(digits.begin(), digits.end());
            }
        }
        return digits;
    }
};