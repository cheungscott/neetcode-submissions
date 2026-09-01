class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            seen = [0] * 26
            for c in s:
                seen[ord(c) - ord("a")] += 1
            res[tuple(seen)].append(s)
        return list(res.values())