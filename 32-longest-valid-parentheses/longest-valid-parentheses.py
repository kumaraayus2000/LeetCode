class Solution:
    def longestValidParentheses(self, s: str) -> int:

        s1 =[]

        s1.append(-1)
        maxi=0

        for s2 in range(len(s)):
            if s[s2] =='(':
                s1.append(s2)
            else:
                s1.pop()
                if len(s1)==0:
                    s1.append(s2)
                else:
                    maxi = max(maxi,s2-s1[-1])

        return maxi