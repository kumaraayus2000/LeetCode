class Solution:

    def solve(self,index,digits,mp,curr,ans):
        if index==len(digits):
            ans.append(curr)
            return
        
        letters = mp[digits[index]]

        for i in range(len(letters)):
            self.solve(index+1,digits,mp,curr+letters[i],ans)
            

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []

        mp = {}
        mp["2"] = "abc"
        mp["3"]= "def"
        mp["4"] = "ghi"
        mp["5"] = "jkl"
        mp["6"] = "mno"
        mp["7"] = "pqrs"
        mp["8"] = "tuv"
        mp["9"] = "wxyz"

        ans = []
        self.solve(0,digits,mp,"",ans)
        return ans