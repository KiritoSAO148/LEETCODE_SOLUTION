class Solution {
public:
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string code[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    
    int uniqueMorseRepresentations(vector<string>& words) {
        set<string> se;
        for (int i = 0; i < words.size(); ++i){
            string ans = "";
            for (int j = 0; j < words[i].size(); ++j){
                for (int k = 0; k < alphabet.size(); ++k){
                    if (words[i][j] == alphabet[k]){
                        ans += code[k];
                    }
                }
            }
            se.insert(ans);
        }
        return se.size();
    }
};