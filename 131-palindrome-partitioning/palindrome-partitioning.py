class Solution:

    def part(self,s:str,indx:int,path:List[List[str]],result:List[List[str]]):
        if indx == len(s):
            result.append(path.copy())
            return

        for i in range(indx,len(s)):

            s1 = s[indx:i+1]

            if s1 == s1[::-1]:
                path.append(s1)

                self.part(s,i+1,path,result)
                path.pop()




    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []
        self.part(s,0,path,result)    
        return result