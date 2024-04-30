from case_MBPP_179 import volume_cone


def check(candidate):
    assert math.isclose(candidate(5,12), 314.15926535897927, rel_tol=0.001)
    assert math.isclose(candidate(10,15), 1570.7963267948965, rel_tol=0.001)
    assert math.isclose(candidate(19,17), 6426.651371693521, rel_tol=0.001)

if __name__ == '__main__':
    check(volume_cone)