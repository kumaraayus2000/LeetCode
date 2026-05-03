class Solution {
public:


    void solve(int x, vector<int>& candidates, int target,vector<int>&v1,vector<vector<int>>&v2){

            if(target==0){
                v2.push_back(v1);
                return;
            }
          

                for(int i=x;i<candidates.size();i++){
                      if(candidates[i]<=target){
                    v1.push_back(candidates[i]);
                    solve(i,candidates,target-candidates[i],v1,v2);
                    v1.pop_back();
                    }
                }
            

    }


    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        vector<vector<int>>v2;
        vector<int>v1;

        solve(0,candidates,target,v1,v2);
        return v2;
    }
};