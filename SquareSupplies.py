"""
Square supplies
===============

With the zombie cure injections ready to go, it’s time to start treating our zombified rabbit friends (known as zombits) at our makeshift zombit treatment center. You need to run out really fast to buy some gauze pads but you only have 30 seconds before you need to be back.

Luckily, the corner store has unlimited gauze pads in squares of all sizes. Jackpot! The pricing is simple – a square gauze pad of size K x K costs exactly K * K coins. For example, a gauze pad of size 3×3 costs 9 coins.

You’re in a hurry and the cashier takes a long time to process each transaction. You decide the fastest way to get what you need is to buy as few gauze pads as possible, while spending all of your coins (you can always cut up the gauze later if you need to). Given that you have n coins, what’s the fewest number of gauze pads you can buy?

Write a method answer(n), which returns the smallest number of square gauze pads that can be bought with exactly n coins.

n will be an integer, satisfying 1 <= n <= 10000.
"""
#The basic idea of this program is to take the int(sqrt(n)) or flooring the squareroot which provides the length of the size of the gauze
#that you need. then you subtract this value squared from the initial squared value and repeat the process, until the remaining value is 0.
#I had to use round(square**2) because python oftentimes won't return the exact value of squareroots.
from math import sqrt
def answer(n):
    count = 0
    squared = n
    square = sqrt(n)
    while square > 0:
        count += 1
        sub = int(square)
        square = sqrt(squared - sub**2)
        squared = round(square**2)
    return count
