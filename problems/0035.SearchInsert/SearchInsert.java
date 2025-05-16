public class SearchInsert {
    public int searchInsert(int[] nums, int target) {
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
        return left; // 返回应该插入的位置
    }
    
    public static void main(String[] args) {
        SearchInsert solution = new SearchInsert();
        
        // 测试用例1: 目标值在数组中
        int[] nums1 = {1, 3, 5, 6};
        int target1 = 5;
        System.out.println("输入: nums = " + java.util.Arrays.toString(nums1) + ", target = " + target1);
        System.out.println("输出: " + solution.searchInsert(nums1, target1)); // 预期输出: 2
        
        // 测试用例2: 目标值不在数组中，应插入到中间位置
        int[] nums2 = {1, 3, 5, 6};
        int target2 = 2;
        System.out.println("输入: nums = " + java.util.Arrays.toString(nums2) + ", target = " + target2);
        System.out.println("输出: " + solution.searchInsert(nums2, target2)); // 预期输出: 1
        
        // 测试用例3: 目标值不在数组中，应插入到末尾
        int[] nums3 = {1, 3, 5, 6};
        int target3 = 7;
        System.out.println("输入: nums = " + java.util.Arrays.toString(nums3) + ", target = " + target3);
        System.out.println("输出: " + solution.searchInsert(nums3, target3)); // 预期输出: 4
        
        // 测试用例4: 目标值不在数组中，应插入到开头
        int[] nums4 = {1, 3, 5, 6};
        int target4 = 0;
        System.out.println("输入: nums = " + java.util.Arrays.toString(nums4) + ", target = " + target4);
        System.out.println("输出: " + solution.searchInsert(nums4, target4)); // 预期输出: 0
        
        // 测试用例5: 空数组
        int[] nums5 = {};
        int target5 = 5;
        System.out.println("输入: nums = " + java.util.Arrays.toString(nums5) + ", target = " + target5);
        System.out.println("输出: " + solution.searchInsert(nums5, target5)); // 预期输出: 0
    }
}
