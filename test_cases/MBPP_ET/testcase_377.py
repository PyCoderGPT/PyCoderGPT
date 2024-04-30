from case_MBPP_377 import second_smallest


def check(candidate):
    assert candidate([1, 2, -8, -2, 0, -2])==-2
    assert candidate([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert candidate([2,2])==None
    assert candidate([4, 6, -7, 2, 3, -7]) == 2
    assert candidate([3, 4, -4, -7, 5, -4]) == -4
    assert candidate([5, 2, -10, 0, 5, -2]) == -2
    assert candidate([1, 1, -7, 0, 1, 3]) == 0
    assert candidate([1, 5, -8, 2, 2, 0]) == 0
    assert candidate([4, 3, -12, -4, 4, -1]) == -4
    assert candidate([6, 3, -6, -6, 4, 3]) == 3
    assert candidate([5, 6, -9, -1, 1, -5]) == -5
    assert candidate([4, 6, -3, 3, 1, -5]) == -3
    assert candidate([6, 1, -7, -1, 4, -1]) == -1
    assert candidate([5, 7, -8, -1, 1, -2]) == -2
    assert candidate([2, 2, -5, -7, 3, 3]) == -5
    assert candidate([4, 2, -5, 1, 5, -1]) == -1
    assert candidate([1, 4, -8, -4, 4, -3]) == -4
    assert candidate([5, 4, -8, 1, 1, -6]) == -6
    assert candidate([1, 4, -4, -1, 1, -3]) == -3
    assert candidate([1, 5, -12, 3, 1, -6]) == -6
    assert candidate([6, 3, -13, -2, 1, -6]) == -6
    assert candidate([2, 7, -13, -7, 4, 2]) == -7
    assert candidate([3, 3, -5, 0, 4, -1]) == -1
    assert candidate([6, 2, -8, -2, 3, 0]) == -2
    assert candidate([4, 5, -6, 0, 5, -2]) == -2
    assert candidate([2, 2, -6, -5, 3, -2]) == -5
    assert candidate([4, 3, -8, 3, 2, -4]) == -4
    assert candidate([6, 1, -5, -7, 5, 2]) == -5
    assert candidate([3, 6, -13, -5, 3, -5]) == -5
    assert candidate([1, 7, -10, -7, 4, -2]) == -7
    assert candidate([4, 7, -5, -3, 2, 2]) == -3
    assert candidate([4, 4, -7, 3, 1, -4]) == -4
    assert candidate([5, 3, -11, -1, 1, -3]) == -3
    assert candidate([4, 7, -8, -4, 1, -2]) == -4
    assert candidate([2, 6, -8, -4, 1, -7]) == -7
    assert candidate([1, 7, -13, -1, 3, -3]) == -3
    assert candidate([3, 2, 2.6001204916072878, 4, 4, -7, -7]) == 2
    assert candidate([1, 6, 5.724424646495638, 5, 5, -5, 2]) == 1
    assert candidate([6, 1, 5.5221015473642705, 1, 3, -2, -1]) == -1
    assert candidate([1, 1, 3.447743971849392, 1, 6, -3, 3]) == 1
    assert candidate([4, 1, 1.096187235598133, 2, 6, 1, 2]) == 1.096187235598133
    assert candidate([6, 3, 4.329976582341966, 5, 2, 3, -7]) == 2
    assert candidate([5, 3, 5.232787624230036, 2, 3, 2, -4]) == 2
    assert candidate([1, 3, 4.050227737862737, 4, 6, 2, 2]) == 2
    assert candidate([4, 4, 2.82504701110075, 2, 2, 3, -2]) == 2
    assert candidate([5, 4, 4.030550976592697, 1, 6, -4, -6]) == -4
    assert candidate([6, 3, 4.523644230757451, 5, 1, -6, -6]) == 1
    assert candidate([5, 5, 4.233586616131731, 5, 4, -4, -3]) == -3
    assert candidate([4, 6, 5.624403075180702, 5, 5, -3, 0]) == 0
    assert candidate([3, 5, 1.9138849035524488, 5, 1, 2, -4]) == 1
    assert candidate([4, 3, 1.1285649466536498, 2, 4, 1, 0]) == 1
    assert candidate([3, 1, 5.862501819987239, 1, 3, -4, -3]) == -3
    assert candidate([5, 6, 1.717701469665796, 5, 1, -5, -1]) == -1
    assert candidate([4, 2, 3.3682590022073606, 4, 7, 2, 2]) == 3.3682590022073606
    assert candidate([6, 4, 1.7710853474279702, 3, 2, -7, 1]) == 1
    assert candidate([5, 1, 3.3495188443981188, 1, 1, 0, -7]) == 0
    assert candidate([5, 2, 4.047275209559686, 4, 4, 2, 2]) == 4
    assert candidate([6, 1, 5.560677018039675, 1, 2, 0, 2]) == 1
    assert candidate([1, 2, 1.4838695827343606, 1, 2, 1, 2]) == 1.4838695827343606
    assert candidate([3, 3, 3.3805827968676234, 5, 4, -5, -2]) == -2
    assert candidate([3, 2, 4.8176552548736105, 1, 2, -1, -7]) == -1
    assert candidate([3, 2, 2.668698656949097, 1, 7, 3, -5]) == 1
    assert candidate([4, 4, 4.086864961711968, 1, 4, -2, -1]) == -1
    assert candidate([2, 2, 3.9788492434404223, 2, 1, -2, -3]) == -2
    assert candidate([6, 1, 3.261424550090157, 4, 3, 1, -4]) == 1
    assert candidate([6, 4, 3.372885362969777, 1, 3, -2, -1]) == -1
    assert candidate([1, 1, 1.0700956011800855, 2, 3, -1, 0]) == 0
    assert candidate([1, 4, 5.140594673019265, 4, 1, -1, -3]) == -1
    assert candidate([1, 1, 1.8757431576934303, 5, 6, -3, -7]) == -3
    assert candidate([5, 6]) == 6
    assert candidate([7, 5]) == 7
    assert candidate([4, 7]) == 7
    assert candidate([6, 1]) == 6
    assert candidate([2, 1]) == 2
    assert candidate([2, 5]) == 5
    assert candidate([7, 3]) == 7
    assert candidate([7, 3]) == 7
    assert candidate([3, 5]) == 5
    assert candidate([1, 4]) == 4
    assert candidate([3, 3]) == None
    assert candidate([4, 1]) == 4
    assert candidate([7, 7]) == None
    assert candidate([4, 1]) == 4
    assert candidate([7, 2]) == 7
    assert candidate([2, 5]) == 5
    assert candidate([3, 3]) == None
    assert candidate([7, 4]) == 7
    assert candidate([2, 4]) == 4
    assert candidate([3, 2]) == 3
    assert candidate([4, 1]) == 4
    assert candidate([1, 1]) == None
    assert candidate([4, 7]) == 7
    assert candidate([3, 4]) == 4
    assert candidate([6, 4]) == 6
    assert candidate([1, 1]) == None
    assert candidate([3, 1]) == 3
    assert candidate([5, 4]) == 5
    assert candidate([7, 1]) == 7
    assert candidate([6, 5]) == 6
    assert candidate([4, 4]) == None
    assert candidate([6, 1]) == 6
    assert candidate([5, 2]) == 5

if __name__ == '__main__':
    check(second_smallest)