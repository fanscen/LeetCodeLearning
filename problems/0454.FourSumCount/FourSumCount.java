import java.util.HashMap;
import java.util.Map;

class FourSumCount {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        // 使用哈希表存储前两个数组元素和的频率
        Map<Integer, Integer> countAB = new HashMap<>();
        for (int a : nums1) {
            for (int b : nums2) {
                countAB.put(a + b, countAB.getOrDefault(a + b, 0) + 1);
            }
        }
        
        // 统计后两个数组元素和的相反数在哈希表中的出现次数
        int result = 0;
        for (int c : nums3) {
            for (int d : nums4) {
                int target = -(c + d);
                if (countAB.containsKey(target)) {
                    result += countAB.get(target);
                }
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {-2, -1};
        int[] nums3 = {-1, 2};
        int[] nums4 = {0, 2};
        System.out.println(new FourSumCount().fourSumCount(nums1, nums2, nums3, nums4));

        int[] nums5 = {0};
        int[] nums6 = {0};
        int[] nums7 = {0};
        int[] nums8 = {0};
        System.out.println(new FourSumCount().fourSumCount(nums5, nums6, nums7, nums8));
    }
}