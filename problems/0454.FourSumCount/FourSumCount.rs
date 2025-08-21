use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn four_sum_count(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>, nums4: Vec<i32>) -> i32 {
        // 使用哈希表存储前两个数组元素和的频率
        let mut count_ab = HashMap::new();
        for &a in &nums1 {
            for &b in &nums2 {
                *count_ab.entry(a + b).or_insert(0) += 1;
            }
        }
        
        // 统计后两个数组元素和的相反数在哈希表中的出现次数
        let mut result = 0;
        for &c in &nums3 {
            for &d in &nums4 {
                let target = -(c + d);
                if let Some(&count) = count_ab.get(&target) {
                    result += count;
                }
            }
        }
        
        result
    }
}

fn main() {
    let nums1 = vec![1, 2];
    let nums2 = vec![-2, -1];
    let nums3 = vec![-1, 2];
    let nums4 = vec![0, 2];
    
    let result = Solution::four_sum_count(nums1, nums2, nums3, nums4);
    println!("{}", result);
}