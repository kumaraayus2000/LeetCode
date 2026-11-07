class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        mp = {}

        word_len = len(words[0])

        current = {}

        for word in words:
            mp[word] = mp.get(word,0) + 1

        total_words = len(words)

        res = []

        for start in range(word_len):
            left = start 
            right = start
            current = {}

            count = 0

            while right + word_len <= len(s):
                word = s[right:right+word_len]

                right += word_len
                
                if word in mp:
                    current[word] = current.get(word,0)+1
                    count+=1
                    while current[word]>mp[word]:
                        left_word = s[left:left+word_len]

                        current[left_word]-=1

                        left= left+word_len
                        count-=1

                    if count == total_words:
                        res.append(left)
                        left_word = s[left:left+word_len]
                        current[left_word]-=1
                        left+=word_len
                        count-=1
                else:
                        current = {}
                        count = 0
                        left = right
                        

        return res


