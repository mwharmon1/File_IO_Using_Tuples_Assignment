"""
Author: Michael Harmon
Date: 10/9/2019
Description: This program will create, open and write to a file.
"""


def write_to_file(my_scores):
    """
    opens, writes to and closes a file
    :param my_scores: user input of kwargs and scores
    :return: none
    """
    with open('student_info.txt', 'a') as f:
        f.writelines(str(my_scores) + "\n")
        f.close()


def get_student_info(**kwargs):
    """
    prompts for scores input by user and passes input to write_to_file function
    :param kwargs: users name
    :return: none
    """
    for key, value in kwargs.items():
        print("Hello " + value)
    score = 0
    sentinel = -1
    my_scores = [kwargs]
    while score >= 0:
        try:
            score = float(input("Enter a score or -1 to exit: "))
        except ValueError:
            print("Numbers only.")
        else:
            if score == int(sentinel):
                break
            else:
                my_scores.append(score)
    write_to_file(my_scores)


def read_from_file():
    """
    reads from and closes the file
    :return: none
    """
    with open('student_info.txt', 'r') as f:
        for line in f:
            print(line)
        f.close()


if __name__ == '__main__':
    get_student_info(name="Michael Harmon")
    get_student_info(name="Elijah Harmon")
    get_student_info(name="Dean Harmon")
    get_student_info(name="Torie Harmon")
    read_from_file()

