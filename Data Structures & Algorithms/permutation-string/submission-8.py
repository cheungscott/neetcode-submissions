class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts1, counts2 = [0] * 26, [0] * 26
        for c in range(len(s1)):
            counts1[ord(s1[c]) - ord("a")] += 1
            counts2[ord(s2[c]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            counts2[ord(s2[r]) - ord("a")] += 1
            if counts2[ord(s2[r]) - ord("a")] == counts1[ord(s2[r]) - ord("a")]:
                matches += 1
            elif counts2[ord(s2[r]) - ord("a")] == counts1[ord(s2[r]) - ord("a")] + 1:
                matches -= 1
            
            counts2[ord(s2[l]) - ord("a")] -= 1
            if counts2[ord(s2[l]) - ord("a")] == counts1[ord(s2[l]) - ord("a")]:
                matches += 1
            elif counts2[ord(s2[l]) - ord("a")] + 1 == counts1[ord(s2[l]) - ord("a")]:
                matches -= 1
            l += 1
        return matches == 26
        