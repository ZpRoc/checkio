# ---------------------------------------------------------------- #

# Between Markers
#   find a substring between markers
#   (String, parsing, has-Hints)

# ---------------------------------------------------------------- #

# You are given a string and two markers (the initial and final). 
# You have to find a substring enclosed between these two markers. 
# But there are a few important conditions:
#   The initial and final markers are always different.
#   If there is no initial marker, then the first character should be considered the beginning of a string.
#   If there is no final marker, then the last character should be considered the ending of a string.
#   If the initial and final markers are missing then simply return the whole string.
#   If the final marker comes before the initial marker, then return an empty string.

# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
# Output: A string.
# Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    i_s = text.find(begin) + len(begin) if begin in text else None
    i_e = text.find(end) if end in text else None
    return text[i_s:i_e]


def between_markers_1(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    i_s = text.find(begin)
    i_e = text.find(end)

    if i_s == -1 and i_e == -1:
        return text
    else:
        if i_s == -1:
            return text[:i_e]
        elif i_e == -1:
            return text[i_s+len(begin):]
        elif i_s >= i_e:
            return ''
        else:
            return text[i_s+len(begin):i_e]


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

