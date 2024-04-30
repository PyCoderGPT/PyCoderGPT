from case_HE_041 import car_race_collision


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


if __name__ == '__main__':
    check(car_race_collision)