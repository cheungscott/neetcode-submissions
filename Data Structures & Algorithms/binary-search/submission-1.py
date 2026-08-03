class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if target < nums[mid]:
                return binarySearch(l, mid - 1)
            elif target > nums[mid]:
                return binarySearch(mid + 1, r)
            else:
                return mid
        return binarySearch(0, len(nums) - 1)