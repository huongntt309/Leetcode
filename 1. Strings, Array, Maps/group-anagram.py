# https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=2nlt4w25
# # Medium

# Solution 1:
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        gr_counter = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))  # Hashable!
            gr_counter[key].append(s)
        print(gr_counter)
        res = [value for key, value in gr_counter.items()]
        print(res)
        return res
    
# SOLUTION 2:
""" 
nhận xét bài toán có constraints
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
Quan sát: Vì strs[i].length <= 100, thì có thể dùng sort để sort lại string, dùng kết quả sorted string làm key. Độ phức tạp sort là nlogn với n < 100 thì không đáng kể.
TIME COMPLEXITY: O(n * klogk) 
 - n là số lượng string trong strs
 - k là độ dài của string lớn nhất trong strs.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        gr_str = defaultdict(list)
        for s in strs:
            # convert string -> list character
            s_cop = list(s)
            # sort list char, inplace: change the var, return None
            s_cop.sort()
            # concatenate sorted character to 1 string
            s_cop_sorted = ''.join(s_cop)
            # use the sorted character to be the key of dict, value is string
            gr_str[s_cop_sorted].append(s)
        return gr_str.values()