from case_MBPP_039 import surfacearea_sphere


def check(candidate):
    assert candidate(10)==1256.6370614359173
    assert candidate(15)==2827.4333882308138
    assert candidate(20)==5026.548245743669
    assert candidate(12) == 1809.5573684677208
    assert candidate(10) == 1256.6370614359173
    assert candidate(15) == 2827.4333882308138
    assert candidate(6) == 452.3893421169302
    assert candidate(9) == 1017.8760197630929
    assert candidate(13) == 2123.7166338267
    assert candidate(11) == 1520.5308443374597
    assert candidate(9) == 1017.8760197630929
    assert candidate(5) == 314.1592653589793
    assert candidate(9) == 1017.8760197630929
    assert candidate(15) == 2827.4333882308138
    assert candidate(11) == 1520.5308443374597
    assert candidate(8) == 804.247719318987
    assert candidate(10) == 1256.6370614359173
    assert candidate(13) == 2123.7166338267
    assert candidate(11) == 1520.5308443374597
    assert candidate(10) == 1256.6370614359173
    assert candidate(12) == 1809.5573684677208
    assert candidate(10) == 1256.6370614359173
    assert candidate(8) == 804.247719318987
    assert candidate(11) == 1520.5308443374597
    assert candidate(14) == 2463.0086404143976
    assert candidate(15) == 2827.4333882308138
    assert candidate(12) == 1809.5573684677208
    assert candidate(11) == 1520.5308443374597
    assert candidate(5) == 314.1592653589793
    assert candidate(5) == 314.1592653589793
    assert candidate(15) == 2827.4333882308138
    assert candidate(12) == 1809.5573684677208
    assert candidate(5) == 314.1592653589793
    assert candidate(14) == 2463.0086404143976
    assert candidate(8) == 804.247719318987
    assert candidate(8) == 804.247719318987
    assert candidate(17) == 3631.6811075498013
    assert candidate(13) == 2123.7166338267
    assert candidate(12) == 1809.5573684677208
    assert candidate(18) == 4071.5040790523717
    assert candidate(11) == 1520.5308443374597
    assert candidate(13) == 2123.7166338267
    assert candidate(17) == 3631.6811075498013
    assert candidate(13) == 2123.7166338267
    assert candidate(13) == 2123.7166338267
    assert candidate(17) == 3631.6811075498013
    assert candidate(20) == 5026.548245743669
    assert candidate(17) == 3631.6811075498013
    assert candidate(20) == 5026.548245743669
    assert candidate(14) == 2463.0086404143976
    assert candidate(10) == 1256.6370614359173
    assert candidate(18) == 4071.5040790523717
    assert candidate(14) == 2463.0086404143976
    assert candidate(13) == 2123.7166338267
    assert candidate(20) == 5026.548245743669
    assert candidate(16) == 3216.990877275948
    assert candidate(18) == 4071.5040790523717
    assert candidate(13) == 2123.7166338267
    assert candidate(17) == 3631.6811075498013
    assert candidate(19) == 4536.459791783661
    assert candidate(20) == 5026.548245743669
    assert candidate(18) == 4071.5040790523717
    assert candidate(17) == 3631.6811075498013
    assert candidate(16) == 3216.990877275948
    assert candidate(19) == 4536.459791783661
    assert candidate(13) == 2123.7166338267
    assert candidate(10) == 1256.6370614359173
    assert candidate(10) == 1256.6370614359173
    assert candidate(20) == 5026.548245743669
    assert candidate(19) == 4536.459791783661
    assert candidate(24) == 7238.229473870883
    assert candidate(23) == 6647.610054996002
    assert candidate(22) == 6082.123377349839
    assert candidate(19) == 4536.459791783661
    assert candidate(21) == 5541.769440932396
    assert candidate(18) == 4071.5040790523717
    assert candidate(20) == 5026.548245743669
    assert candidate(25) == 7853.981633974483
    assert candidate(23) == 6647.610054996002
    assert candidate(24) == 7238.229473870883
    assert candidate(15) == 2827.4333882308138
    assert candidate(19) == 4536.459791783661
    assert candidate(16) == 3216.990877275948
    assert candidate(17) == 3631.6811075498013
    assert candidate(18) == 4071.5040790523717
    assert candidate(16) == 3216.990877275948
    assert candidate(17) == 3631.6811075498013
    assert candidate(20) == 5026.548245743669
    assert candidate(17) == 3631.6811075498013
    assert candidate(20) == 5026.548245743669
    assert candidate(23) == 6647.610054996002
    assert candidate(19) == 4536.459791783661
    assert candidate(16) == 3216.990877275948
    assert candidate(17) == 3631.6811075498013
    assert candidate(18) == 4071.5040790523717
    assert candidate(21) == 5541.769440932396
    assert candidate(21) == 5541.769440932396
    assert candidate(16) == 3216.990877275948
    assert candidate(20) == 5026.548245743669
    assert candidate(17) == 3631.6811075498013
    assert candidate(25) == 7853.981633974483
    assert candidate(23) == 6647.610054996002

if __name__ == '__main__':
    check(surfacearea_sphere)