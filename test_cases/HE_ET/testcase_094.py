from case_HE_094 import skjkasdkd


def check(candidate):
    assert candidate([0,81,12,3,1,21]) == 3
    assert candidate([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10
    assert candidate([127, 97, 8192]) == 10
    assert candidate([1, 3, 6, 5, 8, 7, 4, 2, 5, 3, 6, 7, 183, 28, 2, 33, 2, 6, 27, 319, 8, 8]) == 7
    assert candidate([1, 11, 1, 2, 1, 10]) == 2
    assert candidate([8721, 122608, 128, 7]) == 7
    assert candidate([8191, 123456, 127, 7]) == 19
    assert candidate([2, 8, 4, 6, 4, 10]) == 2
    assert candidate([8995]) == 0
    assert candidate([5, 2, 2, 11, 5, 3626, 4, 5, 5, 38, 2, 2, 6, 7, 7, 6, 8, 5]) == 2
    assert candidate([2, 4, 5, 34, 5912, 29, 83693, 108, 164, 25, 3174, 30, 29, 6, 10, 4]) == 11
    assert candidate([3, 729, 37, 66, 95, 33, 8, 5, 1, 93, 79, 5, 9, 2]) == 16
    assert candidate([8035]) == 0
    assert candidate([8910, 123905, 128, 3]) == 3
    assert candidate([2, 5, 2, 7, 3, 4101, 3, 4, 1, 36, 5, 3, 3, 4, 2, 1, 8, 1]) == 7
    assert candidate([3, 81, 15, 4, 5, 25]) == 5
    assert candidate([3, 5, 5, 30, 4831, 37, 83712, 114, 161, 27, 2975, 29, 27, 4, 10, 1]) == 16
    assert candidate([4, 729, 27, 69, 101, 35, 1, 1, 3, 89, 84, 4, 10, 1]) == 2
    assert candidate([2, 76, 15, 3, 3, 25]) == 3
    assert candidate([129, 100, 7701]) == 0
    assert candidate([3, 7, 6, 5, 5, 2, 12, 6, 6, 2, 5, 1, 183, 37, 5, 30, 1, 5, 29, 321, 9, 8]) == 10
    assert candidate([1, 85, 16, 6, 1, 26]) == 1
    assert candidate([3, 78, 16, 3, 1, 17]) == 8
    assert candidate([2, 1, 5, 3, 2, 7, 11, 9, 9, 9, 4, 7, 185, 31, 8, 29, 6, 6, 29, 328, 3, 2]) == 4
    assert candidate([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) == 11
    assert candidate([7476, 123438, 129, 6]) == 0
    assert candidate([6, 3, 6, 9, 1, 4258, 5, 1, 7, 41, 3, 1, 1, 7, 6, 1, 1, 3]) == 5
    assert candidate([2, 8, 3, 3, 4, 3, 5, 6, 2, 6, 9, 3, 184, 30, 7, 37, 7, 2, 34, 324, 1, 5]) == 10
    assert candidate([1, 6, 2, 36, 4276, 36, 83181, 106, 168, 23, 2295, 37, 27, 3, 7, 6]) == 10
    assert candidate([5, 3, 2, 4, 5, 7, 7, 9, 3, 10, 9, 1, 183, 29, 3, 31, 3, 4, 31, 328, 7, 5]) == 4
    assert candidate([5, 85, 17, 6, 3, 26]) == 8
    assert candidate([123, 96, 8623]) == 19
    assert candidate([8379, 123265, 124, 2]) == 2
    assert candidate([1, 1, 1, 34, 5604, 29, 83308, 108, 167, 22, 1969, 32, 29, 1, 4, 4]) == 14
    assert candidate([132, 96, 8998]) == 0
    assert candidate([1, 4, 4, 2, 1, 4, 5, 8, 3, 3, 3, 6, 185, 29, 7, 33, 4, 7, 36, 322, 6, 7]) == 11
    assert candidate([7337, 122667, 123, 10]) == 0
    assert candidate([2, 720, 31, 66, 98, 30, 10, 1, 2, 93, 78, 5, 10, 3]) == 4
    assert candidate([3, 8, 3, 2, 1, 7]) == 7
    assert candidate([5, 6, 2, 3, 6, 2]) == 5
    assert candidate([7273, 122950, 128, 10]) == 0
    assert candidate([2, 7, 7, 3, 2, 3, 4, 2, 8, 1, 9, 2, 180, 35, 7, 32, 1, 6, 27, 322, 7, 6]) == 7
    assert candidate([1, 9, 5, 4, 1, 11]) == 2
    assert candidate([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) == 13
    assert candidate([3, 719, 31, 66, 97, 29, 1, 3, 5, 86, 80, 3, 7, 3]) == 17
    assert candidate([3, 722, 34, 72, 97, 30, 10, 1, 6, 91, 80, 2, 3, 7]) == 16
    assert candidate([130, 95, 8293]) == 22
    assert candidate([4, 8, 6, 6, 3, 9, 10, 7, 2, 7, 9, 3, 184, 32, 2, 27, 5, 6, 31, 319, 2, 8]) == 4
    assert candidate([1, 7, 1, 3, 4, 2, 8, 8, 7, 3, 10, 7, 176, 27, 9, 35, 5, 7, 28, 329, 1, 5]) == 7
    assert candidate([1, 5, 3, 6, 5, 4637, 6, 2, 6, 39, 2, 2, 1, 5, 3, 1, 7, 2]) == 20
    assert candidate([5, 2, 5, 2, 7, 9, 7, 5, 5, 7, 7, 2, 181, 35, 4, 34, 1, 4, 35, 320, 3, 7]) == 10
    assert candidate([4, 726, 34, 75, 95, 28, 7, 1, 3, 94, 83, 3, 3, 6]) == 11
    assert candidate([8677, 122524, 129, 7]) == 28
    assert candidate([2, 6, 1, 1, 5, 1, 10, 6, 1, 2, 6, 2, 176, 32, 5, 33, 3, 1, 36, 319, 7, 7]) == 7
    assert candidate([1, 724, 28, 71, 94, 37, 1, 2, 10, 87, 81, 1, 7, 7]) == 8
    assert candidate([8191]) == 19
    assert candidate([5, 9, 5, 5, 5, 4]) == 5
    assert candidate([129, 95, 7634]) == 0
    assert candidate([2, 724, 35, 68, 97, 29, 3, 1, 8, 86, 88, 2, 8, 1]) == 16
    assert candidate([3, 4, 3, 9, 5, 4816, 2, 1, 1, 44, 6, 6, 3, 2, 9, 1, 10, 4]) == 5
    assert candidate([1, 84, 7, 3, 4, 25]) == 7
    assert candidate([8982]) == 0
    assert candidate([126, 92, 8168]) == 0
    assert candidate([5, 727, 35, 66, 97, 33, 3, 4, 7, 96, 84, 2, 6, 7]) == 16
    assert candidate([8839, 122979, 125, 10]) == 28
    assert candidate([4, 84, 11, 6, 4, 20]) == 2
    assert candidate([1, 724, 36, 72, 103, 34, 8, 2, 8, 87, 78, 1, 10, 4]) == 4
    assert candidate([6, 3, 2, 7, 1, 5133, 6, 4, 4, 37, 6, 4, 4, 2, 3, 3, 7, 5]) == 10
    assert candidate([2, 13, 3, 4, 6, 4]) == 4
    assert candidate([5, 729, 37, 72, 94, 31, 8, 5, 7, 90, 85, 2, 8, 10]) == 10
    assert candidate([3, 80, 12, 5, 5, 24]) == 5
    assert candidate([2, 5, 1, 13, 3, 3861, 1, 3, 1, 40, 1, 6, 5, 4, 5, 2, 10, 4]) == 4
    assert candidate([4, 5, 2, 4, 5, 4354, 3, 4, 5, 35, 3, 3, 4, 6, 7, 3, 9, 6]) == 7
    assert candidate([5, 12, 5, 7, 6, 9]) == 7
    assert candidate([5, 3, 1, 10, 2, 3930, 4, 2, 5, 45, 2, 3, 2, 4, 3, 6, 2, 3]) == 5
    assert candidate([8202]) == 0
    assert candidate([2, 7, 1, 37, 4211, 31, 83200, 107, 158, 28, 1455, 29, 30, 4, 13, 3]) == 8
    assert candidate([1, 7, 3, 28, 4374, 34, 82577, 108, 161, 22, 2382, 31, 35, 3, 14, 4]) == 4
    assert candidate([5, 79, 12, 2, 6, 16]) == 16
    assert candidate([1, 8, 4, 2, 6, 4, 7, 4, 7, 8, 10, 3, 186, 27, 9, 37, 5, 7, 32, 325, 4, 8]) == 10
    assert candidate([2, 725, 28, 72, 103, 33, 1, 1, 2, 96, 86, 1, 5, 11]) == 4
    assert candidate([131, 99, 8407]) == 5
    assert candidate([9057, 122599, 125, 4]) == 28
    assert candidate([6, 2, 2, 34, 4802, 29, 83179, 104, 163, 20, 2855, 28, 34, 6, 5, 6]) == 10
    assert candidate([2, 80, 16, 1, 2, 26]) == 2
    assert candidate([8096, 123506, 128, 12]) == 0
    assert candidate([0,8,1,2,1,7]) == 7
    assert candidate([4, 725, 37, 70, 100, 27, 11, 1, 7, 90, 88, 1, 6, 9]) == 10
    assert candidate([5, 5, 3, 1, 5, 3]) == 5
    assert candidate([3, 7, 3, 1, 1, 5]) == 7
    assert candidate([3, 1, 1, 8, 1, 4909, 3, 4, 6, 43, 6, 4, 6, 5, 1, 1, 4, 5]) == 22
    assert candidate([5, 2, 3, 5, 3, 8, 10, 5, 4, 8, 6, 4, 179, 28, 2, 35, 4, 7, 29, 324, 4, 5]) == 17
    assert candidate([131, 93, 8571]) == 5
    assert candidate([132, 94, 7961]) == 0
    assert candidate([129, 101, 8468]) == 2
    assert candidate([1, 13, 3, 5, 1, 8]) == 4
    assert candidate([7534]) == 0
    assert candidate([2, 4, 6, 4, 2, 5344, 6, 1, 5, 39, 4, 3, 3, 2, 7, 6, 8, 5]) == 7
    assert candidate([8267, 123600, 124, 7]) == 7
    assert candidate([6, 3, 2, 32, 5561, 31, 83909, 107, 166, 26, 3275, 29, 32, 5, 14, 6]) == 8
    assert candidate([126, 99, 8790]) == 0
    assert candidate([1, 3, 4, 13, 3, 4527, 1, 2, 2, 41, 6, 5, 5, 6, 8, 1, 3, 4]) == 5
    assert candidate([2, 83, 14, 1, 3, 21]) == 11
    assert candidate([3, 13, 5, 5, 4, 12]) == 4
    assert candidate([8491]) == 0
    assert candidate([4, 84, 9, 8, 4, 23]) == 5
    assert candidate([131, 98, 7278]) == 5
    assert candidate([7730]) == 0
    assert candidate([8957]) == 0
    assert candidate([8558, 122558, 127, 8]) == 10
    assert candidate([1, 5, 1, 4, 5, 4161, 1, 3, 3, 35, 6, 2, 2, 2, 9, 1, 7, 2]) == 7
    assert candidate([8472]) == 0
    assert candidate([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25
    assert candidate([8305]) == 0
    assert candidate([2, 83, 16, 4, 4, 25]) == 11
    assert candidate([5, 2, 5, 9, 5, 4969, 4, 1, 7, 38, 5, 6, 6, 1, 3, 4, 7, 1]) == 28
    assert candidate([5, 86, 15, 1, 5, 21]) == 5
    assert candidate([8138, 123467, 128, 10]) == 0
    assert candidate([4, 6, 2, 35, 4257, 37, 82857, 113, 166, 24, 1400, 30, 34, 5, 6, 1]) == 5
    assert candidate([7732]) == 0
    assert candidate([8449, 123035, 132, 12]) == 0
    assert candidate([4, 7, 2, 6, 5, 3, 12, 6, 8, 5, 2, 4, 186, 36, 1, 28, 7, 6, 37, 322, 8, 1]) == 10
    assert candidate([127, 100, 7275]) == 10
    assert candidate([5, 7, 2, 30, 4641, 32, 83437, 111, 158, 27, 3279, 29, 27, 6, 9, 1]) == 25
    assert candidate([1, 9, 6, 5, 1, 12]) == 5
    assert candidate([5, 722, 35, 76, 102, 28, 11, 1, 6, 93, 83, 3, 1, 5]) == 11
    assert candidate([7207]) == 16
    assert candidate([5, 7, 5, 6, 6, 6]) == 7
    assert candidate([129, 93, 7500]) == 0
    assert candidate([1, 4, 3, 29, 4849, 35, 83707, 107, 168, 19, 2483, 34, 30, 5, 12, 2]) == 8
    assert candidate([8839]) == 28
    assert candidate([4, 4, 1, 33, 5640, 39, 84108, 111, 165, 24, 3055, 32, 26, 5, 12, 8]) == 5
    assert candidate([2, 6, 2, 33, 4932, 39, 82581, 106, 165, 25, 3239, 31, 30, 5, 9, 5]) == 4
    assert candidate([2, 8, 1, 33, 4189, 32, 82229, 109, 167, 22, 1460, 30, 28, 1, 8, 6]) == 14

if __name__ == '__main__':
    check(skjkasdkd)