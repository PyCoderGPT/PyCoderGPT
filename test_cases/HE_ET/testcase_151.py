from case_HE_151 import double_the_difference


def check(candidate):
    assert candidate([2.641, 1, 4]) == 1
    assert candidate([1.62, 2.226, 2.234]) == 0
    assert candidate([4, -4, 11]) == 121
    assert candidate([5, 4]) == 25 
    assert candidate([-10, -15, -34]) == 0
    assert candidate([1.898, 1.028, 5.285]) == 0
    assert candidate([5.104, 4.104, 5.848]) == 0
    assert candidate([1.982, 4.132, 4.139]) == 0
    assert candidate([2, 5]) == 25
    assert candidate([-3, -2, 7]) == 49
    assert candidate([3.552, 4.834, 4.285]) == 0
    assert candidate([4.059, 1, 1]) == 2
    assert candidate([-13, -17, -35]) == 0
    assert candidate([5, 5]) == 50
    assert candidate([9, 6]) == 81
    assert candidate([2.608, 6, 7]) == 49
    assert candidate([4.575, 7, 2]) == 49
    assert candidate([3, 2]) == 9
    assert candidate([1, 9]) == 82
    assert candidate([-6, -18, -25]) == 0
    assert candidate([4, 8]) == 0
    assert candidate([2.532, 8, 9]) == 81
    assert candidate([9, 7]) == 130
    assert candidate([2.92, 5, 5]) == 50
    assert candidate([2, 3, 4]) == 9
    assert candidate([-12, -19, -26]) == 0
    assert candidate([-8, -24, -27]) == 0
    assert candidate([2.803, 6, 4]) == 0
    assert candidate([6, 3]) == 9
    assert candidate([-4, -5, 4]) == 0
    assert candidate(lst) == odd_sum 
    assert candidate([3.343, 1.859, 1.119]) == 0
    assert candidate([8, 4]) == 0
    assert candidate([2, 1, 9]) == 82
    assert candidate([9, 1]) == 82
    assert candidate([4, 3]) == 9
    assert candidate([3.091, 4.937, 4.685]) == 0
    assert candidate([-13, -19, -33]) == 0
    assert candidate([-6, -4, 13]) == 169
    assert candidate([4.856, 3.784, 3.223]) == 0
    assert candidate([5.622, 1.327, 3.166]) == 0
    assert candidate([-1, -2, 8]) == 0
    assert candidate([-5, -16, -27]) == 0
    assert candidate([3.618, 3.501, 3.619]) == 0
    assert candidate([-14, -25, -31]) == 0
    assert candidate([2, -1, 9]) == 81
    assert candidate([2.136, 8, 1]) == 1
    assert candidate([5.803, 8, 4]) == 0
    assert candidate([2.337, 7, 7]) == 98
    assert candidate([]) == 0
    assert candidate([1.734, 8, 9]) == 81
    assert candidate([5.116, 3.781, 3.771]) == 0
    assert candidate([3.486, 1.151, 1.076]) == 0
    assert candidate([-13, -19, -29]) == 0
    assert candidate([-2, 0, 3]) == 9
    assert candidate([-9, -15, -31]) == 0
    assert candidate([3.002, 3, 8]) == 9
    assert candidate([4, 1]) == 1
    assert candidate([7, 3]) == 58
    assert candidate([5.659, 5.72, 2.59]) == 0
    assert candidate([2.746, 2.314, 4.262]) == 0
    assert candidate([4.341, 4.528, 1.906]) == 0
    assert candidate([-10, -20, -30]) == 0 
    assert candidate([1, -6, 7]) == 50
    assert candidate([-5, -5, 10]) == 0
    assert candidate([4, -6, 7]) == 49
    assert candidate([1.314, 8, 8]) == 0
    assert candidate([1.777, 3, 3]) == 18
    assert candidate([-14, -18, -26]) == 0
    assert candidate([2.327, 3, 7]) == 58
    assert candidate([2.978, 2, 5]) == 25
    assert candidate([-8, -19, -27]) == 0
    assert candidate([8, 2]) == 0
    assert candidate([-6, -22, -31]) == 0
    assert candidate([]) == 0 
    assert candidate([-13, -23, -35]) == 0
    assert candidate([2.853, 5, 1]) == 26
    assert candidate([-8, -20, -30]) == 0
    assert candidate([-1, -3, 8]) == 0
    assert candidate([3, 3, 4]) == 18
    assert candidate([2.845, 4, 4]) == 0
    assert candidate([0.2, 3, 5]) == 34
    assert candidate([-1, 2, 8]) == 0
    assert candidate([-1, 3, 6]) == 9
    assert candidate([0.1, 0.2, 0.3]) == 0 
    assert candidate([-14, -22, -25]) == 0
    assert candidate([8, 5]) == 25
    assert candidate([4, -1, 9]) == 81
    assert candidate([-11, -21, -26]) == 0
    assert candidate([2.598, 1.052, 1.239]) == 0
    assert candidate([4.251, 1.83, 4.155]) == 0
    assert candidate([3.484, 5.185, 5.807]) == 0
    assert candidate([-13, -16, -32]) == 0
    assert candidate([-3, 2, 6]) == 0
    assert candidate([-3, -5, 3]) == 9

if __name__ == '__main__':
    check(double_the_difference)