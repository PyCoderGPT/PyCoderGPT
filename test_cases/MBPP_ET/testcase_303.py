from case_MBPP_303 import find_kth


def check(candidate):
    assert candidate([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5) == 6
    assert candidate([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, 7) == 256
    assert candidate([3, 4, 7, 8, 10], [2, 5, 9, 11], 5, 4, 6) == 8
    assert candidate([3, 6, 8, 4, 6], [4, 9, 12, 7], 1, 2, 2) == 4
    assert candidate([6, 7, 4, 3, 6], [3, 5, 5, 10], 1, 4, 2) == 5
    assert candidate([2, 5, 10, 3, 8], [6, 2, 7, 13], 5, 2, 1) == 2
    assert candidate([1, 4, 10, 7, 9], [1, 9, 4, 10], 5, 2, 3) == 4
    assert candidate([5, 6, 2, 12, 10], [3, 7, 9, 13], 4, 4, 8) == 13
    assert candidate([7, 5, 5, 8, 13], [3, 2, 9, 12], 5, 1, 6) == 13
    assert candidate([1, 5, 9, 10, 9], [2, 1, 5, 10], 4, 2, 1) == 1
    assert candidate([7, 6, 1, 2, 10], [6, 2, 10, 8], 1, 1, 2) == 7
    assert candidate([7, 1, 9, 4, 5], [2, 9, 12, 6], 5, 1, 6) == 5
    assert candidate([4, 2, 5, 12, 6], [6, 3, 5, 12], 4, 4, 4) == 6
    assert candidate([3, 4, 8, 2, 5], [2, 3, 10, 6], 2, 4, 2) == 3
    assert candidate([4, 4, 5, 12, 14], [5, 4, 11, 11], 3, 1, 2) == 4
    assert candidate([2, 4, 10, 9, 7], [4, 8, 13, 9], 3, 3, 3) == 4
    assert candidate([2, 8, 7, 10, 14], [4, 1, 4, 14], 1, 2, 3) == 1
    assert candidate([4, 3, 11, 12, 7], [5, 8, 7, 7], 4, 1, 1) == 4
    assert candidate([2, 4, 11, 3, 10], [5, 9, 3, 6], 1, 3, 3) == 9
    assert candidate([4, 6, 6, 9, 6], [3, 2, 9, 6], 3, 3, 6) == 9
    assert candidate([4, 3, 6, 12, 10], [3, 7, 6, 13], 1, 4, 1) == 3
    assert candidate([6, 8, 4, 11, 9], [3, 3, 4, 7], 1, 4, 1) == 3
    assert candidate([5, 8, 5, 6, 12], [4, 1, 11, 12], 4, 1, 1) == 4
    assert candidate([4, 8, 6, 2, 7], [2, 6, 9, 14], 2, 3, 2) == 4
    assert candidate([2, 4, 5, 11, 11], [1, 2, 5, 6], 4, 4, 3) == 2
    assert candidate([1, 4, 9, 12, 5], [5, 9, 4, 14], 3, 1, 3) == 5
    assert candidate([4, 5, 1, 6, 8], [2, 3, 11, 7], 1, 4, 2) == 3
    assert candidate([7, 5, 4, 10, 5], [1, 8, 7, 7], 5, 4, 3) == 5
    assert candidate([1, 6, 10, 10, 11], [2, 2, 9, 7], 2, 1, 1) == 1
    assert candidate([5, 3, 9, 8, 4], [5, 2, 8, 10], 5, 4, 5) == 8
    assert candidate([6, 2, 4, 8, 9], [1, 4, 12, 7], 3, 2, 1) == 1
    assert candidate([2, 5, 2, 3, 14], [5, 4, 10, 13], 2, 2, 4) == 5
    assert candidate([3, 7, 5, 4, 8], [1, 1, 10, 14], 4, 1, 4) == 5
    assert candidate([7, 4, 1, 7, 10], [3, 9, 11, 9], 5, 4, 9) == 9
    assert candidate([6, 6, 3, 11, 10], [4, 6, 11, 7], 5, 1, 2) == 6
    assert candidate([3, 3, 1, 6, 14], [5, 4, 11, 11], 2, 4, 5) == 11
    assert candidate([104, 108, 260, 344, 770], [71, 87, 116, 117, 269, 450, 892], 4, 7, 3) == 104
    assert candidate([100, 113, 257, 353, 769], [70, 83, 117, 115, 269, 447, 895], 4, 6, 8) == 269
    assert candidate([104, 111, 251, 349, 766], [74, 88, 117, 122, 269, 445, 890], 5, 5, 2) == 88
    assert candidate([99, 112, 256, 349, 773], [74, 89, 118, 124, 260, 440, 896], 3, 2, 4) == 112
    assert candidate([100, 109, 257, 351, 773], [68, 82, 111, 119, 267, 446, 892], 2, 7, 8) == 446
    assert candidate([97, 112, 251, 350, 768], [69, 89, 117, 121, 265, 446, 893], 2, 6, 3) == 97
    assert candidate([98, 117, 258, 348, 767], [71, 83, 118, 116, 261, 447, 887], 1, 3, 2) == 83
    assert candidate([102, 117, 252, 349, 773], [67, 89, 111, 117, 266, 446, 893], 3, 4, 2) == 89
    assert candidate([101, 112, 261, 354, 765], [75, 85, 112, 124, 265, 444, 897], 4, 7, 3) == 101
    assert candidate([104, 108, 261, 348, 768], [68, 90, 110, 116, 264, 450, 897], 4, 7, 6) == 116
    assert candidate([102, 107, 256, 348, 774], [69, 86, 117, 122, 261, 443, 897], 1, 5, 3) == 102
    assert candidate([105, 108, 254, 345, 765], [73, 89, 118, 122, 270, 446, 887], 4, 5, 3) == 105
    assert candidate([97, 111, 257, 346, 769], [72, 81, 109, 122, 269, 447, 893], 4, 7, 8) == 269
    assert candidate([95, 113, 257, 348, 774], [67, 87, 114, 115, 268, 446, 889], 4, 4, 4) == 113
    assert candidate([105, 112, 261, 354, 766], [72, 86, 116, 122, 267, 450, 891], 1, 5, 3) == 105
    assert candidate([97, 107, 261, 353, 765], [76, 84, 112, 117, 269, 447, 887], 5, 5, 7) == 261
    assert candidate([105, 115, 260, 348, 775], [73, 91, 110, 124, 269, 444, 896], 3, 4, 3) == 105
    assert candidate([100, 116, 261, 353, 766], [75, 86, 110, 118, 270, 448, 893], 3, 4, 2) == 86
    assert candidate([101, 108, 257, 350, 775], [76, 84, 111, 121, 265, 442, 897], 1, 3, 4) == 111
    assert candidate([95, 112, 255, 350, 769], [68, 87, 114, 121, 260, 447, 887], 5, 4, 2) == 87
    assert candidate([97, 114, 254, 348, 770], [68, 89, 112, 119, 265, 447, 894], 1, 7, 7) == 447
    assert candidate([97, 108, 258, 347, 774], [76, 86, 111, 121, 265, 446, 893], 5, 4, 2) == 86
    assert candidate([98, 117, 258, 344, 772], [69, 89, 118, 115, 260, 449, 889], 1, 6, 2) == 89
    assert candidate([99, 107, 261, 349, 774], [70, 82, 109, 119, 265, 450, 892], 3, 7, 6) == 119
    assert candidate([104, 111, 259, 347, 768], [75, 88, 111, 115, 260, 444, 887], 1, 4, 4) == 111
    assert candidate([103, 110, 255, 350, 770], [73, 84, 108, 115, 264, 448, 887], 5, 6, 2) == 84
    assert candidate([103, 117, 257, 349, 769], [76, 86, 110, 114, 265, 446, 893], 3, 4, 5) == 114
    assert candidate([99, 116, 261, 351, 774], [72, 81, 108, 124, 262, 443, 887], 1, 3, 4) == 108
    assert candidate([101, 114, 256, 354, 768], [74, 84, 109, 119, 260, 445, 888], 5, 7, 2) == 84
    assert candidate([96, 109, 259, 352, 771], [77, 81, 111, 114, 269, 449, 887], 4, 3, 7) == 352
    assert candidate([99, 109, 261, 351, 769], [76, 82, 114, 119, 262, 448, 891], 3, 7, 6) == 119
    assert candidate([104, 111, 261, 349, 766], [73, 86, 108, 121, 267, 448, 888], 3, 6, 9) == 448
    assert candidate([103, 112, 253, 349, 765], [67, 86, 110, 120, 262, 450, 888], 5, 5, 6) == 120
    assert candidate([6, 1, 2, 11, 9], [3, 7, 5, 8], 3, 4, 5) == 7
    assert candidate([5, 3, 7, 3, 13], [5, 7, 13, 7], 5, 4, 8) == 7
    assert candidate([5, 2, 7, 8, 13], [7, 5, 10, 13], 4, 2, 4) == 5
    assert candidate([6, 8, 5, 5, 6], [3, 3, 14, 9], 1, 4, 1) == 3
    assert candidate([1, 4, 5, 11, 12], [6, 9, 14, 7], 5, 1, 5) == 11
    assert candidate([5, 9, 9, 12, 8], [5, 3, 11, 14], 4, 2, 6) == 12
    assert candidate([7, 3, 3, 3, 5], [7, 2, 5, 15], 5, 2, 1) == 7
    assert candidate([2, 4, 7, 11, 7], [1, 4, 13, 14], 5, 3, 6) == 11
    assert candidate([3, 7, 12, 4, 7], [6, 8, 5, 8], 2, 4, 6) == 8
    assert candidate([8, 3, 12, 12, 6], [4, 6, 8, 7], 1, 4, 3) == 8
    assert candidate([7, 1, 2, 10, 9], [4, 5, 8, 9], 4, 3, 4) == 1
    assert candidate([3, 2, 10, 10, 13], [7, 4, 5, 7], 3, 4, 5) == 5
    assert candidate([1, 9, 2, 13, 15], [5, 10, 9, 14], 4, 2, 6) == 13
    assert candidate([8, 3, 3, 5, 12], [5, 8, 10, 6], 5, 3, 3) == 8
    assert candidate([5, 6, 9, 3, 12], [7, 1, 7, 11], 3, 3, 2) == 6
    assert candidate([6, 2, 2, 11, 14], [2, 8, 10, 8], 2, 4, 2) == 6
    assert candidate([1, 4, 3, 8, 14], [6, 7, 9, 8], 1, 4, 5) == 8
    assert candidate([5, 4, 3, 11, 13], [3, 4, 10, 14], 3, 3, 6) == 10
    assert candidate([8, 2, 5, 4, 12], [5, 7, 14, 10], 4, 3, 4) == 2
    assert candidate([2, 5, 5, 7, 9], [6, 8, 10, 6], 4, 1, 5) == 7
    assert candidate([3, 7, 7, 7, 11], [5, 5, 6, 7], 4, 2, 1) == 3
    assert candidate([6, 6, 3, 13, 6], [7, 9, 10, 11], 4, 4, 5) == 9
    assert candidate([4, 3, 8, 4, 10], [7, 9, 4, 16], 3, 3, 1) == 4
    assert candidate([6, 5, 4, 11, 5], [5, 3, 12, 8], 2, 4, 4) == 5
    assert candidate([3, 8, 2, 9, 7], [4, 10, 10, 13], 5, 1, 2) == 4
    assert candidate([5, 6, 12, 3, 9], [3, 10, 11, 12], 4, 4, 4) == 10
    assert candidate([7, 4, 11, 8, 13], [6, 7, 7, 10], 4, 4, 5) == 4
    assert candidate([8, 9, 8, 12, 15], [2, 3, 13, 13], 5, 4, 1) == 2
    assert candidate([7, 3, 11, 4, 14], [6, 7, 9, 9], 1, 3, 4) == 9
    assert candidate([6, 6, 6, 9, 7], [6, 9, 8, 8], 1, 4, 4) == 8
    assert candidate([7, 7, 12, 7, 7], [6, 7, 13, 8], 5, 1, 6) == 7
    assert candidate([3, 2, 6, 13, 5], [1, 8, 11, 7], 2, 2, 4) == 8
    assert candidate([2, 9, 4, 7, 15], [4, 9, 8, 8], 3, 1, 1) == 2

if __name__ == '__main__':
    check(find_kth)