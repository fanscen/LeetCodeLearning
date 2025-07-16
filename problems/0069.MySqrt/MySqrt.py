class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }
        
        int left = 2, right = x / 2;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long square = (long) mid * mid; // Use long to prevent overflow
            
            if (square == x) {
                return mid;
            } else if (square < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return right; // The largest integer whose square is less than or equal to x                                            
    }
}