from case_MBPP_080 import tup_string


def check(candidate):
    assert candidate(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
    assert candidate(('p','y','t','h','o','n'))==("python")
    assert candidate(('p','r','o','g','r','a','m'))==("program")

if __name__ == '__main__':
    check(tup_string)