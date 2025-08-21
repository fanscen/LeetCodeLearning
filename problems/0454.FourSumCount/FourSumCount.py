class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        计算四个数组中各取一个元素，使得四元素之和为0的组合数量
        
        Args:
            nums1, nums2, nums3, nums4: 四个长度相同的整数数组
            
        Returns:
            int: 满足条件的四元组数量
        """
        # 使用字典存储前两个数组元素和的频率
        count_ab = {}
        for a in nums1:
            for b in nums2:
                count_ab[a + b] = count_ab.get(a + b, 0) + 1
        
        # 统计后两个数组元素和的相反数在字典中的出现次数
        result = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count_ab:
                    result += count_ab[target]
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
    print(s.fourSumCount([0], [0], [0], [0]))