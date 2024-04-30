from case_MBPP_322 import move_num


def check(candidate):
    assert candidate('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert candidate('Avengers124Assemble') == 'AvengersAssemble124'
    assert candidate('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

if __name__ == '__main__':
    check(move_num)