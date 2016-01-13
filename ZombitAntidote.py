"""
Zombit antidote
===============
Forget flu season. Zombie rabbits have broken loose and are terrorizing Silicon Valley residents! Luckily, you've managed to steal a zombie antidote and set up a makeshift rabbit rescue station. Anyone who catches a zombie rabbit can schedule a meeting at your station to have it injected with the antidote, turning it back from a zombit to a fluffy bunny. Unfortunately, you have a limited amount of time each day, so you need to maximize these meetings. Every morning, you get a list of requested injection meetings, and you have to decide which to attend fully. If you go to an injection meeting, you will join it exactly at the start of the meeting, and only leave exactly at the end.
Can you optimize your meeting schedule? The world needs your help!
Write a method called answer(meetings) which, given a list of meeting requests, returns the maximum number of non-overlapping meetings that can be scheduled. If the start time of one meeting is the same as the end time of another, they are not considered overlapping.
meetings will be a list of lists. Each element of the meetings list will be a two element list denoting a meeting request. The first element of that list will be the start time and the second element will be the end time of that meeting request.
All the start and end times will be non-negative integers, no larger than 1000000. 
The start time of a meeting will always be less than the end time.
The number of meetings will be at least 1 and will be no larger than 100.
The list of meetings will not necessarily be ordered in any particular fashion.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
"""
#this program uses the python sorted() capability to sort the meetings by start and then end time if multiple starttimes are equal
#it then starts at each element in the ordered list and creates the longest path through the meetings that obey the above rules.
#It then returns the longest amount of meetings that could work in succession in the given schedule.
def answer(meetings):
    count = 1
    for n in range(len(meetings)):
        potential = 0
        #skip keeps track of how many elements in the list have successively been skipped because they don't work in the order of the meetings
        skip = 0
        for i in range(len(meetings[n:-1])):
            x = sorted(meetings)[n][1]
            y = sorted(meetings)[i+1][0]
            if x <= y:
                potential+=1
                n+=1+skip
                skip = 0
            else: skip += 1
        if potential > count: count = potential+1
    return count
