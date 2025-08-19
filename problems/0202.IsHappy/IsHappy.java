import java.util.HashSet;
import java.util.Set;

class IsHappy {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        
        while (n != 1 && !seen.contains(n)) {
            seen.add(n);
            n = getNext(n);
        }
        
        return n == 1;
    }
    
    private int getNext(int num) {
        int total = 0;
        while (num > 0) {
            int digit = num % 10;
            total += digit * digit;
            num /= 10;
        }
        return total;
    }

    public static void main(String[] args) {
        IsHappy ih = new IsHappy();
        System.out.println(ih.isHappy(19));
    }
}