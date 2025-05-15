import java.util.Arrays; // 需要导入 Arrays 类

class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; // 防止整数溢出，更稳健的 mid 计算方式
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1; // 未找到目标值
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 测试用例1: 目标值在数组中
        int[] nums1 = {-1, 0, 3, 5, 9, 12};
        int target1 = 9;
        System.out.println("Input: nums = " + Arrays.toString(nums1) + ", target = " + target1);
        System.out.println("Output: " + sol.search(nums1, target1)); // 预期输出: 4

        // 测试用例2: 目标值不在数组中
        int[] nums2 = {-1, 0, 3, 5, 9, 12};
        int target2 = 2;
        System.out.println("Input: nums = " + Arrays.toString(nums2) + ", target = " + target2);
        System.out.println("Output: " + sol.search(nums2, target2)); // 预期输出: -1

        // 测试用例3: 空数组
        int[] nums3 = {};
        int target3 = 5;
        System.out.println("Input: nums = " + Arrays.toString(nums3) + ", target = " + target3);
        System.out.println("Output: " + sol.search(nums3, target3)); // 预期输出: -1

        // 测试用例4: 目标值在数组头部
        int[] nums4 = {5, 7, 8, 10, 12};
        int target4 = 5;
        System.out.println("Input: nums = " + Arrays.toString(nums4) + ", target = " + target4);
        System.out.println("Output: " + sol.search(nums4, target4)); // 预期输出: 0

        // 测试用例5: 目标值在数组尾部
        int[] nums5 = {5, 7, 8, 10, 12};
        int target5 = 12;
        System.out.println("Input: nums = " + Arrays.toString(nums5) + ", target = " + target5);
        System.out.println("Output: " + sol.search(nums5, target5)); // 预期输出: 4
        
        // 测试用例6: 数组中只有一个元素，且为目标值
        int[] nums6 = {5};
        int target6 = 5;
        System.out.println("Input: nums = " + Arrays.toString(nums6) + ", target = " + target6);
        System.out.println("Output: " + sol.search(nums6, target6)); // 预期输出: 0

        // 测试用例7: 数组中只有一个元素，但不是目标值
        int[] nums7 = {5};
        int target7 = 3;
        System.out.println("Input: nums = " + Arrays.toString(nums7) + ", target = " + target7);
        System.out.println("Output: " + sol.search(nums7, target7)); // 预期输出: -1
    }
}