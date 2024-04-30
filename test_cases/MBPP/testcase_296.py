from case_MBPP_296 import polar_rect


def check(candidate):
    assert candidate(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    assert candidate(4,7)==((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
    assert candidate(15,17)==((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))

if __name__ == '__main__':
    check(polar_rect)