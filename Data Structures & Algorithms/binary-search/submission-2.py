class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(l, r):
            if l > r:
                return -1

            mid = (l + r) // 2
            if target > nums[mid]:
                return bSearch(mid + 1, r)
            elif target < nums[mid]:
                return bSearch(l, mid - 1)
            else:
                return mid
        return bSearch(0, len(nums) - 1)
        