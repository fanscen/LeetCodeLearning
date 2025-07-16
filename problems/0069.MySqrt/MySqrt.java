public class MySqrt {
    public int mySqrt(int x) {
        int left = 0, right = x, ans = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if ((long) mid * mid <= x) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        MySqrt solution = new MySqrt();
        
        int x = 8;
        int result = solution.mySqrt(x);
        System.out.println("Square root of " + x + " is: " + result);

        int x2 = 16;
        int result2 = solution.mySqrt(x2);
        System.out.println("Square root of " + x2 + " is: " + result2);
        
        int x3 = 25;
        int result3 = solution.mySqrt(x3);
        System.out.println("Square root of " + x3 + " is: " + result3);

        int x4 = 26;
        int result4 = solution.mySqrt(x4);
        System.out.println("Square root of " + x4 + " is: " + result4);
        
        int x5 = 100;
        int result5 = solution.mySqrt(x5);
        System.out.println("Square root of " + x5 + " is: " + result5);
        
    }
}