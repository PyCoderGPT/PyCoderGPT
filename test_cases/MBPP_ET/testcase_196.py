from case_MBPP_196 import find_Parity


def check(candidate):
    assert candidate(12) == "Even Parity"
    assert candidate(7) == "Odd Parity"
    assert candidate(10) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(14) == "Odd Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(12) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(17) == "Even Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(16) == "Odd Parity"
    assert candidate(14) == "Odd Parity"
    assert candidate(10) == "Even Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(12) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(12) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(17) == "Even Parity"
    assert candidate(10) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(7) == "Odd Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(14) == "Odd Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(17) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(3) == "Even Parity"
    assert candidate(6) == "Even Parity"
    assert candidate(4) == "Odd Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(3) == "Even Parity"
    assert candidate(5) == "Even Parity"
    assert candidate(7) == "Odd Parity"
    assert candidate(4) == "Odd Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(5) == "Even Parity"
    assert candidate(4) == "Odd Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(3) == "Even Parity"
    assert candidate(2) == "Odd Parity"
    assert candidate(3) == "Even Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(4) == "Odd Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(3) == "Even Parity"
    assert candidate(2) == "Odd Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(4) == "Odd Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(7) == "Odd Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(12) == "Even Parity"
    assert candidate(10) == "Even Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(5) == "Even Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(14) == "Odd Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(14) == "Odd Parity"
    assert candidate(8) == "Odd Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(6) == "Even Parity"
    assert candidate(10) == "Even Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(12) == "Even Parity"
    assert candidate(11) == "Odd Parity"
    assert candidate(6) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(15) == "Even Parity"
    assert candidate(10) == "Even Parity"
    assert candidate(6) == "Even Parity"
    assert candidate(7) == "Odd Parity"
    assert candidate(12) == "Even Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(12) == "Even Parity"
    assert candidate(9) == "Even Parity"
    assert candidate(6) == "Even Parity"
    assert candidate(13) == "Odd Parity"
    assert candidate(13) == "Odd Parity"

if __name__ == '__main__':
    check(find_Parity)