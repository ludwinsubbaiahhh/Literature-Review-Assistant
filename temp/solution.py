
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            num_to_index[num] = i

# Test cases
solution = Solution()
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
]

results = [solution.twoSum(nums, target) for nums, target in test_cases]

# Print results
for i, result in enumerate(results):
    print(f"Test Case {i+1}: {result}")