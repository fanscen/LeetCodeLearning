package main

import "fmt"

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	// 使用哈希表存储前两个数组元素和的频率
	countAB := make(map[int]int)
	for _, a := range nums1 {
		for _, b := range nums2 {
			countAB[a+b]++
		}
	}

	// 统计后两个数组元素和的相反数在哈希表中的出现次数
	result := 0
	for _, c := range nums3 {
		for _, d := range nums4 {
			target := -(c + d)
			if count, exists := countAB[target]; exists {
				result += count
			}
		}
	}

	return result
}

func main() {
	nums1 := []int{1, 2}
	nums2 := []int{-2, -1}
	nums3 := []int{-1, 2}
	nums4 := []int{0, 2}
	fmt.Println(fourSumCount(nums1, nums2, nums3, nums4))
}
