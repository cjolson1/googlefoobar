def answer(numbers):
    for n in range(len(numbers)):
        reference = numbers[n]
        potential = numbers[n]
        for i in range(len(numbers)):
            reference = numbers[reference]
            if reference == potential:
                return i+1
