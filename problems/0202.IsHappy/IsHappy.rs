use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut seen = HashSet::new();
        let mut current = n;
        
        while current != 1 && !seen.contains(&current) {
            seen.insert(current);
            current = Self::get_next(current);
        }
        
        current == 1
    }
    
    fn get_next(num: i32) -> i32 {
        let mut total = 0;
        let mut n = num;
        
        while n > 0 {
            let digit = n % 10;
            total += digit * digit;
            n /= 10;
        }
        
        total
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_happy() {
        assert_eq!(Solution::is_happy(19), true);
        assert_eq!(Solution::is_happy(2), false);
    }
}

fn main() {
    // 测试用例1: n = 19
    let result1 = Solution::is_happy(19);
    println!("is_happy(19) = {}", result1); // 应该输出 true
    
    // 测试用例2: n = 2
    let result2 = Solution::is_happy(2);
    println!("is_happy(2) = {}", result2); // 应该输出 false
    
    // 额外测试用例: n = 1
    let result3 = Solution::is_happy(1);
    println!("is_happy(1) = {}", result3); // 应该输出 true
    
    // 额外测试用例: n = 7
    let result4 = Solution::is_happy(7);
    println!("is_happy(7) = {}", result4); // 应该输出 true
}