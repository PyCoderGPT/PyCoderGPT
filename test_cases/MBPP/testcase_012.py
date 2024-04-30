from case_MBPP_012 import remove_dirty_chars


def check(candidate):
    assert candidate("probasscurve", "pros") == 'bacuve'
    assert candidate("digitalindia", "talent") == 'digiidi'
    assert candidate("exoticmiles", "toxic") == 'emles'

if __name__ == '__main__':
    check(remove_dirty_chars)