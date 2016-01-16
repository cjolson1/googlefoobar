/*

can't find the instructions for this anywhere! but essentially this problem asks for you to find the amount of pirates that form a loop
when asking about a topic because they keep referencing you to other pirates. the input is a list where the indices correspond
to number of the pirate and the value at the indice corresponds to which pirate they reference you to,

*/
public class Answer {
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
