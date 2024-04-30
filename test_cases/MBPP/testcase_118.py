from case_MBPP_118 import replace_list


def check(candidate):
    assert candidate([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert candidate([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
    assert candidate(["red","blue","green"],["yellow"])==["red","blue","yellow"]

if __name__ == '__main__':
    check(replace_list)