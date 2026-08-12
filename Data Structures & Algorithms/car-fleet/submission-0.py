class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sortedArr = []
        for i in range(len(position)):
            sortedArr.append([position[i], speed[i]])
        sortedArr.sort(reverse = True)

        for i, n in enumerate(sortedArr):
            time = (target - n[0]) / n[1]
            if stack and time > stack[-1]:
                stack.append(time)
            elif not stack:
                stack.append(time)
        return len(stack) 


