from case_MBPP_000 import similar_elements


def check(candidate):
    assert set(candidate((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
    assert set(candidate((1, 2, 3, 4),(5, 4, 3, 7))) == set((3, 4))
    assert set(candidate((11, 12, 14, 13),(17, 15, 14, 13))) == set((13, 14))

if __name__ == '__main__':
    check(similar_elements)