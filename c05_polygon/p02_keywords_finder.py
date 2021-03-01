# ---------------------------------------------------------------- #

# Keywords Finder
#   Help write a CTRL+F function for the robots
#   (Text, string)

# ---------------------------------------------------------------- #

# Sophie has found a stash books and she wants to find information 
# about the ancients who lived on the islands. Unfortunately, she 
# does not have a text search module and needs some help. Let's write 
# a program to help her search for keywords on the pages of a book.

# You are given some plain text (without tags) and a string with 
# keywords (or parts of words, or letters) separated by spaces. 
# You will need to find all the keywords and put these words into 
# "<span></span>" wrappers to highlight them for Sophie. You can 
# ignore upper or lower cases for the key words, but the original 
# letter cases in the text should remain.

# For the cases when keywords contain or intersect each other you 
# should highlight the larger word without nested span tags. Let's 
# look it with example.
#   The text "Hello World! Or LOL" and keywords "hell world or lo".
#   The word "World" contains two keywords thus we tag only larger part "<span>World</span>".
#   "Hello" contains two intersected words "hell" and "lo" and we tag the larger part again "<span>Hello</span>".
#   Be careful, a result like "<span>Hel<span>lo</span></span>" is considered wrong because it contains nested tags.

# Input: Two arguments. A text and key words as strings.
# Output: The text with wrapped key words.
# Precondition:
#       0 < len(text) < 5000
#       0 < len(the_number_of_key_words) < 30


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def checkio(text, words):
    ### Matching the words, get the span indices
    flgs = []
    for word in words.split(' '):
        # space
        if not word:    continue

        # match
        index = -1
        while True:
            index = text.lower().find(word.lower(), index + 1)
            if index >= 0:
                flgs.append([index, index+len(word)])
            else:
                break

    ### Combine flgs
    flgs = sorted(flgs)

    is_finish = True
    while is_finish:
        is_finish = False
        for i in range(len(flgs) - 1):
            if flgs[i+1][0] < flgs[i][1]:
                flgs[i][1] = max(flgs[i][1], flgs[i+1][1])
                flgs.pop(i+1)
                is_finish = True
                break

    ### Modify <span>?</span>
    start   = 0
    str_out = ''
    for flg in flgs:
        str_out += text[start:flg[0]] + '<span>' + text[flg[0]:flg[1]] + '</span>'
        start = flg[1]
    str_out += text[start:]

    return str_out


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("This is only a text example for task example.", "example") ==
            "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio("Python is a widely used high-level programming language.", "pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio("It is experiment for control groups with similar distributions.", "is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"

    assert (checkio("Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio("Hello World! Or LOL", "hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"

    assert (checkio("onetwothree", "three two one") == "<span>one</span><span>two</span><span>three</span>")

