class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums) - 1):
            for z in range(i + 1, len(nums)):
                if nums[z] == (target - nums[i]):
                    res.append(i)
                    res.append(z)
                    res.sort()
                    return res