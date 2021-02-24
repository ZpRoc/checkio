# ---------------------------------------------------------------- #

# Sort by Extension
#   Sort files by extension

# ---------------------------------------------------------------- #

# You are given a list of files. You need to sort this list by the file 
# extension. The files with the same extension should be sorted by name.

# Some possible cases:
#   Filename cannot be an empty string;
#   Files without the extension should go before the files with one;
#   Filename ".config" has an empty extension and a name ".config";
#   Filename "config." has an empty extension and a name "config.";
#   Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
#   Filename ".imp.xls" has an extension "xls" and a name ".imp".

# Input: A list of filenames.
# Output: A list of filenames.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    files.sort(key = lambda x: (x.rsplit('.', 1)[1] if x.rsplit('.', 1)[0] != '' else '', x.rsplit('.', 1)[0]))
    return files


def sort_by_ext_1(files: List[str]) -> List[str]:
    # your code here
    ### file = fn + ex
    files_info = []
    for file in files:
        fn = '.'.join(file.split('.')[0:-1])
        ex = file.split('.')[-1]

        if not fn:
            fn = '.' + ex
            ex = ''
            files_info.append([fn, ex, True])
        else:
            files_info.append([fn, ex, False])

    ### sort
    files_sort = sorted(files_info, key = lambda x: [x[1], x[0]])

    return ['.'.join(x[0:2]).rstrip('.') if x[2] else '.'.join(x[0:2]) for x in files_sort]


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")

