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
