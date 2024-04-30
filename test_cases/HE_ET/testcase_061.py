from case_HE_061 import correct_bracketing


def check(candidate):
    assert candidate("(") == False
    assert candidate("))()))((())((()()((((") == False
    assert candidate(")((((((()())())()(((") == False
    assert candidate(")((())))()(()))())") == False
    assert not candidate("(()")
    assert candidate("(()())") == True
    assert candidate("(()())()()((()()())())(()()(()))()") == True
    assert candidate("()))") == False
    assert not candidate(")")
    assert candidate("()()") == True
    assert candidate(")())()())))(((") == False
    assert candidate("))((((((()") == False
    assert candidate(")((((") == False
    assert candidate("()(()())") == True
    assert candidate("(()())()()((()()())())(()()(()))") == True
    assert candidate("((())()))") == False
    assert candidate("()()()(())(") == False
    assert candidate("))())") == False
    assert candidate("()()(()())()")
    assert candidate("()()(()())()") == True
    assert candidate(")") == False
    assert candidate("()()()") == True
    assert candidate("()))()(") == False
    assert candidate("(())") == True
    assert candidate("()()(()())()()()(()())()") == True
    assert candidate("()()(()())()()()(()())()()()((()()())())(()()(()))") == True
    assert candidate("(()())()(()())") == True
    assert candidate("(()))))()") == False
    assert candidate(")(()())(") == False
    assert candidate("((((") == False
    assert candidate("(()())")
    assert candidate("(((()") == False
    assert candidate("))()") == False
    assert candidate(")))((") == False
    assert candidate(")()())") == False
    assert candidate("(()") == False
    assert candidate("(()())(()())()") == True
    assert candidate("(()())()()(()())()") == True
    assert candidate("()()(()())()(()())()") == True
    assert not candidate("((((")
    assert candidate("))))") == False
    assert candidate("()") == True
    assert candidate("())") == False
    assert candidate(")()(())()((()())") == False
    assert candidate("))()))))(()()(") == False
    assert candidate("()())())(") == False
    assert candidate("()()()()(()())()") == True
    assert candidate(")()(") == False
    assert candidate("((((((") == False
    assert candidate("()()()((()()(") == False
    assert candidate("()()((()()())())(()()(()))()()(()())()()") == True
    assert not candidate("((()())))")
    assert candidate("()")
    assert not candidate("(")
    assert candidate("())())((()()))") == False
    assert candidate("(()())()") == True
    assert candidate(")(()))(((()((()") == False
    assert candidate("()))))") == False
    assert candidate("))())()))(())") == False
    assert candidate(")())())()") == False
    assert candidate(")((()))))((()(") == False
    assert candidate("()())())))(()(())()") == False
    assert candidate(")((((((") == False
    assert not candidate(")(()")
    assert candidate("((())()()") == False
    assert not candidate("()()(()())()))()")
    assert candidate(")(()(())((())((())") == False
    assert candidate(")(()") == False
    assert candidate(")()") == False
    assert candidate("()()(()())()()()((()()())())(()()(()))(()())") == True
    assert candidate("()()(()())()()") == True
    assert candidate("(()())()()((()()())())(()()(()))(()())") == True
    assert candidate("()()((()()())())(()()(()))")
    assert candidate("(((") == False
    assert candidate("") == True
    assert not candidate("()()(()())())(()")
    assert candidate("()(())()()()") == True
    assert candidate(")()()(()(())(") == False
    assert candidate("))()()())(())") == False

if __name__ == '__main__':
    check(correct_bracketing)