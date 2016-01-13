"""
Spy snippets
============
You've been recruited by the team building Spy4Rabbits, a highly advanced search engine used to help fellow agents
discover files and intel needed to continue the operations against Dr. Boolean's evil experiments. The team is known for
recruiting only the brightest rabbit engineers, so there's no surprise they brought you on board. While you're elbow
deep in some important encryption algorithm, a high-ranking rabbit official requests a nice aesthetic feature for the
tool called "Snippet Search."  While you really wanted to tell him how such a feature is a waste of time in this
intense, fast-paced spy organization, you also wouldn't mind  getting kudos from a leader. How hard could it be, anyway?
When someone makes a search, Spy4Rabbits shows the title of the page. Your commander would also like it to show a short
snippet of the page containing the terms that were searched for.
Write a function called answer(document, searchTerms) which returns the shortest snippet of the document, containing all
of the given search terms. The search terms can appear in any order.
The length of a snippet is the number of words in the snippet. For example, the length of the snippet "round fluffy
rabbit tails" is 4. (Hey, don't judge your colleagues for what they search in their spare time).
The document will be a string consisting only of lower-case letters [a-z] and spaces. Words in the string will be
separated by a single  space. A word could appear multiple times in the document. searchTerms will be a list of words,
each word comprised only of lower-case letters [a-z]. All the search terms will be distinct.
Search terms must match words exactly, so "hop" does not match "hopping".
Return the first sub-string if multiple sub-strings are shortest. For example, if the document is "world there hello
hello where world" and the search terms are ["hello", "world"], you must return "world there hello".
The document will be guaranteed to contain all the search terms.
The number of words in the document will be at least one, will not exceed 500, and each word will be 1 to 10 letters
long. Repeat words in  the document are considered distinct for counting purposes.
The number of words in searchTerms will be at least one, will not exceed 100, and each word will not be more than 10
letters long.
"""
def answer(document, searchTerms):
    document_split = document.split()
    order = None
    minimum = 941098042134
    term_index = {

    }
    for term in searchTerms:
        indices = [i for i, x in enumerate(document_split) if x == term]
        term_index[term] = indices
    for term in term_index.keys():
        for position in term_index[term]:
            positions = [position]
            for other_position in term_index.keys():
                distances = [int(abs(position - x)) for x in term_index[other_position]]
                positions.append(term_index[other_position][distances.index(min(distances))])
                score = max(positions) - min(positions)
            if score < minimum:
                minimum = score
                order = document_split[min(positions):max(positions)+1]
    string = ''
    for i in order:
        if not i == order[-1]:
            string += i +' '
        else:
            string += i
    return string
