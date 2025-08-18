package main

import "fmt"

// intersection 返回两个数组的交集，结果中的每个元素必须是唯一的
func intersection(nums1 []int, nums2 []int) []int {
	// 使用map模拟集合去重并求交集
	set1 := make(map[int]bool)
	set2 := make(map[int]bool)

	// 将nums1中的元素添加到set1中
	for _, num := range nums1 {
		set1[num] = true
	}

	// 将nums2中的元素添加到set2中
	for _, num := range nums2 {
		set2[num] = true
	}

	// 找到交集
	var result []int
	for num := range set1 {
		if set2[num] {
			result = append(result, num)
		}
	}

	return result
}

func main() {
	// 测试用例1
	nums1 := []int{1, 2, 2, 1}
	nums2 := []int{2, 2}
	result := intersection(nums1, nums2)
	fmt.Printf("Input: nums1 = %v, nums2 = %v\n", nums1, nums2)
	fmt.Printf("Output: %v\n", result)

	// 测试用例2
	nums1 = []int{4, 9, 5}
	nums2 = []int{9, 4, 9, 8, 4}
	result = intersection(nums1, nums2)
	fmt.Printf("Input: nums1 = %v, nums2 = %v\n", nums1, nums2)
	fmt.Printf("Output: %v\n", result)

	// 额外测试用例
	nums1 = []int{}
	nums2 = []int{1, 2, 3}
	result = intersection(nums1, nums2)
	fmt.Printf("Input: nums1 = %v, nums2 = %v\n", nums1, nums2)
	fmt.Printf("Output: %v\n", result)

	nums1 = []int{1, 2, 3}
	nums2 = []int{}
	result = intersection(nums1, nums2)
	fmt.Printf("Input: nums1 = %v, nums2 = %v\n", nums1, nums2)
	fmt.Printf("Output: %v\n", result)
}
