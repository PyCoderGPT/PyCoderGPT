from case_MBPP_046 import is_undulating


def check(candidate):
    assert candidate("1212121") == True
    assert candidate("1991") == False
    assert candidate("121") == True
    assert candidate("821762331") == False
    assert candidate("320097251") == False
    assert candidate("55719077819") == False
    assert candidate("4478552") == False
    assert candidate("50082161454") == False
    assert candidate("76309042") == False
    assert candidate("314190063970") == False
    assert candidate("053203291") == False
    assert candidate("888587793") == False
    assert candidate("59445720") == False
    assert candidate("052") == False
    assert candidate("4847") == False
    assert candidate("418122655672") == False
    assert candidate("098160505632") == False
    assert candidate("087763313") == False
    assert candidate("6938593744") == False
    assert candidate("0671521") == False
    assert candidate("23984320") == False
    assert candidate("991429723") == False
    assert candidate("4653235468") == False
    assert candidate("131") == True
    assert candidate("3615082") == False
    assert candidate("00150603") == False
    assert candidate("37029515") == False
    assert candidate("5334") == False
    assert candidate("3375") == False
    assert candidate("2874300525") == False
    assert candidate("728262022966") == False
    assert candidate("8655") == False
    assert candidate("48185883") == False
    assert candidate("67557280456") == False
    assert candidate("889831") == False
    assert candidate("3239") == False
    assert candidate("4299") == False
    assert candidate("003022") == False
    assert candidate("966482") == False
    assert candidate("1101") == False
    assert candidate("40058160") == False
    assert candidate("286") == False
    assert candidate("9406") == False
    assert candidate("416") == False
    assert candidate("07401") == False
    assert candidate("431") == False
    assert candidate("38598") == False
    assert candidate("67788") == False
    assert candidate("825023939") == False
    assert candidate("351648") == False
    assert candidate("0847445") == False
    assert candidate("30562741") == False
    assert candidate("6996") == False
    assert candidate("59780963") == False
    assert candidate("663186") == False
    assert candidate("57236") == False
    assert candidate("0117018") == False
    assert candidate("7246") == False
    assert candidate("9596") == False
    assert candidate("28479521") == False
    assert candidate("037337") == False
    assert candidate("90211773") == False
    assert candidate("42841516") == False
    assert candidate("6786510") == False
    assert candidate("81606339") == False
    assert candidate("092") == False
    assert candidate("15487") == False
    assert candidate("36532584") == False
    assert candidate("540971") == False
    assert candidate("646474411") == False
    assert candidate("6465105") == False
    assert candidate("01999") == False
    assert candidate("2630921") == False
    assert candidate("603") == False
    assert candidate("466014") == False
    assert candidate("8163") == False
    assert candidate("61148434") == False
    assert candidate("57064642") == False
    assert candidate("7597088") == False
    assert candidate("595") == True
    assert candidate("583718") == False
    assert candidate("97858") == False
    assert candidate("6789") == False
    assert candidate("80070069") == False
    assert candidate("53747500") == False
    assert candidate("31097") == False
    assert candidate("29666") == False
    assert candidate("3197532") == False
    assert candidate("927") == False
    assert candidate("975637") == False
    assert candidate("3554") == False
    assert candidate("983762") == False
    assert candidate("105") == False
    assert candidate("143388") == False
    assert candidate("594070") == False
    assert candidate("91004") == False
    assert candidate("508769546") == False
    assert candidate("531462") == False
    assert candidate("442362") == False
    assert candidate("775796") == False
    assert candidate("76487") == False
    assert candidate("283829") == False

if __name__ == '__main__':
    check(is_undulating)