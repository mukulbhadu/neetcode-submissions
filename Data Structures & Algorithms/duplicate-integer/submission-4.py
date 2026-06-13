class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        brr=set()
        for i in nums:
            if i in brr:
                return True
            brr.add(i)
        return False