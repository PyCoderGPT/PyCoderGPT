from case_MBPP_072 import angle_complex


def check(candidate):
    assert candidate(0,1j)==1.5707963267948966 
    assert candidate(2,1j)==0.4636476090008061
    assert candidate(0,2j)==1.5707963267948966
    assert candidate(3, 8j) == 1.2120256565243244
    assert candidate(2, 2j) == 0.7853981633974483
    assert candidate(2, 4j) == 1.1071487177940904
    assert candidate(3, 5j) == 1.0303768265243125
    assert candidate(1, 6j) == 1.4056476493802699
    assert candidate(5, 3j) == 0.5404195002705842
    assert candidate(1, 6j) == 1.4056476493802699
    assert candidate(2, 3j) == 0.982793723247329
    assert candidate(2, 3j) == 0.982793723247329
    assert candidate(2, 3j) == 0.982793723247329
    assert candidate(1, 5j) == 1.373400766945016
    assert candidate(3, 4j) == 0.9272952180016122
    assert candidate(5, 4j) == 0.6747409422235526
    assert candidate(5, 8j) == 1.0121970114513341
    assert candidate(2, 2j) == 0.7853981633974483
    assert candidate(2, 2j) == 0.7853981633974483
    assert candidate(2, 2j) == 0.7853981633974483
    assert candidate(4, 5j) == 0.8960553845713439
    assert candidate(5, 4j) == 0.6747409422235526
    assert candidate(1, 5j) == 1.373400766945016
    assert candidate(1, 6j) == 1.4056476493802699
    assert candidate(4, 7j) == 1.0516502125483738
    assert candidate(2, 7j) == 1.2924966677897853
    assert candidate(1, 6j) == 1.4056476493802699
    assert candidate(2, 8j) == 1.3258176636680326
    assert candidate(2, 3j) == 0.982793723247329
    assert candidate(4, 2j) == 0.4636476090008061
    assert candidate(5, 4j) == 0.6747409422235526
    assert candidate(4, 4j) == 0.7853981633974483
    assert candidate(3, 2j) == 0.5880026035475675
    assert candidate(2, 3j) == 0.982793723247329
    assert candidate(5, 8j) == 1.0121970114513341
    assert candidate(5, 7j) == 0.9505468408120752
    assert candidate(5, 6j) == 0.8760580505981934
    assert candidate(4, 3j) == 0.6435011087932844
    assert candidate(2, 8j) == 1.3258176636680326
    assert candidate(5, 5j) == 0.7853981633974483
    assert candidate(2, 7j) == 1.2924966677897853
    assert candidate(4, 5j) == 0.8960553845713439
    assert candidate(6, 4j) == 0.5880026035475675
    assert candidate(3, 3j) == 0.7853981633974483
    assert candidate(7, 4j) == 0.5191461142465229
    assert candidate(2, 8j) == 1.3258176636680326
    assert candidate(7, 6j) == 0.7086262721276703
    assert candidate(2, 4j) == 1.1071487177940904
    assert candidate(3, 3j) == 0.7853981633974483
    assert candidate(4, 3j) == 0.6435011087932844
    assert candidate(1, 5j) == 1.373400766945016
    assert candidate(1, 3j) == 1.2490457723982544
    assert candidate(7, 6j) == 0.7086262721276703
    assert candidate(7, 4j) == 0.5191461142465229
    assert candidate(5, 5j) == 0.7853981633974483
    assert candidate(1, 8j) == 1.446441332248135
    assert candidate(7, 7j) == 0.7853981633974483
    assert candidate(6, 3j) == 0.4636476090008061
    assert candidate(6, 4j) == 0.5880026035475675
    assert candidate(4, 8j) == 1.1071487177940904
    assert candidate(4, 8j) == 1.1071487177940904
    assert candidate(4, 7j) == 1.0516502125483738
    assert candidate(3, 7j) == 1.1659045405098132
    assert candidate(7, 1j) == 0.14189705460416394
    assert candidate(7, 7j) == 0.7853981633974483
    assert candidate(1, 3j) == 1.2490457723982544
    assert candidate(5, 7j) == 0.9505468408120752
    assert candidate(5, 5j) == 0.7853981633974483
    assert candidate(3, 6j) == 1.1071487177940904
    assert candidate(1, 5j) == 1.373400766945016
    assert candidate(1, 2j) == 1.1071487177940904
    assert candidate(3, 2j) == 0.5880026035475675
    assert candidate(5, 8j) == 1.0121970114513341
    assert candidate(5, 8j) == 1.0121970114513341
    assert candidate(3, 2j) == 0.5880026035475675
    assert candidate(5, 5j) == 0.7853981633974483
    assert candidate(5, 6j) == 0.8760580505981934
    assert candidate(5, 7j) == 0.9505468408120752
    assert candidate(1, 5j) == 1.373400766945016
    assert candidate(3, 1j) == 0.3217505543966422
    assert candidate(1, 1j) == 0.7853981633974483
    assert candidate(3, 4j) == 0.9272952180016122
    assert candidate(3, 1j) == 0.3217505543966422
    assert candidate(1, 1j) == 0.7853981633974483
    assert candidate(3, 5j) == 1.0303768265243125
    assert candidate(5, 4j) == 0.6747409422235526
    assert candidate(1, 2j) == 1.1071487177940904
    assert candidate(5, 5j) == 0.7853981633974483
    assert candidate(2, 6j) == 1.2490457723982544
    assert candidate(1, 4j) == 1.3258176636680326
    assert candidate(1, 3j) == 1.2490457723982544
    assert candidate(2, 7j) == 1.2924966677897853
    assert candidate(3, 3j) == 0.7853981633974483
    assert candidate(1, 1j) == 0.7853981633974483
    assert candidate(5, 4j) == 0.6747409422235526
    assert candidate(4, 4j) == 0.7853981633974483
    assert candidate(3, 4j) == 0.9272952180016122
    assert candidate(4, 5j) == 0.8960553845713439
    assert candidate(3, 5j) == 1.0303768265243125
    assert candidate(4, 5j) == 0.8960553845713439
    assert candidate(3, 7j) == 1.1659045405098132
    assert candidate(4, 3j) == 0.6435011087932844

if __name__ == '__main__':
    check(angle_complex)