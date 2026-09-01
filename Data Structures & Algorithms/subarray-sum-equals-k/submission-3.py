class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        prefixSums = {0 : 1}
        for n in nums:
            total += n
            diff = total - k

            res += prefixSums.get(diff, 0)
            prefixSums[total] = prefixSums.get(total, 0) + 1
        return res