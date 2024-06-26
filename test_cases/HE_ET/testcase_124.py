from case_HE_124 import valid_date


def check(candidate):
    assert candidate("152020823") == False
    assert candidate("15-2-6158") == False
    assert candidate("9~*&:@08@??1%=7") == False
    assert candidate('04-2003') == False
    assert candidate("10-15-2951") == True
    assert candidate("03-15-957") == True
    assert candidate("07-2-5707") == True
    assert candidate("00-10-1292") == False
    assert candidate("07-1-7237") == True
    assert candidate("03-27-2895") == True
    assert candidate("!-5?|/") == False
    assert candidate("#3:5?4+|3?=/5?3") == False
    assert candidate("02-3-4779") == True
    assert candidate("01-36-1682") == False
    assert candidate("tb") == False
    assert candidate("65?:!") == False
    assert candidate("!&5*~") == False
    assert candidate("496928724496") == False
    assert candidate("+81:37-8!8") == False
    assert candidate('04-31-3000') == False
    assert candidate("89728") == False
    assert candidate("17-29-6002") == False
    assert candidate("6%-2!/1$=") == False
    assert candidate("@86@2&*18-3!$4") == False
    assert candidate("%+5^74&^$?") == False
    assert candidate("/1|?@/#/|") == False
    assert candidate("3058229043") == False
    assert candidate("-6!@") == False
    assert candidate("17-13-2769") == False
    assert candidate("81346880") == False
    assert candidate("1|=@:") == False
    assert candidate("?2-5%21$:") == False
    assert candidate('21-31-2000') == False
    assert candidate("#~+18=") == False
    assert candidate("32|1@94") == False
    assert candidate("15-1-1527") == False
    assert candidate("dvt") == False
    assert candidate("8~8+*/") == False
    assert candidate("946216") == False
    assert candidate("$#7") == False
    assert candidate("*5:444%=62#-9") == False
    assert candidate("=8_2&-!3$~2/33") == False
    assert candidate('') == False
    assert candidate("@=6") == False
    assert candidate('15-01-2012') == False
    assert candidate("!?0|+1:|&=6?_2") == False
    assert candidate("9:|=+$6$#*5") == False
    assert candidate("787890") == False
    assert candidate("5+#$!@~02!~$4%7") == False
    assert candidate("01-12-7681") == True
    assert candidate("07-38-1109") == False
    assert candidate("/1:$/1*:6=!^5") == False
    assert candidate("x") == False
    assert candidate("%:*7^|4") == False
    assert candidate("12-37-5174") == False
    assert candidate('04-12-2003') == True
    assert candidate("%_%5|7-041144$:") == False
    assert candidate("09-37-3863") == False
    assert candidate("#0~!!&_3$^") == False
    assert candidate("907387") == False
    assert candidate("^$?@=#/_^6") == False
    assert candidate('01-01-2007') == True
    assert candidate('06-04-2020') == True
    assert candidate("09-26-7422") == True
    assert candidate("4%2_9:7@#:-4") == False
    assert candidate("!*^3%/*/|:^/!6") == False
    assert candidate('03-32-2011') == False
    assert candidate("05-3-4654") == True
    assert candidate("/*_#6$$:9!") == False
    assert candidate("8#012%7") == False
    assert candidate("00-33-325") == False
    assert candidate("07-24-6153") == True
    assert candidate("33&5$+??") == False
    assert candidate("142@6!4=/|@7") == False
    assert candidate("18-4-5532") == False
    assert candidate("j") == False
    assert candidate("*7:+3*0#~0") == False
    assert candidate("16-12-4616") == False
    assert candidate("19-32-6633") == False
    assert candidate("00-10-2109") == False
    assert candidate("$0:591=8:~:5/!") == False
    assert candidate("2=26~-~0") == False
    assert candidate("40/#70^") == False
    assert candidate("?/3~=!") == False
    assert candidate("qu") == False
    assert candidate("08-19-2738") == True
    assert candidate("19-19-1656") == False
    assert candidate('2003-04') == False
    assert candidate("05-14-1215") == True
    assert candidate("9739~4-_3510|3") == False
    assert candidate("18-36-13") == False
    assert candidate("03-38-9986") == False
    assert candidate("=-*9486") == False
    assert candidate("1^!?3+") == False
    assert candidate("76434488") == False
    assert candidate("11-36-6667") == False
    assert candidate("#?71-/#9:%91%77") == False
    assert candidate("04-17-4753") == True
    assert candidate("36924") == False
    assert candidate("467279042980") == False
    assert candidate("02-14-8921") == True
    assert candidate("$~@6$~") == False
    assert candidate("2/$7:471/!0#") == False
    assert candidate("_&4=$#1-*7*8/_") == False
    assert candidate("62@*%34#2") == False
    assert candidate("!?%!29&4-20-=") == False
    assert candidate("2118829671") == False
    assert candidate("09-40-5143") == False
    assert candidate("/4__8#01+") == False
    assert candidate("^-47?6_=%") == False
    assert candidate("?74^~@9/39") == False
    assert candidate("_9=+@_-+") == False
    assert candidate("+04&%2") == False
    assert candidate('03-11-2000') == True
    assert candidate("/26~%9$") == False
    assert candidate("aby") == False
    assert candidate("_-2%%=$+") == False
    assert candidate("xm") == False
    assert candidate("622654210301") == False
    assert candidate('06-06-2005') == True
    assert candidate("05-26-7803") == True
    assert candidate('2003-04-12') == False
    assert candidate("||&!%6%2_$&_9") == False
    assert candidate('20030412') == False
    assert candidate("04582") == False
    assert candidate("1~@") == False
    assert candidate("00-34-5915") == False
    assert candidate("596063116") == False
    assert candidate("09-26-6048") == True
    assert candidate('04-0-2040') == False
    assert candidate("?_2~634-6") == False
    assert candidate("^1*!^?") == False
    assert candidate("1&!56&!?:08%^+8") == False
    assert candidate("06-38-5638") == False
    assert candidate(":90:^=!*:+8+?") == False
    assert candidate('04122003') == False
    assert candidate("^/?$25") == False
    assert candidate("10-4-1092") == True
    assert candidate("3!8:99443^:94") == False
    assert candidate("19-24-2294") == False
    assert candidate("713472149") == False
    assert candidate(":8?@243|") == False
    assert candidate("12-14-575") == True

if __name__ == '__main__':
    check(valid_date)