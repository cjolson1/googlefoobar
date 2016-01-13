"""
Solution for origins_and_order
Thoughts:
- Year could be any value. Month is 1-12. Day depends on month.
- Ambiguity could be between month/day (two values <= 12) or day/year (two values <= # of days in month)
- Corner case: If two values are equal, then they are not ambiguous (since they have the same string representation). E.g., "02/28/28"
- I could use Calendar but since it *does* take leap years into account then the answers will actually be wrong for some times.
"""
limit = {
    1: 31,
    2: 27,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def answer(x, y, z):
    nums = sorted([x, y, z])
    first = int(nums[0])
    second = int(nums[1])
    third = int(nums[2])
    valid = False
    if first < 13 and not first == 0:
        if second == first:
            month = first
            day = first
            if third > limit[first]:
                year = third
                valid = True
            elif third == first:
                year = first
                valid = True
            else:
                return "Ambiguous"
        elif second in range(limit[first] + 1):
            month = first
            day = second
            if second == third and second > 12:
                year = second
                valid = True
            elif second > 12 and third not in range(limit[first] + 1):
                valid = True
                year = third
            elif third in range(limit[first] + 1):
                return "Ambiguous"
            else:
                return "Ambiguous"
    elif first == 0:
        year = first
        if second < 13 and third < 13:
            if second in range(limit[third] + 1) and third not in range(limit[second] + 1):
                day = second
                month = third
                valid = True
            elif second not in range(limit[third] + 1) and third in range(limit[second] + 1):
                day = third
                month = second
                valid = True
            elif second == third and second in range(limit[second] + 1):
                valid = True
                month = second
                day = second
            else:
                return "Ambiguous"
        elif second < 13 and third > 12:
            valid = True
            month = second
            day = third
        else:
            return "Ambiguous"
    else:
        return 'Ambiguous'
    if valid:
        if year < 10:
            year = '0' + str(year)
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        return str(month) + '/' + str(day) + '/' + str(year)
