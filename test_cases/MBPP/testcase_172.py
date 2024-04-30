from case_MBPP_172 import start_withp


def check(candidate):
    assert candidate(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert candidate(["Python Programming","Java Programming"])==('Python','Programming')
    assert candidate(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

if __name__ == '__main__':
    check(start_withp)