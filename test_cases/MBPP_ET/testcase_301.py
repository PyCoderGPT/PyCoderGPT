from case_MBPP_301 import min_Swaps


def check(candidate):
    assert candidate("1101","1110") == 1
    assert candidate("111","000") == "Not Possible"
    assert candidate("111","110") == "Not Possible"
    assert candidate('1746', '02942769') == 2
    assert candidate('26298', '147996') == 2
    assert candidate('051365', '7989622') == "Not Possible"
    assert candidate('195', '70017664') == "Not Possible"
    assert candidate('780', '0133') == "Not Possible"
    assert candidate('25896609', '15612071') == "Not Possible"
    assert candidate('2492', '82752146') == 2
    assert candidate('80898435', '138431439') == "Not Possible"
    assert candidate('798000', '0040406') == 2
    assert candidate('747', '2693') == "Not Possible"
    assert candidate('36391', '897414185') == 2
    assert candidate('543', '8216890') == "Not Possible"
    assert candidate('91404', '747632') == "Not Possible"
    assert candidate('315', '26906') == "Not Possible"
    assert candidate('11087', '553138186') == "Not Possible"
    assert candidate('02868956', '22766586') == "Not Possible"
    assert candidate('0436169', '369926243') == 3
    assert candidate('6975698', '941676798') == "Not Possible"
    assert candidate('5521', '17170') == 2
    assert candidate('4086', '1594708') == 2
    assert candidate('99119', '5171869') == 2
    assert candidate('3370316', '1345068') == 3
    assert candidate('14751071', '652696132') == 4
    assert candidate('02216', '2115682') == 2
    assert candidate('98236', '11187503') == "Not Possible"
    assert candidate('675021104', '047149616') == "Not Possible"
    assert candidate('2957533', '95984268') == "Not Possible"
    assert candidate('08191', '176918') == "Not Possible"
    assert candidate('340', '318804236') == 1
    assert candidate('9988', '17959') == 2
    assert candidate('0925', '6783617') == 2
    assert candidate('881564', '625825') == 3
    assert candidate('2316206', '39009995') == "Not Possible"
    assert candidate('0311', '378921') == 2
    assert candidate('4670', '4174832') == 1
    assert candidate('8510', '28748') == 2
    assert candidate('129215', '858718496') == "Not Possible"
    assert candidate('349868', '051852') == "Not Possible"
    assert candidate('5843', '185473') == "Not Possible"
    assert candidate('2009', '314639') == 2
    assert candidate('173930', '8054874') == 3
    assert candidate('997341', '213312616') == "Not Possible"
    assert candidate('1415018', '883190119') == "Not Possible"
    assert candidate('55687', '92130697') == "Not Possible"
    assert candidate('71538', '7673405') == "Not Possible"
    assert candidate('411796', '1207833') == "Not Possible"
    assert candidate('134916', '449292') == 3
    assert candidate('9172', '05856683') == 2
    assert candidate('54678', '140164') == 2
    assert candidate('025', '79467185') == "Not Possible"
    assert candidate('9474', '346967') == "Not Possible"
    assert candidate('805427', '457548') == 3
    assert candidate('4197', '9411') == 2
    assert candidate('93710', '9851461') == "Not Possible"
    assert candidate('6567', '6701') == "Not Possible"
    assert candidate('972', '4903') == "Not Possible"
    assert candidate('724', '4781') == "Not Possible"
    assert candidate('13457', '39569420') == "Not Possible"
    assert candidate('7495', '85514315') == 2
    assert candidate('014070', '006246232') == "Not Possible"
    assert candidate('122', '062287') == 1
    assert candidate('4564230', '5699040') == 3
    assert candidate('17668', '69079556') == "Not Possible"
    assert candidate('4592254', '170456376') == "Not Possible"
    assert candidate('71567866', '45158029') == 4
    assert candidate('53943', '33503984') == "Not Possible"
    assert candidate('44722', '62339851') == "Not Possible"
    assert candidate('30419351', '39769513') == 3
    assert candidate('49571', '672639239') == "Not Possible"
    assert candidate('3456', '12599') == "Not Possible"
    assert candidate('2511', '5775615') == 2
    assert candidate('268', '431370925') == "Not Possible"
    assert candidate('5925', '12114872') == 2
    assert candidate('7491', '97342') == 2
    assert candidate('647', '49242052') == "Not Possible"
    assert candidate('8857', '650033295') == 2
    assert candidate('9397', '8421') == 2
    assert candidate('717', '2262') == "Not Possible"
    assert candidate('06117', '743289667') == "Not Possible"
    assert candidate('364994', '927497') == "Not Possible"
    assert candidate('626748', '2177701') == "Not Possible"
    assert candidate('308790', '93774526') == "Not Possible"
    assert candidate('061709976', '720050686') == 4
    assert candidate('9653779', '266715743') == 3
    assert candidate('0026', '912603309') == 1
    assert candidate('48665748', '095339193') == 4
    assert candidate('430', '48810924') == 1
    assert candidate('52247', '02556') == 2
    assert candidate('52485649', '02947030') == "Not Possible"
    assert candidate('25287', '154181906') == 2
    assert candidate('74451', '391375507') == "Not Possible"
    assert candidate('259', '352060') == 1
    assert candidate('73976', '71794') == 2
    assert candidate('27363', '1108711') == "Not Possible"
    assert candidate('423', '35252') == "Not Possible"
    assert candidate('4080', '02111210') == 2
    assert candidate('27584', '4334618') == "Not Possible"
    assert candidate('080', '301') == "Not Possible"
    assert candidate('0098336', '01733193') == "Not Possible"

if __name__ == '__main__':
    check(min_Swaps)