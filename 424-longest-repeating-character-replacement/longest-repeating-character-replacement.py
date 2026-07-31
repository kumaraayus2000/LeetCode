class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mp = {}

        r = 0
        maxfreq = 0
        l = 0
        maxlen = 0
        while r < len(s):
            mp[s[r]] = mp.get(s[r],0) +1
            maxfreq = max(maxfreq,mp[s[r]])
            while (r-l)+1 - maxfreq > k:
                mp[s[l]]-=1
                l+=1

            maxlen = max(maxlen, (r-l)+1)
            r+=1

        return maxlen



        