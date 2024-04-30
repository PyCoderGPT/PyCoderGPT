from case_HE_022 import filter_integers


def check(candidate):
    assert candidate([6, 'b', 3, 5, 'j', 'q']) == [6, 3, 5]
    assert candidate([6, {}, [], 18.909, 12, 'mbzxbij']) == [6, 12]
    assert candidate([2, {}, [], 18.424, 9, 'tjy']) == [2, 9]
    assert candidate([6, {}, [], 25.939, 13, 'cmhgop']) == [6, 13]
    assert candidate([7, 'o', 4, 7, 'c', 't']) == [7, 4, 7]
    assert candidate([3, 'w', 4, 2, 'l', 'l']) == [3, 4, 2]
    assert candidate([2, {}, [], 26.863, 8, 'zxn']) == [2, 8]
    assert candidate([2, 'z', 8, 1, 'r', 'y']) == [2, 8, 1]
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]
    assert candidate([2, 'c', 5, 7, 'r', 'f']) == [2, 5, 7]
    assert candidate([8, 'o', 3, 2, 'a', 'i']) == [8, 3, 2]
    assert candidate([6, {}, [], 27.436, 6, 'hho']) == [6, 6]
    assert candidate([4, {}, [], 25.808, 14, 'caqzpanje']) == [4, 14]
    assert candidate([4, {}, [], 26.185, 5, 'axoflvgka']) == [4, 5]
    assert candidate([2, 'a', 5, 7, 'e', 's']) == [2, 5, 7]
    assert candidate([1, {}, [], 20.647, 8, 'pkziwunmr']) == [1, 8]
    assert candidate([7, 'n', 7, 5, 'h', 'n']) == [7, 7, 5]
    assert candidate([1, {}, [], 27.919, 6, 'nuocpan']) == [1, 6]
    assert candidate([3, 'x', 3, 8, 'k', 'j']) == [3, 3, 8]
    assert candidate([1, {}, [], 24.526, 4, 'picjtngpl']) == [1, 4]
    assert candidate([3, {}, [], 18.073, 5, 'tuhq']) == [3, 5]
    assert candidate([5, 'o', 5, 6, 'u', 'd']) == [5, 5, 6]
    assert candidate([8, 'v', 5, 7, 'h', 'x']) == [8, 5, 7]
    assert candidate([5, {}, [], 22.736, 9, 'exui']) == [5, 9]
    assert candidate([6, {}, [], 21.822, 5, 'kdkmktk']) == [6, 5]
    assert candidate([3, {}, [], 22.267, 11, 'lwwqfh']) == [3, 11]
    assert candidate([7, {}, [], 28.243, 5, 'ksxclwb']) == [7, 5]
    assert candidate([5, {}, [], 19.22, 10, 'lynj']) == [5, 10]
    assert candidate([4, 'm', 6, 3, 'i', 'g']) == [4, 6, 3]
    assert candidate([4, {}, [], 28.709, 9, 'mkhbja']) == [4, 9]
    assert candidate([4, {}, [], 22.761, 12, 'pcjdigsyd']) == [4, 12]
    assert candidate([8, 'l', 5, 3, 't', 'j']) == [8, 5, 3]
    assert candidate([4, 'i', 6, 6, 'h', 'm']) == [4, 6, 6]
    assert candidate([6, {}, [], 19.651, 11, 'mgvuao']) == [6, 11]
    assert candidate([7, {}, [], 20.427, 12, 'ylxey']) == [7, 12]
    assert candidate([4, {}, [], 22.65, 11, 'eygiqau']) == [4, 11]
    assert candidate([7, {}, [], 20.658, 13, 'vpg']) == [7, 13]
    assert candidate([1, 'u', 8, 4, 'b', 'p']) == [1, 8, 4]
    assert candidate([8, 'j', 8, 8, 'l', 'f']) == [8, 8, 8]
    assert candidate([8, {}, [], 21.99, 6, 'fnu']) == [8, 6]
    assert candidate([2, {}, [], 28.929, 8, 'hthtwa']) == [2, 8]
    assert candidate([6, 'z', 7, 7, 'k', 'q']) == [6, 7, 7]
    assert candidate([5, {}, [], 20.827, 6, 'wqmdbaxm']) == [5, 6]
    assert candidate([2, 'a', 8, 6, 'h', 'i']) == [2, 8, 6]
    assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
    assert candidate([4, 'k', 1, 3, 'v', 'v']) == [4, 1, 3]
    assert candidate([6, 'p', 4, 2, 'l', 'j']) == [6, 4, 2]
    assert candidate([7, {}, [], 26.016, 7, 'beuwntqbp']) == [7, 7]
    assert candidate([8, 's', 7, 6, 'r', 'e']) == [8, 7, 6]
    assert candidate([7, 'k', 5, 4, 'u', 's']) == [7, 5, 4]
    assert candidate([8, {}, [], 19.9, 5, 'yvdtml']) == [8, 5]
    assert candidate([2, 'd', 8, 2, 'r', 'x']) == [2, 8, 2]
    assert candidate([8, 't', 2, 4, 'l', 'r']) == [8, 2, 4]
    assert candidate([8, 'z', 1, 6, 's', 'n']) == [8, 1, 6]
    assert candidate([1, {}, [], 19.564, 10, 'qwgs']) == [1, 10]
    assert candidate([7, {}, [], 24.761, 12, 'kzqs']) == [7, 12]
    assert candidate([8, 'j', 4, 5, 's', 'j']) == [8, 4, 5]
    assert candidate([3, 'k', 4, 6, 'o', 'k']) == [3, 4, 6]
    assert candidate([7, {}, [], 22.394, 8, 'jyeaj']) == [7, 8]
    assert candidate([2, {}, [], 23.928, 13, 'uwqe']) == [2, 13]
    assert candidate([4, 'p', 7, 5, 'a', 'd']) == [4, 7, 5]
    assert candidate([5, {}, [], 18.807, 12, 'nagicj']) == [5, 12]
    assert candidate([4, {}, [], 23.515, 6, 'tvfbrqn']) == [4, 6]
    assert candidate([8, 'x', 4, 1, 'c', 'd']) == [8, 4, 1]
    assert candidate([2, {}, [], 26.176, 8, 'hgbees']) == [2, 8]
    assert candidate([]) == []
    assert candidate([3, {}, [], 24.279, 12, 'mxqjmkgod']) == [3, 12]
    assert candidate([1, 'e', 4, 7, 'i', 'p']) == [1, 4, 7]
    assert candidate([4, {}, [], 20.506, 5, 'ismsmeo']) == [4, 5]
    assert candidate([7, {}, [], 19.691, 6, 'bfic']) == [7, 6]
    assert candidate([4, 'y', 6, 2, 'b', 'i']) == [4, 6, 2]
    assert candidate([4, 'x', 5, 4, 'u', 'd']) == [4, 5, 4]
    assert candidate([5, {}, [], 22.556, 14, 'fkm']) == [5, 14]
    assert candidate([5, 'p', 1, 1, 'm', 'p']) == [5, 1, 1]
    assert candidate([8, 'a', 7, 8, 'r', 'z']) == [8, 7, 8]
    assert candidate([9, {}, [], 21.928, 10, 'xomljymzc']) == [9, 10]
    assert candidate([8, {}, [], 20.381, 14, 'ognzwbuya']) == [8, 14]
    assert candidate([3, 'w', 3, 8, 'z', 'm']) == [3, 3, 8]
    assert candidate([8, 'k', 3, 4, 'e', 'l']) == [8, 3, 4]
    assert candidate([3, {}, [], 18.128, 12, 'gru']) == [3, 12]
    assert candidate([8, 'a', 7, 6, 'x', 'l']) == [8, 7, 6]
    assert candidate([5, 'g', 2, 5, 's', 'u']) == [5, 2, 5]
    assert candidate([7, 's', 5, 7, 'd', 't']) == [7, 5, 7]
    assert candidate([2, 'm', 2, 2, 'y', 'k']) == [2, 2, 2]
    assert candidate([5, 'i', 3, 8, 'u', 'u']) == [5, 3, 8]
    assert candidate([9, {}, [], 24.691, 12, 'emo']) == [9, 12]
    assert candidate([6, 'r', 6, 3, 'c', 'k']) == [6, 6, 3]

if __name__ == '__main__':
    check(filter_integers)