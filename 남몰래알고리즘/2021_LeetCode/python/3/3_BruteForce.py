class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if (self.check(s,i,j)):
                    res=max(res, j-i+1)
        return res
    
    def check(self, s, start, end):
        chars=[0]*128
        for i in range(start, end+1):
            c=s[i]
            now=ord(c)
            chars[now]+=1
            if chars[now]>1 :
                return False
        return True