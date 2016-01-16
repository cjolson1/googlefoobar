/*
The sign outside reads: Name no one man.
"Escape. We must escape." Staring at the locked door of his cage, Beta Rabbit, spy and brilliant mathematician, 
has a revelation. "Of course! Name no one man - it's a palindrome! Palindromes are the key to opening this lock!"
To help Beta Rabbit crack the lock, write a function answer(n) which returns the smallest positive integer base b, 
at least 2, in which the integer n is a palindrome. The input n will satisfy "0 <= n <= 1000."
*/

public class BackwardAndForward {
    public static int answer(int n){
        int ans = 0;
        for(int i=2; i < 37; i++) {
            String pali = convToBase(n, i);
            if (pali.equals(new StringBuilder(pali).reverse().toString())) {
                ans = i;
            }
        }
        return ans;
    }

    private static String convToBase(int x, int base){
        String r = "";
        while(x>0){
            r += Integer.toString(x%base);
            x /= base;
        }
        return r;
    }
}
