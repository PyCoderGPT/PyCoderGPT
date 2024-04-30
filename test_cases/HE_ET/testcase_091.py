from case_HE_091 import is_bored


def check(candidate):
    assert candidate("Hello I sky blue? I") == 0
    assert candidate("I I I . I I the . I be I I") == 3
    assert candidate("I I I Is I") == 1
    assert candidate("I I Hello") == 1
    assert candidate("bIt I") == 0
    assert candidate("walk I I I I I be I I") == 0
    assert candidate("world world Hello") == 0
    assert candidate("Is I I I the") == 0
    assert candidate("love . today. . bIt . I I .") == 1
    assert candidate("world world I") == 0
    assert candidate("world I Hello") == 0
    assert candidate("I It Is I I") == 1
    assert candidate("I blue? the Hello I") == 1
    assert candidate("I I . . sky I I I I be will I") == 1
    assert candidate("I . blue? . I I . I I I I I") == 3
    assert candidate("blue? I world blue? I") == 1
    assert candidate("sky I ! I I") == 1
    assert candidate("I . . I I I a I kill") == 2
    assert candidate("I . I I I . be I I I I I") == 2
    assert candidate("Hello I I I I I I I I be ! I") == 0
    assert candidate("sky I I sky I") == 0
    assert candidate("I I kill I I I . I I") == 2
    assert candidate("You and I are going for a walk") == 0, "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("I the . I world") == 2
    assert candidate("I . going I I I I I .") == 1
    assert candidate("I feel good today. I will be productive. will kill It") == 2, "Test 5"
    assert candidate("I I I I Hello") == 1
    assert candidate("I I I I I I I It . I I I") == 2
    assert candidate("I I world") == 1
    assert candidate("I . I I I I I It I") == 2
    assert candidate("I I I Is .") == 1
    assert candidate("I . . I I I world I .") == 2
    assert candidate("the . the blue? .") == 0
    assert candidate("I I I . I going I I I") == 2
    assert candidate("blue? I I blue? I") == 1
    assert candidate("I . the I It I . I I feel I I") == 2
    assert candidate("I I world I I . are I .") == 1
    assert candidate("Hello . I I will I I I I") == 1
    assert candidate("I I I I walk for . I productive.") == 2
    assert candidate("sky . I . I") == 1
    assert candidate("sky I I I Hello") == 0
    assert candidate("I blue? Is . Hello") == 1
    assert candidate("I .") == 1
    assert candidate("I Hello . I I") == 2
    assert candidate("I be I I I I I I . Hello I I") == 1
    assert candidate("world I .") == 0
    assert candidate("I I I") == 1
    assert candidate("I I love sky I . I I I I . productive.") == 2
    assert candidate("! .") == 0
    assert candidate("kill . I I the . I I blue? be productive. .") == 2
    assert candidate("sky I I the .") == 0
    assert candidate("I sky I . blue?") == 1
    assert candidate("I be I I Is . . . I Hello . I") == 2
    assert candidate("Is I") == 0
    assert candidate("I the world I It") == 1
    assert candidate("sky I I I I") == 0
    assert candidate("world . I") == 0
    assert candidate("the I I . the") == 0
    assert candidate("Is the sky blue?") == 0, "Test 2"
    assert candidate("Is I It I I") == 0
    assert candidate("the .") == 0
    assert candidate("productive. world productive. I . I I feel productive. I I I") == 3
    assert candidate("I I I I I It I I . world I I") == 1
    assert candidate("I I . I I") == 2
    assert candidate("Hello I .") == 0
    assert candidate("I It I I I . I I I . I I") == 3
    assert candidate("world I") == 0
    assert candidate("I I . I . I I a I") == 3
    assert candidate("I I I I . I . I I") == 3
    assert candidate("I . . I world") == 2
    assert candidate("I sky I I I") == 1
    assert candidate("I I I . . blue? bIt . . I good kill") == 2
    assert candidate("Hello I I . I") == 0
    assert candidate("Hello . I") == 0
    assert candidate("I . . I today. I I I will I . I") == 3
    assert candidate("I I I I kill I I for I") == 1
    assert candidate("the Is the . I") == 0
    assert candidate("I I I will I I . I I today. the I") == 2
    assert candidate("sky blue? I sky sky") == 1
    assert candidate("I . world") == 1
    assert candidate("I I I . I I I . I I I I") == 3
    assert candidate("I I I . . I . blue? I") == 2
    assert candidate("I I I . I") == 1
    assert candidate("bIt") == 0, "Test 4"
    assert candidate("I I world . sky") == 1
    assert candidate("Hello I Hello") == 0
    assert candidate("Hello Hello love . blue?") == 0
    assert candidate("Hello world") == 0, "Test 1"
    assert candidate("world . world") == 0
    assert candidate("Hello world world") == 0
    assert candidate("I love It !") == 1, "Test 3"
    assert candidate("I Hello Hello") == 1
    assert candidate("It I") == 0
    assert candidate("I blue? I Is .") == 2
    assert candidate("I Hello I") == 1
    assert candidate("I I") == 1
    assert candidate("I I . I I I I I .") == 2
    assert candidate("I I I I I I I I .") == 1
    assert candidate("I . I I !") == 2
    assert candidate("I ! I . sky") == 2
    assert candidate("I I I I I I I I I") == 1
    assert candidate("I kill I I I blue? I good I productive. I I") == 3
    assert candidate("I good I I I sky world I .") == 1
    assert candidate("I I I . I be I I . I will I") == 3
    assert candidate("world It I It I") == 0
    assert candidate("I I I I I a I . .") == 1
    assert candidate("world I world") == 0

if __name__ == '__main__':
    check(is_bored)