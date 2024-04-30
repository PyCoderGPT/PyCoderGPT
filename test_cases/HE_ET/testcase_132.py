from case_HE_132 import is_nested


def check(candidate):
    assert candidate('[[]') == False
    assert candidate("[]]]][[]") == False
    assert candidate('[]]]]]]][[[[[]') == False
    assert candidate("][[[[]]") == True
    assert candidate("[][[][][") == True
    assert candidate(('[]')) == False
    assert candidate("[][][[[[[]]") == True
    assert candidate('[[]][[') == True
    assert candidate("][][[") == False
    assert candidate('') == False
    assert candidate("[]][") == False
    assert candidate("][][][]]]") == True
    assert candidate("]][[[[][][]") == True
    assert candidate("[[[]][][[") == True
    assert candidate("b") == False
    assert candidate("][][][]") == True
    assert candidate("[[[][]]][") == True
    assert candidate("][]]]]]]]") == False
    assert candidate("[][[[]") == False
    assert candidate("]][][]]") == True
    assert candidate('[][][[]]') == True
    assert candidate("[]]][[[") == False
    assert candidate("[]][[[[]]") == True
    assert candidate("][][[][]") == True
    assert candidate("[][[]") == False
    assert candidate('[[[[[[[[') == False
    assert candidate("]]]]][][]][[[]") == True
    assert candidate("][[]]") == True
    assert candidate("][]]][][[][]") == True
    assert candidate("]]]][[]][") == True
    assert candidate("][[][]") == True
    assert candidate('[[]]') == True
    assert candidate("[]]]][") == False
    assert candidate("gv") == False
    assert candidate("[[[[][[[") == False
    assert candidate("]][][][]]") == True
    assert candidate("]]]][][]]]]") == True
    assert candidate("][]]]][[]]") == True
    assert candidate("][[[") == False
    assert candidate("][[[]]]") == True
    assert candidate("[[][]") == True
    assert candidate("][[[]") == False
    assert candidate("][]][]") == False
    assert candidate("]]][") == False
    assert candidate("[[[[]]][[[[]") == True
    assert candidate("ol") == False
    assert candidate("][[][][[") == True
    assert candidate("][[]]]") == True
    assert candidate("]][[") == False
    assert candidate("][]]") == False
    assert candidate("][][]][[[") == True
    assert candidate("ljv") == False
    assert candidate('[[[[]]]]') == True
    assert candidate("]]][[") == False
    assert candidate("[]]]]") == False
    assert candidate("][[]") == False
    assert candidate("][]]]]") == False
    assert candidate("]][[]]]][[][") == True
    assert candidate("][[][[]") == True
    assert candidate("[[[[[][][[") == True
    assert candidate("][]][][") == False
    assert candidate("adx") == False
    assert candidate("][]][") == False
    assert candidate("[[]][][]]") == True
    assert candidate("[][[[]][]]]") == True
    assert candidate("][[[]][") == True
    assert candidate("]]]") == False
    assert candidate("][[]]][][]][") == True
    assert candidate("[[]]]") == True
    assert candidate("uh") == False
    assert candidate("]][]][[][") == False
    assert candidate("]]]]]][]") == False
    assert candidate("]]]]]") == False
    assert candidate(']]]]]]]]') == False
    assert candidate("[]]][[]][") == True
    assert candidate("[[][]]]]") == True
    assert candidate("[]][][[]]") == True
    assert candidate("][]]][][]]") == True
    assert candidate("[]]][[[[[]") == False
    assert candidate("]]]]]][[[") == False
    assert candidate("]]][[][[[") == False
    assert candidate("]]][]]]]][[[][[") == False
    assert candidate("[[[[][") == False
    assert candidate("[][]][[[]][[[][") == True
    assert candidate("[[[]]]") == True
    assert candidate("]][]][]]][") == True
    assert candidate("[[][][]") == True
    assert candidate('[][]') == False
    assert candidate("]][") == False
    assert candidate("[]][[]]]") == True
    assert candidate("[][]]") == True
    assert candidate("][[") == False
    assert candidate("]][][[") == False
    assert candidate("]]][[]][][]][[][]]") == True
    assert candidate("]][[[[") == False
    assert candidate("]]][][[[[][]]") == True
    assert candidate("][[]][[[[") == True
    assert candidate("c") == False
    assert candidate("]][[]]") == True
    assert candidate("[]][][][]") == True
    assert candidate("][]][[[") == False
    assert candidate("[]]]][[]]][][]") == True
    assert candidate("]]]][[[[") == False
    assert candidate("[[[[[[[[][]]") == True
    assert candidate("[][][[") == False
    assert candidate("][[][[[[") == False
    assert candidate("]]]][]") == False
    assert candidate("]][[[][][[[") == True
    assert candidate("[[[[[[") == False
    assert candidate("[][[") == False
    assert candidate('[]]]]]]]]]]') == False
    assert candidate('[[][]]') == True

    # Check some edge cases that are easy to work out by hand.
    assert candidate("[][[][]]]]") == True
    assert candidate('[]]') == False
    assert candidate("][]]][[") == False
    assert candidate("[][[][[][") == True
    assert candidate("[]][[") == False
    assert candidate("[][]][]][") == True
    assert candidate("[[]][[") == True
    assert candidate("[[[[]]][[[[[") == True
    assert candidate("uz") == False
    assert candidate("]][]]]]") == False
    assert candidate("[[[]][][][]") == True
    assert candidate("]]][[]][[") == True
    assert candidate("[]][]") == False
    assert candidate("[][][[[[[][") == True
    assert candidate("h") == False
    assert candidate("[]]]]][[]") == False

if __name__ == '__main__':
    check(is_nested)