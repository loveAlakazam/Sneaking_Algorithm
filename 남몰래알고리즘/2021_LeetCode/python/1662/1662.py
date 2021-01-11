class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        w1= ''.join(word1)
        w2= ''.join(word2)
        
        if w1==w2:
            return True
        return False