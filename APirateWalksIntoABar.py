"""
can't find the instructions for this anywhere! but essentially this problem asks for you to find the amount of pirates that form a loop
when asking about a topic because they keep referencing you to other pirates. the input is a list where the indices correspond
to number of the pirate and the value at the indice corresponds to which pirate they reference you to,
"""
def answer(numbers):
    for n in range(len(numbers)):
        reference = numbers[n]
        potential = numbers[n]
        for i in range(len(numbers)):
            reference = numbers[reference]
            if reference == potential:
                return i+1
