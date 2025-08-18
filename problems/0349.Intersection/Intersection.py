class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        返回两个数组的交集，结果中的每个元素必须是唯一的。
        
        Args:
            nums1: List[int] - 第一个整数数组
            nums2: List[int] - 第二个整数数组
            
        Returns:
            List[int] - 交集数组，元素唯一
        """
        # 使用集合去重并求交集
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = solution.intersection(nums1, nums2)
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result}")
    
    # 测试用例2
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = solution.intersection(nums1, nums2)
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result}")
    
    # 额外测试用例
    nums1 = []
    nums2 = [1, 2, 3]
    result = solution.intersection(nums1, nums2)
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result}")
    
    nums1 = [1, 2, 3]
    nums2 = []
    result = solution.intersection(nums1, nums2)
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result}")