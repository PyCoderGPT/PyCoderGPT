from case_MBPP_252 import drop_empty


def check(candidate):
    assert candidate({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    assert candidate({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
    assert candidate({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}

if __name__ == '__main__':
    check(drop_empty)