class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for n in range(len(s)):
            hashS[s[n]] = 1 + hashS.get(s[n], 0)
            hashT[t[n]] = 1 + hashT.get(t[n], 0)
        
        for m in hashS:
            if hashS[m] != hashT.get(m, 0):
                return False

        return True