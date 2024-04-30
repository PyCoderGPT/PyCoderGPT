from case_MBPP_127 import insert_element


def check(candidate):
    assert candidate(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert candidate(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']
    assert candidate(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']

if __name__ == '__main__':
    check(insert_element)