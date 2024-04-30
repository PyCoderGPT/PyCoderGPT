from case_MBPP_048 import index_minimum


def check(candidate):
    assert candidate([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert candidate([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert candidate([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'

if __name__ == '__main__':
    check(index_minimum)