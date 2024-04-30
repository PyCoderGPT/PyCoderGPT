from case_MBPP_068 import string_to_list


def check(candidate):
    assert candidate("python programming")==['python','programming']
    assert candidate("lists tuples strings")==['lists','tuples','strings']
    assert candidate("write a program")==['write','a','program']

if __name__ == '__main__':
    check(string_to_list)