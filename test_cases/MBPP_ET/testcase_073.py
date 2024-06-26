from case_MBPP_073 import find_length


def check(candidate):
    assert candidate("11000010001", 11) == 6
    assert candidate("10111", 5) == 1
    assert candidate("11011101100101", 14) == 2 
    assert candidate('5588348', 6) == 0
    assert candidate('45731861915227', 12) == 0
    assert candidate('907379631930277', 15) == 1
    assert candidate('24805653973522', 7) == 1
    assert candidate('01968127', 6) == 1
    assert candidate('53278843141882', 13) == 0
    assert candidate('051535838', 9) == 1
    assert candidate('67750097667823', 13) == 2
    assert candidate('031601076722', 11) == 1
    assert candidate('74587544703542', 10) == 1
    assert candidate('816412', 6) == 0
    assert candidate('968443598849770', 9) == 0
    assert candidate('48962373866', 6) == 0
    assert candidate('1774711968602', 9) == 0
    assert candidate('9745499332161', 8) == 0
    assert candidate('335909428541161', 14) == 1
    assert candidate('818860663876799', 8) == 1
    assert candidate('43319697992', 6) == 0
    assert candidate('61098977642009', 13) == 2
    assert candidate('6481297882878', 12) == 0
    assert candidate('820564627', 9) == 1
    assert candidate('52387858203590', 6) == 0
    assert candidate('556672032292537', 7) == 1
    assert candidate('13462576303', 6) == 0
    assert candidate('369201833961953', 8) == 1
    assert candidate('281357464957', 6) == 0
    assert candidate('736506785752632', 13) == 1
    assert candidate('75676347893', 7) == 0
    assert candidate('428285974788', 11) == 0
    assert candidate('417906751', 9) == 1
    assert candidate('44426936870', 10) == 0
    assert candidate('72635020277123', 6) == 1
    assert candidate('0514092375', 9) == 1
    assert candidate('4616', 4) == 0
    assert candidate('424675959', 8) == 0
    assert candidate('007437765', 8) == 2
    assert candidate('2378', 2) == 0
    assert candidate('490500', 2) == 0
    assert candidate('055139795', 4) == 1
    assert candidate('492806663', 6) == 1
    assert candidate('176546957', 6) == 0
    assert candidate('8309844', 2) == 0
    assert candidate('578264', 1) == 0
    assert candidate('31412472', 3) == 0
    assert candidate('1560', 2) == 0
    assert candidate('42166840', 8) == 1
    assert candidate('41855', 4) == 0
    assert candidate('06683554', 3) == 1
    assert candidate('915428860', 4) == 0
    assert candidate('0020648', 2) == 2
    assert candidate('942012578', 6) == 1
    assert candidate('41478', 5) == 0
    assert candidate('7688309', 4) == 0
    assert candidate('95446', 3) == 0
    assert candidate('3223', 2) == 0
    assert candidate('5511', 3) == 0
    assert candidate('3194231', 3) == 0
    assert candidate('87422340', 7) == 0
    assert candidate('497500811', 3) == 0
    assert candidate('633330', 2) == 0
    assert candidate('946026', 2) == 0
    assert candidate('85233', 2) == 0
    assert candidate('763817065', 1) == 0
    assert candidate('8028', 4) == 1
    assert candidate('90567', 3) == 1
    assert candidate('294006461', 7) == 2
    assert candidate('431482860658913', 11) == 1
    assert candidate('4103231862329', 11) == 1
    assert candidate('1621676786766', 13) == 0
    assert candidate('04203487887279789', 15) == 1
    assert candidate('5870051729268', 10) == 2
    assert candidate('35543563452', 9) == 0
    assert candidate('4541441833', 9) == 0
    assert candidate('59156308187753', 11) == 1
    assert candidate('20722847473291751', 14) == 1
    assert candidate('3628991552078904', 13) == 1
    assert candidate('680913160474801', 11) == 1
    assert candidate('4329972590535168', 15) == 1
    assert candidate('93700680471473939', 17) == 2
    assert candidate('857433058461049176', 15) == 1
    assert candidate('784492065860560755', 9) == 1
    assert candidate('383455399704', 9) == 0
    assert candidate('6155982988321718', 10) == 0
    assert candidate('86816467754255', 11) == 0
    assert candidate('563877227299078467', 15) == 1
    assert candidate('748437162359', 11) == 0
    assert candidate('48260954493446', 9) == 1
    assert candidate('794709656688486', 15) == 1
    assert candidate('4703483866150187', 10) == 1
    assert candidate('643539974561599169', 9) == 0
    assert candidate('54123029135492', 13) == 1
    assert candidate('30893790725777850', 9) == 1
    assert candidate('411058807271518', 11) == 1
    assert candidate('185507887473953', 15) == 1
    assert candidate('820506037881404', 13) == 1
    assert candidate('672639283957529762', 14) == 0
    assert candidate('07033601245001171', 17) == 2
    assert candidate('08013861479211083', 16) == 1
    assert candidate('323429890831373880', 14) == 1

if __name__ == '__main__':
    check(find_length)