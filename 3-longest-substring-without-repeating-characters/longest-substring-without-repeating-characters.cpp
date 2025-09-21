class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        //
        unordered_map<char,int>mp;
int l=0;
int ml=0;
        for(int i=0;i<s.length();i++){
            if(mp.find(s[i])!=mp.end() && mp[s[i]]>=l){ //make sure its not a common element){
                l= mp[s[i]]+1; //increasing the window by one if the leement exists

            }
        mp[s[i]]=i;
        ml =max(ml,i-l+1);
        }
        return ml;
    }
};