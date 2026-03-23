class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        
        map<int,int>mp;

        for(int i=0;i<nums.size();i++){
            mp[nums[i]]++;
        }
        vector<int>v1;
        for(int i=0;i<nums.size();i++){
            if(mp[nums[i]]>1){
                v1.push_back(nums[i]);
                mp[nums[i]]=0;
            }
        }

        return v1;

    }
};