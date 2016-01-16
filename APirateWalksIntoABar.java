public class APirateWalksIntoABar {
    public static int answer(int[] numbers){
        int ans = 0;
        for(int n = 0; n < numbers.length; n++){
            int reference = numbers[n];
            int potential = numbers[n];
            for(int i = 0; i < numbers.length; i++){
                reference = numbers[reference];
                if(reference == potential){
                    ans = i+1;
                }
            }
        }
        return ans;
    }
}
