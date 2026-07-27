class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsHash = {}

        for n in range(len(strs)):
            strsHash.setdefault(tuple(sorted(strs[n])), []).append(strs[n])
        return list(strsHash.values())
