class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            if l > r:
                return -1
            pointer = (r + l) // 2
            if nums[pointer] == target:
                return pointer
            elif nums[pointer] < target:
                return binarySearch(pointer + 1, r)
            else:
                return binarySearch(l, pointer - 1)
        return binarySearch(0, len(nums) - 1)
                