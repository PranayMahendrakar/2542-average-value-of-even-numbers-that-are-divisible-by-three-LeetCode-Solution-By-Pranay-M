class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # Even and divisible by 3 means divisible by 6
        valid = [n for n in nums if n % 6 == 0]
        return sum(valid) // len(valid) if valid else 0