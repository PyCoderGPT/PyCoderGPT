from case_MBPP_326 import is_upper


def check(candidate):
    assert candidate("person") =="PERSON"
    assert candidate("final") == "FINAL"
    assert candidate("Valid") == "VALID"

if __name__ == '__main__':
    check(is_upper)