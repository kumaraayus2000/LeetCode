class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False

        mp = {}

        for char in s:
            mp[char] = mp.get(char,0)+1

        for char in t:

            if char not in mp:
                return False
            mp[char]-=1

            if mp[char]<0:
                return False

        
        for x in mp.values():
            if x>0:
                return False

        return True

            
        