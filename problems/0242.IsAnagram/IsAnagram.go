package main

import "fmt"  // 添加这一行

func isAnagram(s string, t string) bool {
    // 如果长度不同，肯定不是异位词
    if len(s) != len(t) {
        return false
    }

    // 使用map统计字符出现次数
    charCount := make(map[rune]int)

    // 统计字符串s中每个字符的出现次数
    for _, char := range s {
        charCount[char]++
    }

    // 遍历字符串t，减少对应字符的计数
    for _, char := range t {
        charCount[char]--
        if charCount[char] == 0 {
            delete(charCount, char)
        }
    }

    // 如果所有字符都匹配，map应该为空
    return len(charCount) == 0
}

func main() {
    s := "anagram"
    t := "nagaram"
    result := isAnagram(s, t)
    fmt.Println(result)
}
