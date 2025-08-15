class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果长度不同，肯定不是异位词
        if len(s) != len(t):
            return False
        
        # 使用字典统计字符出现次数
        char_count = {}
        
        # 统计字符串s中每个字符的出现次数
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # 遍历字符串t，减少对应字符的计数
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        
        # 如果所有字符都匹配，字典应该为空
        return len(char_count) == 0
    
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))