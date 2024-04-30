from case_HE_133 import sum_squares


def check(candidate):
    assert candidate([9434, 10144]) == 191901092
    assert candidate([5.997, 6, 3]) == 81
    assert candidate([3.327, 2, 7]) == 69
    assert candidate([0.018, 14.66, 13.014, 15.188]) == 678
    assert candidate([9574, 10213]) == 195966845
    assert candidate([9165, 10377]) == 191679354
    assert candidate([-4.222, 3.751, 10.595]) == 153
    assert candidate([-5.714, 22.497, 14.173, 22.134]) == 1308
    assert candidate([1, 1, 1]) == 3
    assert candidate([1, 1, 2]) == 6
    assert candidate([3, 7, 2]) == 62
    assert candidate([-3, 6, 5]) == 70
    assert candidate([-4.95, 2, 5]) == 45
    assert candidate([9277, 9545]) == 177169754
    assert candidate([2.01, 6.193, 1]) == 59
    assert candidate([-1]) == 1
    assert candidate([1, 8, 1, 2]) == 70
    assert candidate([2, 1, 10, 7]) == 154
    assert candidate([1.457, 7, 8]) == 117
    assert candidate([1.05, 6.88, 5]) == 78
    assert candidate([5.855, 4.571, 3]) == 70
    assert candidate([103, 4, 15, 3]) == 10859
    assert candidate([-2.854, 12.651, 18.252, 22.792]) == 1063
    assert candidate([0.156, 2.708, 1.964]) == 14
    assert candidate([102, 1, 16, 3]) == 10670
    assert candidate([-2.192, 6.531, 7.947]) == 117
    assert candidate([2.169, 7, 1]) == 59
    assert candidate([2.872, 3, 5]) == 43
    assert candidate([-6, 5, 1]) == 62
    assert candidate([2.178, 2.152, 5]) == 43
    assert candidate([0.29, 1.85, 7.406]) == 69
    assert candidate([1,2,3])==14
    assert candidate([3.808, 1, 2]) == 21
    assert candidate([10899, 9187]) == 203189170
    assert candidate([0, 5, 2]) == 29
    assert candidate([-3, 4, 3]) == 34
    assert candidate([1,3,5,7])==84
    assert candidate([100,1,15,2])==10230
    assert candidate([5, 1, 5, 12]) == 195
    assert candidate([-2.286, 12.406, 13.124, 15.17]) == 625
    assert candidate([10530, 10750]) == 226443400
    assert candidate([1, 3, 4, 7]) == 75
    assert candidate([2.414, 6, 7]) == 94
    assert candidate([6.717, 7.781, 2]) == 117
    assert candidate([-1.25, 6, 4]) == 53
    assert candidate([2, 2, 4]) == 24
    assert candidate([1.4,4.2,0])==29
    assert candidate([-1, 3, 4]) == 26
    assert candidate([2.501, 1.394, 5]) == 38
    assert candidate([-3.736, 7.572, 3.736]) == 89
    assert candidate([3.534, 3, 6]) == 61
    assert candidate([1, 6, 2]) == 41
    assert candidate([1, 3, 5, 3]) == 44
    assert candidate([-1,1,0])==2
    assert candidate([97, 1, 10, 3]) == 9519
    assert candidate([3.706, 1, 8]) == 81
    assert candidate([2.427, 2.41, 1]) == 19
    assert candidate([98, 4, 18, 5]) == 9969
    assert candidate([1.02, 4, 3]) == 29
    assert candidate([2.819, 3.053, 3]) == 34
    assert candidate([-5.899, 4.772, 3.238]) == 66
    assert candidate([2.973, 6, 3]) == 54
    assert candidate([-3]) == 9
    assert candidate([95, 6, 15, 7]) == 9335
    assert candidate([-1.008, 20.367, 17.503, 15.597]) == 1022
    assert candidate([6, 8, 10, 5]) == 225
    assert candidate([10000,10000])==200000000
    assert candidate([1]) == 1
    assert candidate([-1, 4, 4]) == 33
    assert candidate([-1.466, 20.894, 13.499, 18.436]) == 999
    assert candidate([3.246, 6, 3]) == 61
    assert candidate([4, 3, 4]) == 41
    assert candidate([-4.293, 4, 2]) == 36
    assert candidate([-1.049, 21.79, 17.42, 24.654]) == 1434
    assert candidate([4.321, 6.246, 2.174]) == 83
    assert candidate([-2.4,1,1])==6
    assert candidate([-1.063, 2, 5]) == 30
    assert candidate([4]) == 16
    assert candidate([1, 3, 10, 4]) == 126
    assert candidate([-0.161, 4.708, 2.846]) == 34
    assert candidate([-5.071, 19.003, 21.797, 14.901]) == 1134
    assert candidate([9472, 10900]) == 208528784
    assert candidate([1.13, 4, 1]) == 21
    assert candidate([98, 5, 11, 6]) == 9786
    assert candidate([10570, 10770]) == 227717800
    assert candidate([-4.626, 9.385, 6.866]) == 165
    assert candidate([-2]) == 4
    assert candidate([-1, 1, 4]) == 18
    assert candidate([-0.824, 2, 5]) == 29
    assert candidate([99, 2, 18, 1]) == 10130
    assert candidate([0.069, 2, 4]) == 21
    assert candidate([-1])==1
    assert candidate([3, 2, 1, 2]) == 18
    assert candidate([10100, 9662]) == 195364244
    assert candidate([1.413, 6, 5]) == 65
    assert candidate([5]) == 25
    assert candidate([2]) == 4
    assert candidate([4.716, 3.326, 9.135]) == 141
    assert candidate([2, 1, 8]) == 69
    assert candidate([-5, 1, 2]) == 30
    assert candidate([9751, 10057]) == 196225250
    assert candidate([4, 1, 7, 5]) == 91
    assert candidate([0])==0
    assert candidate([98, 5, 20, 1]) == 10030
    assert candidate([4.313, 5.557, 2]) == 65
    assert candidate([2.372, 22.016, 15.346, 18.542]) == 1155
    assert candidate([-1.4,4.6,6.3])==75
    assert candidate([1, 3, 4, 10]) == 126
    assert candidate([1.0,2,3])==14
    assert candidate([97, 2, 16, 5]) == 9694
    assert candidate([5, 6, 3]) == 70
    assert candidate([-5]) == 25
    assert candidate([-2, 6, 4]) == 56
    assert candidate([5.028, 2.27, 5]) == 70
    assert candidate([-1.4,17.9,18.9,19.9])==1086
    assert candidate([102, 4, 14, 2]) == 10620
    assert candidate([3.57, 14.883, 23.709, 15.874]) == 1073
    assert candidate([4, 3, 3]) == 34
    assert candidate([3]) == 9
    assert candidate([5, 5, 8]) == 114

if __name__ == '__main__':
    check(sum_squares)