from collections import Counter 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. count the frequency of each element in nums
        count = Counter(nums)
        
        # 2. find the element with the maximum frequency
        majority_element = max(count, key=count.get)
        
        return majority_element
    
# Test cases
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # Output: 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(solution.majorityElement([1]))  # Output: 1
print(solution.majorityElement([1, 2, 3, 4, 5, 5, 5]))  # Output: 5
# Run Python File in Terminal
