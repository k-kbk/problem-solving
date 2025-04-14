def solution(nums):
    s = set(nums)
    s_len = len(s)
    nums_len = len(nums) / 2
    
    return nums_len if s_len > nums_len else s_len
