from case_MBPP_002 import heap_queue_largest


def check(candidate):
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75]
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]

if __name__ == '__main__':
    check(heap_queue_largest)