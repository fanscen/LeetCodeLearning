class IsAnagram {
    public boolean isAnagram(String s, String t) {
        // 如果长度不同，肯定不是异位词
        if (s.length() != t.length()) {
            return false;
        }
        
        // 使用数组统计字符出现次数（假设只包含小写字母）
        int[] charCount = new int[26];
        
        // 统计字符串s中每个字符的出现次数
        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;
        }
        
        // 遍历字符串t，减少对应字符的计数
        for (int i = 0; i < t.length(); i++) {
            charCount[t.charAt(i) - 'a']--;
            // 如果某个字符在t中出现次数超过在s中出现次数，则不是异位词
            if (charCount[t.charAt(i) - 'a'] < 0) {
                return false;
            }
        }
        
        // 检查是否所有字符计数都为0
        for (int count : charCount) {
            if (count != 0) {
                return false;
            }
        }
        
        return true;
    }

    public static void main(String[] args) {
        IsAnagram solution = new IsAnagram();
        System.out.println(solution.isAnagram("anagram", "nagaram"));
        System.out.println(solution.isAnagram("rat", "car"));
    }
}