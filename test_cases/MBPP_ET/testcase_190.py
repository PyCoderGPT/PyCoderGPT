from case_MBPP_190 import sum_of_digits


def check(candidate):
    assert candidate([10,2,56])==14
    assert candidate([[10,20,4,5,'b',70,'a']])==19
    assert candidate([10,20,-4,5,-70])==19
    assert candidate([8, 2, 59]) == 24
    assert candidate([10, 1, 58]) == 15
    assert candidate([12, 7, 58]) == 23
    assert candidate([6, 3, 53]) == 17
    assert candidate([9, 1, 53]) == 18
    assert candidate([6, 5, 51]) == 17
    assert candidate([11, 7, 60]) == 15
    assert candidate([7, 5, 55]) == 22
    assert candidate([8, 5, 52]) == 20
    assert candidate([10, 2, 56]) == 14
    assert candidate([5, 5, 55]) == 20
    assert candidate([7, 4, 58]) == 24
    assert candidate([5, 3, 56]) == 19
    assert candidate([14, 5, 53]) == 18
    assert candidate([14, 5, 61]) == 17
    assert candidate([5, 6, 52]) == 18
    assert candidate([15, 7, 57]) == 25
    assert candidate([12, 1, 52]) == 11
    assert candidate([13, 2, 53]) == 14
    assert candidate([8, 1, 52]) == 16
    assert candidate([15, 7, 61]) == 20
    assert candidate([13, 4, 51]) == 14
    assert candidate([15, 4, 55]) == 20
    assert candidate([14, 2, 58]) == 20
    assert candidate([13, 6, 57]) == 22
    assert candidate([10, 7, 53]) == 16
    assert candidate([15, 2, 53]) == 16
    assert candidate([10, 2, 61]) == 10
    assert candidate([6, 5, 55]) == 21
    assert candidate([11, 7, 53]) == 17
    assert candidate([11, 6, 53]) == 16
    assert candidate([13, 2, 52]) == 13
    assert candidate([11, 1, 55]) == 13
    assert candidate([[13, 21, 9, 9, 'o', 67, 'l']]) == 38
    assert candidate([[5, 15, 6, 2, 'u', 66, 't']]) == 31
    assert candidate([[7, 22, 7, 1, 'k', 73, 'y']]) == 29
    assert candidate([[14, 23, 9, 4, 'q', 71, 'c']]) == 31
    assert candidate([[11, 19, 5, 9, 'm', 75, 'r']]) == 38
    assert candidate([[7, 19, 8, 2, 'm', 75, 'i']]) == 39
    assert candidate([[6, 16, 6, 10, 'z', 73, 'f']]) == 30
    assert candidate([[12, 19, 4, 8, 'b', 69, 'v']]) == 40
    assert candidate([[9, 15, 1, 7, 'y', 72, 'm']]) == 32
    assert candidate([[9, 16, 8, 4, 'n', 70, 'b']]) == 35
    assert candidate([[6, 18, 5, 1, 'a', 74, 'x']]) == 32
    assert candidate([[8, 16, 6, 8, 'j', 70, 'z']]) == 36
    assert candidate([[11, 16, 9, 9, 'd', 70, 'z']]) == 34
    assert candidate([[8, 17, 8, 5, 'w', 66, 'b']]) == 41
    assert candidate([[15, 16, 5, 2, 'v', 67, 'i']]) == 33
    assert candidate([[7, 23, 2, 7, 'd', 65, 'y']]) == 32
    assert candidate([[10, 18, 4, 4, 'p', 69, 'm']]) == 33
    assert candidate([[12, 17, 7, 8, 'z', 68, 'k']]) == 40
    assert candidate([[13, 17, 1, 4, 'e', 69, 'u']]) == 32
    assert candidate([[14, 18, 4, 10, 'u', 71, 'v']]) == 27
    assert candidate([[10, 22, 3, 10, 'd', 72, 'f']]) == 18
    assert candidate([[8, 19, 9, 4, 'w', 72, 'm']]) == 40
    assert candidate([[8, 18, 9, 10, 'b', 67, 'c']]) == 40
    assert candidate([[12, 23, 9, 6, 'z', 75, 'h']]) == 35
    assert candidate([[15, 20, 3, 6, 'c', 69, 'h']]) == 32
    assert candidate([[10, 18, 3, 1, 'v', 72, 'b']]) == 23
    assert candidate([[10, 21, 4, 3, 'z', 70, 'k']]) == 18
    assert candidate([[14, 24, 8, 6, 'f', 70, 'j']]) == 32
    assert candidate([[9, 19, 9, 5, 'q', 68, 't']]) == 47
    assert candidate([[8, 24, 7, 9, 'l', 65, 'l']]) == 41
    assert candidate([[9, 20, 7, 3, 'v', 65, 'p']]) == 32
    assert candidate([[5, 16, 3, 4, 'v', 66, 'p']]) == 31
    assert candidate([[12, 23, 5, 6, 'z', 71, 'f']]) == 27
    assert candidate([10, 18, -5, 6, -73]) == 31
    assert candidate([15, 24, -8, 4, -69]) == 39
    assert candidate([7, 22, -6, 6, -72]) == 32
    assert candidate([5, 25, -4, 5, -65]) == 32
    assert candidate([10, 15, -7, 9, -68]) == 37
    assert candidate([9, 18, 0, 10, -71]) == 27
    assert candidate([11, 19, -8, 5, -68]) == 39
    assert candidate([6, 18, -7, 5, -73]) == 37
    assert candidate([15, 25, -6, 3, -74]) == 33
    assert candidate([15, 22, -7, 1, -71]) == 26
    assert candidate([15, 19, -4, 1, -74]) == 32
    assert candidate([8, 17, -4, 4, -74]) == 35
    assert candidate([12, 17, -1, 8, -69]) == 35
    assert candidate([7, 15, -4, 3, -75]) == 32
    assert candidate([5, 24, -3, 8, -73]) == 32
    assert candidate([11, 18, -3, 3, -66]) == 29
    assert candidate([5, 19, -7, 10, -73]) == 33
    assert candidate([10, 25, -2, 5, -74]) == 26
    assert candidate([14, 20, -5, 9, -75]) == 33
    assert candidate([5, 23, -2, 8, -67]) == 33
    assert candidate([15, 19, 1, 1, -70]) == 25
    assert candidate([10, 24, -9, 2, -67]) == 31
    assert candidate([12, 16, -6, 7, -65]) == 34
    assert candidate([7, 15, -7, 2, -75]) == 34
    assert candidate([8, 23, -2, 7, -66]) == 34
    assert candidate([14, 18, 0, 10, -75]) == 27
    assert candidate([15, 15, 1, 5, -70]) == 25
    assert candidate([9, 19, -6, 1, -69]) == 41
    assert candidate([13, 20, 1, 4, -75]) == 23
    assert candidate([12, 17, 0, 8, -66]) == 31
    assert candidate([11, 18, -7, 4, -75]) == 34
    assert candidate([12, 21, 0, 3, -70]) == 16
    assert candidate([12, 18, -3, 3, -67]) == 31

if __name__ == '__main__':
    check(sum_of_digits)