from case_MBPP_182 import add_string


def check(candidate):
    assert candidate([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
    assert candidate(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
    assert candidate([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']

if __name__ == '__main__':
    check(add_string)