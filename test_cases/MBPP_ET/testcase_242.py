from case_MBPP_242 import check_monthnumb_number


def check(candidate):
    assert candidate(5)==True
    assert candidate(2)==False
    assert candidate(6)==False
    assert candidate(5) == True
    assert candidate(1) == True
    assert candidate(4) == False
    assert candidate(1) == True
    assert candidate(8) == True
    assert candidate(3) == True
    assert candidate(2) == False
    assert candidate(5) == True
    assert candidate(4) == False
    assert candidate(9) == False
    assert candidate(10) == True
    assert candidate(2) == False
    assert candidate(5) == True
    assert candidate(7) == True
    assert candidate(6) == False
    assert candidate(7) == True
    assert candidate(7) == True
    assert candidate(4) == False
    assert candidate(3) == True
    assert candidate(5) == True
    assert candidate(3) == True
    assert candidate(6) == False
    assert candidate(3) == True
    assert candidate(1) == True
    assert candidate(3) == True
    assert candidate(5) == True
    assert candidate(4) == False
    assert candidate(8) == True
    assert candidate(9) == False
    assert candidate(9) == False
    assert candidate(3) == True
    assert candidate(3) == True
    assert candidate(8) == True
    assert candidate(3) == True
    assert candidate(6) == False
    assert candidate(4) == False
    assert candidate(2) == False
    assert candidate(6) == False
    assert candidate(7) == True
    assert candidate(6) == False
    assert candidate(6) == False
    assert candidate(6) == False
    assert candidate(6) == False
    assert candidate(6) == False
    assert candidate(2) == False
    assert candidate(4) == False
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(5) == True
    assert candidate(7) == True
    assert candidate(2) == False
    assert candidate(4) == False
    assert candidate(1) == True
    assert candidate(1) == True
    assert candidate(7) == True
    assert candidate(4) == False
    assert candidate(4) == False
    assert candidate(3) == True
    assert candidate(7) == True
    assert candidate(1) == True
    assert candidate(6) == False
    assert candidate(4) == False
    assert candidate(1) == True
    assert candidate(4) == False
    assert candidate(2) == False
    assert candidate(1) == True
    assert candidate(3) == True
    assert candidate(7) == True
    assert candidate(5) == True
    assert candidate(5) == True
    assert candidate(1) == True
    assert candidate(11) == False
    assert candidate(5) == True
    assert candidate(9) == False
    assert candidate(9) == False
    assert candidate(3) == True
    assert candidate(1) == True
    assert candidate(2) == False
    assert candidate(8) == True
    assert candidate(8) == True
    assert candidate(9) == False
    assert candidate(4) == False
    assert candidate(10) == True
    assert candidate(10) == True
    assert candidate(10) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(10) == True
    assert candidate(9) == False
    assert candidate(11) == False
    assert candidate(6) == False
    assert candidate(5) == True
    assert candidate(10) == True
    assert candidate(6) == False
    assert candidate(4) == False
    assert candidate(5) == True
    assert candidate(3) == True
    assert candidate(2) == False
    assert candidate(1) == True

if __name__ == '__main__':
    check(check_monthnumb_number)