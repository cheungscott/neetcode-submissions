class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0 : 1}
        res = 0
        total = 0
        for n in nums:
            total += n
            diff = total - k

            res += prefixSums.get(diff, 0)
            prefixSums[total] = prefixSums.get(total, 0) + 1
        return res