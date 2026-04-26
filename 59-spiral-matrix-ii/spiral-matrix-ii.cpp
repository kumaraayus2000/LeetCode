class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
       int l1=0;
        vector<vector<int>> v1(n, vector<int>(n, 0));
        int n1 = n-1;
        int m1 = n-1;
        int left =0;
        int right = m1;
        int top = 0;
        int bottom = n1;

        while(left<=right && top<=bottom){

            for(int i=left;i<=right;i++){
                l1=l1+1;
                v1[top][i]=l1;
            }
            top++;

            for(int i=top;i<=bottom;i++){
                l1=l1+1;
                v1[i][right]=l1;
            }
            right--;

            if(top<=bottom){
            for(int i=right;i>=left;i--){
                l1=l1+1;
                v1[bottom][i]=l1;
            }
            bottom--;
            }

            if(left<=right){
                for(int i=bottom;i>=top;i--){
                    l1=l1+1;
                    v1[i][left]=l1;
                }
                left++;
            }
        }

    return v1;

    }
};