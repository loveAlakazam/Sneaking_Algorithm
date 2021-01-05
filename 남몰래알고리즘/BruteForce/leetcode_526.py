class Solution:
    def __init__(self):
        self.answer = 0

    def countArrangement(self, n: int) -> int:
        nums = [num for num in range(1, n + 1)]
        self.permute(nums, 0)
        return self.answer

    def permute(self, nums, l):
        if l == len(nums):
            self.answer += 1

        for i in range(l, len(nums)):
            self.swap(nums, i, l)
            if nums[l] % (l + 1) == 0 or (l + 1) % nums[l] == 0:
                self.permute(nums, l + 1)
            self.swap(nums, i, l)

    def swap(self, nums, x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp