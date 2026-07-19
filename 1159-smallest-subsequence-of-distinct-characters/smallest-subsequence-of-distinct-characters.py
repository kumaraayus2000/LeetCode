class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = {}
        used = {}

        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch] = 1

        ans = []

        for ch in s:
            freq[ch] -= 1

            if ch in used and used[ch]:
                continue

            while ans and ch < ans[-1] and freq[ans[-1]]>0:
                used[ans[-1]] =False
                ans.pop()

            ans.append(ch)
            used[ch] = True

        return "".join(ans)