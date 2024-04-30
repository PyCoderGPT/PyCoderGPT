from case_HE_092 import any_int


def check(candidate):
    assert candidate(8, 19, 11) == True
    assert candidate(7.307, 7.071, 5.088) == False
    assert candidate(6, 12, 6) == True
    assert candidate(6.511, 2, 3) == False
    assert candidate(12, 6, 6) == True
    assert candidate(2, 2, 4) == True
    assert candidate(5.114, 5, 4) == False
    assert candidate(3.376, 6.953, 2.111) == False
    assert candidate(2, 3, 1)==True
    assert candidate(2, 5, 4) == False
    assert candidate(7.194, 1.302, 7.462) == False
    assert candidate(1, 7, 8) == True
    assert candidate(5, 8, 3) == True
    assert candidate(2.389, 9, 10) == False
    assert candidate(-1, 0, 1) == True
    assert candidate(9, 6, 3) == True
    assert candidate(4.38, 6, 1) == False
    assert candidate(3.785, 6.308, 7.367) == False
    assert candidate(6, 10, 4) == True
    assert candidate(1.705, 2, 6.616) == False
    assert candidate(6, 4, 2) == True
    assert candidate(4, 2, 2)==True
    assert candidate(3.692, 2, 7.2) == False
    assert candidate(2.5, 2, 3)==False
    assert candidate(5, 6, 1) == True
    assert candidate(1, 3, 2) == True
    assert candidate(3,4,7)==True
    assert candidate(6, 10, 1) == False
    assert candidate(6, 2, 4) == True
    assert candidate(6.155, 2.926, 1.672) == False
    assert candidate(5, 2, 3) == True
    assert candidate(7.829, 2, 9) == False
    assert candidate(4, 6, 3) == False
    assert candidate(2.583, 3.749, 4.738) == False
    assert candidate(12, 11, 1) == True
    assert candidate(3.211, 4, 3) == False
    assert candidate(1, 1, 7) == False
    assert candidate(0, 3, 3) == True
    assert candidate(1.157, 8, 2) == False
    assert candidate(3, 3, 6) == True
    assert candidate(4.272, 6.612, 6.663) == False
    assert candidate(1, 1, 2) == True
    assert candidate(2.2, 2.2, 2.2)==False
    assert candidate(3.158, 8, 6.135) == False
    assert candidate(1.346, 5, 6) == False
    assert candidate(15, 9, 6) == True
    assert candidate(1, 4, 5) == True
    assert candidate(7.656, 1, 7) == False
    assert candidate(3.599, 5, 1) == False
    assert candidate(3, 1, 2) == True
    assert candidate(-3, 2, 5) == True
    assert candidate(4, 11, 5) == False
    assert candidate(10, 7, 3) == True
    assert candidate(7, 3, 10) == True
    assert candidate(3, 4, 1) == True
    assert candidate(3.103, 3, 10) == False
    assert candidate(6, 16, 10) == True
    assert candidate(1.812, 6.567, 7.145) == False
    assert candidate(6, 6, 12) == True
    assert candidate(1, 7, 2) == False
    assert candidate(7, 6, 1) == True
    assert candidate(4, 3, 7) == True
    assert candidate(4, 6, 2) == True
    assert candidate(2.007, 9, 7.198) == False
    assert candidate(2, 3, 5) == True
    assert candidate(6.086, 4, 4) == False
    assert candidate(3.754, 6, 5.044) == False
    assert candidate(8, 10, 2) == True
    assert candidate(7.73, 5.041, 6.418) == False
    assert candidate(2, 6, 2)==False
    assert candidate(3.683, 8, 1.193) == False
    assert candidate(-4, 6, 2)==True
    assert candidate(7, 13, 6) == True
    assert candidate(2.003, 3, 11) == False
    assert candidate(3.357, 7, 8.074) == False
    assert candidate(3.621, 6.679, 2.542) == False
    assert candidate(12, 3, 9) == True
    assert candidate(7.797, 7, 4) == False
    assert candidate(7, 1, 8) == True
    assert candidate(5, 3, 8) == True
    assert candidate(5, 7, 2) == True
    assert candidate(5, 6, 11) == True
    assert candidate(6.681, 8, 4.747) == False
    assert candidate(3, 2, 5) == True
    assert candidate(3.0,4,7)==False
    assert candidate(9, 1, 10) == True
    assert candidate(1.5, 5, 3.5)==False
    assert candidate(2.834, 7, 9) == False
    assert candidate(2, 6, 4) == True
    assert candidate(6.068, 1, 3.454) == False
    assert candidate(1.834, 7.255, 6.304) == False
    assert candidate(1.726, 3, 1) == False
    assert candidate(13, 7, 6) == True
    assert candidate(6.9, 4, 12) == False
    assert candidate(4.039, 5, 5.992) == False
    assert candidate(4, 5, 9) == True
    assert candidate(6, 2, 7) == False
    assert candidate(3, 10, 7) == True
    assert candidate(5.586, 1, 2) == False
    assert candidate(12, 8, 4) == True
    assert candidate(2.459, 5, 11) == False
    assert candidate(0, 2, 2) == True
    assert candidate(6.175, 9, 4) == False
    assert candidate(12, 5, 7) == True
    assert candidate(8.854, 2, 8) == False
    assert candidate(2.858, 1, 2) == False
    assert candidate(4, 3, 1) == True
    assert candidate(4, 11, 1) == False
    assert candidate(5, 5, 10) == True
    assert candidate(10, 5, 5) == True
    assert candidate(3.228, 6, 6) == False
    assert candidate(2.805, 3, 6.418) == False
    assert candidate(2, 1, 1) == True
    assert candidate(6, 3, 3) == True
    assert candidate(7, 5, 12) == True
    assert candidate(-4, 11, 7) == True
    assert candidate(2,1,1)==True
    assert candidate(7, 2, 9) == True
    assert candidate(3.445, 2, 2) == False
    assert candidate(2, 7, 5) == True
    assert candidate(6.254, 6, 7) == False
    assert candidate(3.685, 2, 6) == False
    assert candidate(5, 9, 5) == False
    assert candidate(5.408, 8, 3.454) == False
    assert candidate(-7, 5, -2) == True
    assert candidate(4, 8, 4) == True
    assert candidate(12, 7, 5) == True
    assert candidate(4, 7, 3) == True
    assert candidate(6.61, 1.687, 2.647) == False
    assert candidate(3.033, 6.554, 7.391) == False
    assert candidate(2.08, 7, 1.239) == False

if __name__ == '__main__':
    check(any_int)