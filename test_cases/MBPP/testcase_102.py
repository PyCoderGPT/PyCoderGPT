from case_MBPP_102 import count_occurance


def check(candidate):
    assert candidate("letstdlenstdporstd") == 3
    assert candidate("truststdsolensporsd") == 1
    assert candidate("makestdsostdworthit") == 2
    assert candidate("stds") == 1
    assert candidate("") == 0

if __name__ == '__main__':
    check(count_occurance)