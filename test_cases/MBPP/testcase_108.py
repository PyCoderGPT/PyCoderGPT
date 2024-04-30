from case_MBPP_108 import all_Bits_Set_In_The_Given_Range


def check(candidate):
    assert candidate(4,1,2) == True
    assert candidate(17,2,4) == True
    assert candidate(39,4,6) == False

if __name__ == '__main__':
    check(all_Bits_Set_In_The_Given_Range)