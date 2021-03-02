# ---------------------------------------------------------------- #

# Ryerson Letter Grade
#   Calculate the letter grade that would appear in the Ryerson's grade transcript.
#   (Number, sparsing)

# ---------------------------------------------------------------- #

# Given the grade percentage for the course, calculate and return the 
# letter grade that would appear in the Ryerson’s grade transcript, 
# as defined on the page Ryerson Grade Scales. The letter grade should 
# be returned as a string that consists of the uppercase letter followed 
# by the possible modifier "+" or "-" .

# Input: Int. Grade percentage.
# Output: Str. The letter grade.
# Precondition: argument can be from 0 to 150

# The mission was taken from Python CCPS 109 Fall 2018. It is taught 
# for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

TABLE = '''
A 85-89%
A- 80-84%
B+ 77-79%
B 73-76%
B- 70-72%
C+ 67-69%
C 63-66%
C- 60-62%
D+ 57-59%
D 53-56%
D- 50-52%
'''


def ryerson_letter_grade(score) -> str:
    table  = TABLE[0:1] + 'A+ 90-150%' + '\n' + TABLE[1:] + 'F 0-49%'
    grades = [[str.split(' ')[0], str.split(' ')[1].split('-')[0], str.split(' ')[1].split('-')[1][:-1]] 
                    for str in table.strip('\n').split('\n')]
    for grade in grades:
        if int(grade[1]) <= score <= int(grade[2]):
            return grade[0]


def ryerson_letter_grade_1(pct: int) -> str:
    # your code here
    while True:
        if pct > 89:
            return 'A+'
        elif pct < 50:
            return 'F'
        else:
            i_pct = TABLE.find(str(pct))
            if(i_pct < 0):  
                pct -= 1
                continue

            i_n = TABLE.find('\n', max(i_pct-8, 0))
            i_s = TABLE.find(' ',  max(i_pct-8, 0))

            return TABLE[i_n+1:i_s]


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(ryerson_letter_grade(45))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    assert ryerson_letter_grade(83) == "A-"
    assert ryerson_letter_grade(89) == "A"
    print("Coding complete? Click 'Check' to earn cool rewards!")

