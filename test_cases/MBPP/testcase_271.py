from case_MBPP_271 import Find_Max_Length


def check(candidate):
    assert candidate([[1],[1,4],[5,6,7,8]]) == 4
    assert candidate([[0,1],[2,2,],[3,2,1]]) == 3
    assert candidate([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5

if __name__ == '__main__':
    check(Find_Max_Length)