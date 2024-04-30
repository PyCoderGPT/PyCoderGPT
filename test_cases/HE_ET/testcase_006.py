from case_HE_006 import parse_nested_parens


def check(candidate):
    assert candidate("((())()()) (()()) ((())) (((()))) (((()))) (()) ()") == [3, 2, 3, 4, 4, 2, 1]
    assert candidate("((())) () (()) (()()) ((())) ((())()())") == [3, 1, 2, 2, 3, 3]
    assert candidate("(((()))) ((())) ((())()()) (()) (()()) ((())) ((())) () () ((())()()) (()()) () (((()))) ((())()()) () (((()))) (((()))) ()") == [4, 3, 3, 2, 2, 3, 3, 1, 1, 3, 2, 1, 4, 3, 1, 4, 4, 1]
    assert candidate("((())) (((()))) ((())()()) (()()) () (((())))") == [3, 4, 3, 2, 1, 4]
    assert candidate("(()()) ((())) (()()) () () (()()) () ()") == [2, 3, 2, 1, 1, 2, 1, 1]
    assert candidate("((())) (()()) () ((())()()) () () ((())) ((())) (()()) () () (()())") == [3, 2, 1, 3, 1, 1, 3, 3, 2, 1, 1, 2]
    assert candidate("((())) (()()) ((())()()) ((())) (()()) () ((())()()) (()()) ((())()()) ((())) ((())) (()())") == [3, 2, 3, 3, 2, 1, 3, 2, 3, 3, 3, 2]
    assert candidate("((())) () (()(())((()))) (((()))) ((())) (()) () ((())) ((())) (()()) ((())()()) (()()) () (()) (((()))) (()) ((())) (((()))) ((())) ((())()()) ((())()())") == [3, 1, 4, 4, 3, 2, 1, 3, 3, 2, 3, 2, 1, 2, 4, 2, 3, 4, 3, 3, 3]
    assert candidate("((())) (()()) ((())()()) ((())()()) (()()) ((())) () () ((())) () () (()())") == [3, 2, 3, 3, 2, 3, 1, 1, 3, 1, 1, 2]
    assert candidate("((())()()) ((())) ((())) () () () () (()()) (()()) (()()) ((())()()) ()") == [3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 3, 1]
    assert candidate("(()()) (((()))) (()) ((())()()) () () ((())) ((())) (((()))) () (()()) (((())))") == [2, 4, 2, 3, 1, 1, 3, 3, 4, 1, 2, 4]
    assert candidate("(()()) ((())) ((())) ((())()())") == [2, 3, 3, 3]
    assert candidate("(()) ((())) (()) (()()) ((())()()) ((())()())") == [2, 3, 2, 2, 3, 3]
    assert candidate("((())) (()) (()()) ((())) (((()))) () ((())()()) ((())) (()()) (()()) (()) ((())()())") == [3, 2, 2, 3, 4, 1, 3, 3, 2, 2, 2, 3]
    assert candidate("((())) () ((())()()) ((())()()) (((()))) ((())()()) (((())))") == [3, 1, 3, 3, 4, 3, 4]
    assert candidate("(((()))) ((())) (()) ((())) () () () (((()))) (()()) (()()) (((()))) (()) (()) (((())))") == [4, 3, 2, 3, 1, 1, 1, 4, 2, 2, 4, 2, 2, 4]
    assert candidate("(((()))) (()) (()()) (()()) (()()) ((())) (((()))) (()(())((()))) (()) () (((()))) (()) ((())) (())") == [4, 2, 2, 2, 2, 3, 4, 4, 2, 1, 4, 2, 3, 2]
    assert candidate("(()()) (()) (()) (()()) (()()) (((()))) (()) (((()))) (()(())((()))) ((())) ((())) ((())()()) () (((())))") == [2, 2, 2, 2, 2, 4, 2, 4, 4, 3, 3, 3, 1, 4]
    assert candidate("(()(())((()))) ((())) (((()))) ((())()()) (()()) (()(())((()))) ((())()()) ((())) ((())) (()()) ((())()()) ((())) (()) (()(())((()))) () () (()(())((()))) (()()) (((()))) (((()))) ()") == [4, 3, 4, 3, 2, 4, 3, 3, 3, 2, 3, 3, 2, 4, 1, 1, 4, 2, 4, 4, 1]
    assert candidate("(()(())((()))) ((())) ((())) ((())) (()) (()(())((()))) () ((())) (((()))) (()) ((())) ((())) () (()(())((())))") == [4, 3, 3, 3, 2, 4, 1, 3, 4, 2, 3, 3, 1, 4]
    assert candidate("((())()()) (()()) () ((())) (()()) () ((())()()) ((())) ((())) ((())) ((())) ((()))") == [3, 2, 1, 3, 2, 1, 3, 3, 3, 3, 3, 3]
    assert candidate("(()) ((())()()) ((())()()) () (((()))) ((())()()) ((())()()) (()()) (()()) (()) ((())) (()())") == [2, 3, 3, 1, 4, 3, 3, 2, 2, 2, 3, 2]
    assert candidate("((())()()) (()(())((()))) (()) (()(())((()))) (((()))) (()(())((()))) (())") == [3, 4, 2, 4, 4, 4, 2]
    assert candidate("(()) (()) (()(())((()))) (()) (((()))) (((()))) ((())()())") == [2, 2, 4, 2, 4, 4, 3]
    assert candidate("(((()))) (()(())((()))) (()(())((()))) ((())()()) (((()))) (()(())((()))) ((())()())") == [4, 4, 4, 3, 4, 4, 3]
    assert candidate("() ((())) ((())()()) () ((())()()) (()()) () () ((())) (()()) ((())) ((())()())") == [1, 3, 3, 1, 3, 2, 1, 1, 3, 2, 3, 3]
    assert candidate("(()) (()()) ((())()()) (()()) () () ((())) () ((())()()) (((()))) (((()))) ()") == [2, 2, 3, 2, 1, 1, 3, 1, 3, 4, 4, 1]
    assert candidate("(()()) ((())()()) ((())) (()())") == [2, 3, 3, 2]
    assert candidate("((())()()) ((())) ((())()()) (()()) (()) ((())()()) (((()))) (((()))) ((())()()) ((())) ((())()()) () (()()) (()()) ((())()()) (()) ((())) ((())()())") == [3, 3, 3, 2, 2, 3, 4, 4, 3, 3, 3, 1, 2, 2, 3, 2, 3, 3]
    assert candidate("(()()) () (()()) (()())") == [2, 1, 2, 2]
    assert candidate("(((()))) ((())) () ((())()()) (()()) (()()) () ((())) ((())) (()()) (((()))) (()())") == [4, 3, 1, 3, 2, 2, 1, 3, 3, 2, 4, 2]
    assert candidate("((())()()) ((())) ((())()()) () ((())) (()()) ((())()()) (()())") == [3, 3, 3, 1, 3, 2, 3, 2]
    assert candidate("(()) ((())) ((())) ((())()()) () ((()))") == [2, 3, 3, 3, 1, 3]
    assert candidate("(()()) (()()) (()()) () () ((())) ((())()()) ()") == [2, 2, 2, 1, 1, 3, 3, 1]
    assert candidate("(()) (()(())((()))) ((())()()) (()()) (((()))) ((())()()) ((())()())") == [2, 4, 3, 2, 4, 3, 3]
    assert candidate("((())) () (((()))) (((()))) (()()) (((())))") == [3, 1, 4, 4, 2, 4]
    assert candidate("() ((())) () (()()) (((()))) ((())) (()()) () (()) (((()))) (()(())((()))) (((()))) (((()))) ()") == [1, 3, 1, 2, 4, 3, 2, 1, 2, 4, 4, 4, 4, 1]
    assert candidate("((())) ((())()()) () ((()))") == [3, 3, 1, 3]
    assert candidate("(()()) (()()) () ((()))") == [2, 2, 1, 3]
    assert candidate("(((()))) () (()) () (()) (())") == [4, 1, 2, 1, 2, 2]
    assert candidate("() ((())()()) () ((())) (()()) () () () () (()()) ((())) ((()))") == [1, 3, 1, 3, 2, 1, 1, 1, 1, 2, 3, 3]
    assert candidate("((())) ((())) (()()) (()()) ((())()()) ((())) ((())) ((())()())") == [3, 3, 2, 2, 3, 3, 3, 3]
    assert candidate("((())) () ((())()()) (((()))) (()) (((()))) () ((())) (()()) (()) (((()))) (()())") == [3, 1, 3, 4, 2, 4, 1, 3, 2, 2, 4, 2]
    assert candidate("(()()) (()) ((())) () () () ((()))") == [2, 2, 3, 1, 1, 1, 3]
    assert candidate("((())()()) (((()))) ((())()()) ((())) ((())()()) (())") == [3, 4, 3, 3, 3, 2]
    assert candidate("((())()()) ((())) ((())) (()()) ((())()()) () () ()") == [3, 3, 3, 2, 3, 1, 1, 1]
    assert candidate("(()()) (()()) () (()()) ((())()()) (()()) () (()()) ((())) () () (()())") == [2, 2, 1, 2, 3, 2, 1, 2, 3, 1, 1, 2]
    assert candidate("(()) (((()))) (()) (()) ((())) () ((())) ((())()()) ((())) (()) (()()) (((())))") == [2, 4, 2, 2, 3, 1, 3, 3, 3, 2, 2, 4]
    assert candidate("(((()))) (((()))) () (()()) ((())()()) () (()(())((()))) (()(())((()))) (()()) () (()()) (()) (()) ((())()())") == [4, 4, 1, 2, 3, 1, 4, 4, 2, 1, 2, 2, 2, 3]
    assert candidate("((())()()) (((()))) ((())) ((())) ((())) ((())()()) ((())()()) (()()) () () (()(())((()))) ((())) ((())()()) (()(())((()))) () ((())()()) (((()))) (((()))) (()(())((()))) ((())()()) ()") == [3, 4, 3, 3, 3, 3, 3, 2, 1, 1, 4, 3, 3, 4, 1, 3, 4, 4, 4, 3, 1]
    assert candidate("() ((())) ((())()()) ((())) () (()()) () (()())") == [1, 3, 3, 3, 1, 2, 1, 2]
    assert candidate("(()) (()()) () (()()) ((())()()) ((())) ((())) (()) ((())()()) () ((())()()) (()()) () (()) ((())) (()()) (()()) ((())()())") == [2, 2, 1, 2, 3, 3, 3, 2, 3, 1, 3, 2, 1, 2, 3, 2, 2, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate("(()()) (((()))) (((()))) (()) (()()) (((()))) () (((()))) (()) ((())) () ()") == [2, 4, 4, 2, 2, 4, 1, 4, 2, 3, 1, 1]
    assert candidate("(()()) (((()))) (((()))) (()()) (((()))) ((())) ((())()()) (()) ((())()()) (((()))) (()()) () (()) (((()))) () (()(())((()))) () (()) (()(())((()))) ((())) ((())()())") == [2, 4, 4, 2, 4, 3, 3, 2, 3, 4, 2, 1, 2, 4, 1, 4, 1, 2, 4, 3, 3]
    assert candidate("() (()(())((()))) (()) (()()) ((())()()) (()()) (()())") == [1, 4, 2, 2, 3, 2, 2]
    assert candidate("((())()()) (()(())((()))) (()()) (()()) ((())()()) (()()) ((())) () () (()()) (()(())((()))) ((())()()) (()()) ((())()()) (((()))) (()(())((()))) (()()) () ((())()()) ((())()()) ()") == [3, 4, 2, 2, 3, 2, 3, 1, 1, 2, 4, 3, 2, 3, 4, 4, 2, 1, 3, 3, 1]
    assert candidate("((())()()) () () (()()) (()()) (()()) ((())) (()())") == [3, 1, 1, 2, 2, 2, 3, 2]
    assert candidate("() ((())()()) (()()) (()) ((())()()) () (((()))) ((())()()) () (()) (()) ((())()()) (()) (()) (()) ((())) ((())) (((())))") == [1, 3, 2, 2, 3, 1, 4, 3, 1, 2, 2, 3, 2, 2, 2, 3, 3, 4]
    assert candidate("(()(())((()))) () (()(())((()))) (()) (((()))) ((())()()) ((())()()) ((())) ((())()()) (()(())((()))) ((())) (()(())((()))) ((())) ((())()())") == [4, 1, 4, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3]
    assert candidate("(()()) (((()))) () (()) (()) ((())) (()()) () () ((())()()) (()) ((()))") == [2, 4, 1, 2, 2, 3, 2, 1, 1, 3, 2, 3]
    assert candidate("(()) ((())()()) (()()) ((())()()) (((()))) (()()) (()(())((()))) (()()) (()(())((()))) ((())) (()) ((())) (()()) (()) (()()) () ((())) ((())) ((())) ((())) (()())") == [2, 3, 2, 3, 4, 2, 4, 2, 4, 3, 2, 3, 2, 2, 2, 1, 3, 3, 3, 3, 2]
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate("((())) ((())) ((())()()) ((())) ((())()()) ((())) () ()") == [3, 3, 3, 3, 3, 3, 1, 1]
    assert candidate("((())) (()()) () ((())()())") == [3, 2, 1, 3]
    assert candidate("((())()()) () (()()) ((())) (()()) () ((())()()) ((()))") == [3, 1, 2, 3, 2, 1, 3, 3]
    assert candidate("(((()))) () (()) (((()))) ((())) (()) ((())()()) ((())()()) () ((())()()) (()) ((())()())") == [4, 1, 2, 4, 3, 2, 3, 3, 1, 3, 2, 3]
    assert candidate("((())()()) () (()()) ((())) ((())()()) ((())()())") == [3, 1, 2, 3, 3, 3]
    assert candidate("((())()()) () ((())) () (()()) ((())) ((())()()) () () ((())()()) () (()())") == [3, 1, 3, 1, 2, 3, 3, 1, 1, 3, 1, 2]
    assert candidate("() ((())) (()()) (((()))) () ((())) (((()))) () (()) () () ((())()()) (()) (()()) ((())) (((()))) (()) (())") == [1, 3, 2, 4, 1, 3, 4, 1, 2, 1, 1, 3, 2, 2, 3, 4, 2, 2]
    assert candidate("((())()()) () ((())()()) ((())()()) ((())) () ((())()()) ((())) () ((())()()) (()()) (()())") == [3, 1, 3, 3, 3, 1, 3, 3, 1, 3, 2, 2]
    assert candidate("() (()()) ((())()()) (()(())((()))) (((()))) (()(())((()))) ((())()()) (()) (()()) (((()))) (()) (()) (()()) (((()))) (((()))) () (()) ((())) () (()) (()())") == [1, 2, 3, 4, 4, 4, 3, 2, 2, 4, 2, 2, 2, 4, 4, 1, 2, 3, 1, 2, 2]
    assert candidate("(((()))) () (((()))) (()()) ((())) () (()()) (((()))) (()()) (((()))) () ()") == [4, 1, 4, 2, 3, 1, 2, 4, 2, 4, 1, 1]
    assert candidate("(((()))) (()(())((()))) (()(())((()))) () (()) () ((())) (()) (()()) (((()))) ((())) () () (()) () () (()) () ((())) (()(())((()))) ((()))") == [4, 4, 4, 1, 2, 1, 3, 2, 2, 4, 3, 1, 1, 2, 1, 1, 2, 1, 3, 4, 3]
    assert candidate("(()) (()) (()()) ((())()()) (()) (()()) ((())) (()()) (()(())((()))) (()(())((()))) ((())()()) ((())) (((()))) (()(())((()))) ((())) ((())) (()(())((()))) () ((())) ((())) ((())()())") == [2, 2, 2, 3, 2, 2, 3, 2, 4, 4, 3, 3, 4, 4, 3, 3, 4, 1, 3, 3, 3]
    assert candidate("((())) () (()) ((())()()) (()()) ((())) (()) () () (((()))) (((()))) (())") == [3, 1, 2, 3, 2, 3, 2, 1, 1, 4, 4, 2]
    assert candidate("") == []
    assert candidate("((())()()) (()) (()()) ((())) () ((())) ((())()()) () () (()) (()) (((()))) (((()))) ((())) () () (()()) (())") == [3, 2, 2, 3, 1, 3, 3, 1, 1, 2, 2, 4, 4, 3, 1, 1, 2, 2]
    assert candidate("((())) ((())()()) ((())) (()()) ((())()()) () (()()) ((()))") == [3, 3, 3, 2, 3, 1, 2, 3]
    assert candidate("((())()()) ((())()()) ((())()()) ((())) (()()) ((())) ((())()()) ((())()()) ((())()()) () ((())) (()())") == [3, 3, 3, 3, 2, 3, 3, 3, 3, 1, 3, 2]
    assert candidate("((())()()) (()) () (((()))) ((())()()) ((())()()) (((()))) (()) (((()))) () (((()))) ((())()()) (()()) (()) (()) (()) () (())") == [3, 2, 1, 4, 3, 3, 4, 2, 4, 1, 4, 3, 2, 2, 2, 2, 1, 2]
    assert candidate("(()()) (()) ((())()()) ((())()()) () ((()))") == [2, 2, 3, 3, 1, 3]
    assert candidate("(()()) () ((())()()) () ((())) () ((())) ()") == [2, 1, 3, 1, 3, 1, 3, 1]
    assert candidate("((())) () (()()) ()") == [3, 1, 2, 1]
    assert candidate("((())) ((())) (()()) ((())()()) () ((())()()) ((())()()) ((())) (()()) ((())) () ((())()())") == [3, 3, 2, 3, 1, 3, 3, 3, 2, 3, 1, 3]
    assert candidate("(()()) () (()()) ((())) () ((())()()) (()()) ((())()())") == [2, 1, 2, 3, 1, 3, 2, 3]
    assert candidate("(((()))) (()) () ((())()()) (()()) () (()()) (()(())((()))) (()(())((()))) ((())) (((()))) (()(())((()))) ((())()()) ()") == [4, 2, 1, 3, 2, 1, 2, 4, 4, 3, 4, 4, 3, 1]
    assert candidate("(()()) (()()) () (()())") == [2, 2, 1, 2]
    assert candidate("((())) ((())) (((()))) (()) (()()) (()()) () ((())) ((())()()) () (()(())((()))) (()()) (()(())((()))) ((()))") == [3, 3, 4, 2, 2, 2, 1, 3, 3, 1, 4, 2, 4, 3]
    assert candidate("(()()) (()()) () (()) () (()()) (()) (()) (((()))) () (()()) (())") == [2, 2, 1, 2, 1, 2, 2, 2, 4, 1, 2, 2]
    assert candidate('(()(())((())))') == [4]
    assert candidate("((())) (()) (((()))) () (()()) (((()))) ((())()()) ((())) (()()) ((())()()) (((()))) ((())) (()) ((())) ((())) () ((())) ((())()())") == [3, 2, 4, 1, 2, 4, 3, 3, 2, 3, 4, 3, 2, 3, 3, 1, 3, 3]
    assert candidate("(()) ((())()()) (()) ((())) ((())) ((())()()) (((()))) () ((())()()) (()(())((()))) ((())) ((())()()) ((())()()) (())") == [2, 3, 2, 3, 3, 3, 4, 1, 3, 4, 3, 3, 3, 2]
    assert candidate("(()()) ((())()()) (()()) ()") == [2, 3, 2, 1]
    assert candidate("(()(())((()))) ((())()()) (((()))) (()(())((()))) () (()(())((()))) ()") == [4, 3, 4, 4, 1, 4, 1]
    assert candidate("((())) ((())) ((())()()) () ((())) ((())) (()()) ((())()()) (((()))) () (()) (((())))") == [3, 3, 3, 1, 3, 3, 2, 3, 4, 1, 2, 4]
    assert candidate("((())) (((()))) ((())) (()()) (()()) ((())()()) (()) (()(())((()))) (()) ((())) (()) ((())) () (((())))") == [3, 4, 3, 2, 2, 3, 2, 4, 2, 3, 2, 3, 1, 4]
    assert candidate("((())) ((())) ((())()()) (()()) () (()(())((()))) (()()) (((()))) (((()))) ((())()()) (()()) () () ((())) (((()))) (()(())((()))) (((()))) ((())()()) ((())) (()(())((()))) (())") == [3, 3, 3, 2, 1, 4, 2, 4, 4, 3, 2, 1, 1, 3, 4, 4, 4, 3, 3, 4, 2]
    assert candidate("(()) () (((()))) () (((()))) (()()) (()) (((()))) (()(())((()))) (((()))) () (()()) (()(())((()))) (()()) (()(())((()))) (()()) (((()))) (()()) (((()))) (()) (()())") == [2, 1, 4, 1, 4, 2, 2, 4, 4, 4, 1, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2]

if __name__ == '__main__':
    check(parse_nested_parens)