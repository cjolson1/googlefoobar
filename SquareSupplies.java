/**
 Square supplies
 ===============
 With the zombie cure injections ready to go, it’s time to start treating our zombified rabbit friends (known as zombits) at our makeshift zombit treatment center. You need to run out really fast to buy some gauze pads but you only have 30 seconds before you need to be back.
 Luckily, the corner store has unlimited gauze pads in squares of all sizes. Jackpot! The pricing is simple – a square gauze pad of size K x K costs exactly K * K coins. For example, a gauze pad of size 3×3 costs 9 coins.
 You’re in a hurry and the cashier takes a long time to process each transaction. You decide the fastest way to get what you need is to buy as few gauze pads as possible, while spending all of your coins (you can always cut up the gauze later if you need to). Given that you have n coins, what’s the fewest number of gauze pads you can buy?
 Write a method answer(n), which returns the smallest number of square gauze pads that can be bought with exactly n coins.
 n will be an integer, satisfying 1 <= n <= 10000.
 **/

public class SquareSupplies {
    public static int answer(int n){
        int count = 0;
        double squared = n;
        double square = Math.sqrt(n);
        while(square > 0){
            count += 1;
            int sub = (int) square;
            square = Math.sqrt(squared-Math.pow(sub, 2));
            squared = Math.round(Math.pow(square, 2));
        }
        return count;
    }
}
