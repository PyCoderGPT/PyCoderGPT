from case_MBPP_048 import index_minimum


def check(candidate):
    assert candidate([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert candidate([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert candidate([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'
    assert candidate([('ImQYp', 144), ('gtSkVCBhbnDq', 195), ('JuMxTywobp', 104)]) == "JuMxTywobp"
    assert candidate([('xsLoodC', 142), ('fhIVXhyjm', 201), ('TYvZcDjvemf', 102)]) == "TYvZcDjvemf"
    assert candidate([('zTyMSVCX', 148), ('LmUABXG', 205), ('ClmfxxvYmdlX', 100)]) == "ClmfxxvYmdlX"
    assert candidate([('XcQnLSXLd', 145), ('vHYVnOBs', 197), ('VlZvUah', 97)]) == "VlZvUah"
    assert candidate([('QeQoPF', 146), ('EqVAfeHOohn', 198), ('kCWb', 97)]) == "kCWb"
    assert candidate([('guQxkylB', 144), ('YtMSumUCaZdT', 204), ('EyyHQzcsAeKp', 102)]) == "EyyHQzcsAeKp"
    assert candidate([('BvsiBz', 139), ('wkzbutSJyN', 201), ('qzB', 98)]) == "qzB"
    assert candidate([('cmAcQRQ', 139), ('HIcHeM', 202), ('QKnNY', 103)]) == "QKnNY"
    assert candidate([('FJWAEg', 138), ('gfKP', 201), ('ehukCbQZ', 99)]) == "ehukCbQZ"
    assert candidate([('Mlsx', 142), ('bRjO', 203), ('LRIwampPNAPw', 99)]) == "LRIwampPNAPw"
    assert candidate([('hAtFgf', 145), ('yoOBmdrcb', 198), ('mno', 100)]) == "mno"
    assert candidate([('rTfKvM', 142), ('oFsDxe', 199), ('SnxBnWOIlLFM', 103)]) == "SnxBnWOIlLFM"
    assert candidate([('FIuLgQfg', 147), ('hrRpU', 197), ('YEEvyysxU', 98)]) == "YEEvyysxU"
    assert candidate([('Enpcvuh', 143), ('QazCLpOcC', 203), ('HUxDk', 98)]) == "HUxDk"
    assert candidate([('RnWB', 140), ('UmaZAtjIe', 196), ('OwgH', 100)]) == "OwgH"
    assert candidate([('AtG', 146), ('OADSWNKQTwB', 203), ('LuxaODdV', 96)]) == "LuxaODdV"
    assert candidate([('QhL', 142), ('rgKrXCqHkYSl', 195), ('QmD', 105)]) == "QmD"
    assert candidate([('ALcLmMTAH', 139), ('YIEPPe', 199), ('WRdGBDyH', 96)]) == "WRdGBDyH"
    assert candidate([('LmlrTwkbZ', 147), ('wTgxvKldmI', 195), ('qHeAP', 103)]) == "qHeAP"
    assert candidate([('FDzHkDMz', 148), ('osDa', 201), ('bfjDSaQl', 96)]) == "bfjDSaQl"
    assert candidate([('BCg', 142), ('FIAc', 199), ('AFaq', 105)]) == "AFaq"
    assert candidate([('SagZV', 143), ('KsuIio', 196), ('ZUm', 101)]) == "ZUm"
    assert candidate([('dJxDgsd', 146), ('yeetvNqMsW', 195), ('jEnZhwbXZ', 95)]) == "jEnZhwbXZ"
    assert candidate([('YEisT', 144), ('kYYsBNrMjUk', 205), ('MNAN', 102)]) == "MNAN"
    assert candidate([('loQ', 141), ('Uuy', 198), ('YbXbr', 97)]) == "YbXbr"
    assert candidate([('mFZWmx', 141), ('ySYB', 203), ('pzS', 96)]) == "pzS"
    assert candidate([('pfQAE', 147), ('NSnZcxwfMo', 199), ('ZeExXhHAT', 97)]) == "ZeExXhHAT"
    assert candidate([('DwVjMDSi', 143), ('JaDXuUULNhy', 205), ('acfvZ', 105)]) == "acfvZ"
    assert candidate([('JkjaG', 142), ('GJjEo', 201), ('QDNYBtaDQDz', 95)]) == "QDNYBtaDQDz"
    assert candidate([('olijRoR', 147), ('MArRC', 199), ('qpY', 98)]) == "qpY"
    assert candidate([('wprfQA', 147), ('ORTw', 197), ('XpkDJ', 101)]) == "XpkDJ"
    assert candidate([('chWGGHhBs', 139), ('qSppHSGoysEX', 198), ('ckMBfT', 96)]) == "ckMBfT"
    assert candidate([('DlIm', 142), ('sxpkQaRk', 205), ('WYOExqlT', 99)]) == "WYOExqlT"
    assert candidate([('ZhEfzIRqr', 186), ('MDiQcM', 125), ('kZrwI', 174)]) == "MDiQcM"
    assert candidate([('IzNOAoWc', 188), ('nVIuEj', 130), ('JzBeY', 180)]) == "nVIuEj"
    assert candidate([('YbIiDzQA', 181), ('Xyd', 123), ('cGx', 179)]) == "Xyd"
    assert candidate([('RFaYapCna', 185), ('AoGwf', 127), ('LMFhb', 180)]) == "AoGwf"
    assert candidate([('JZzC', 187), ('DuuBMkdmc', 128), ('zDT', 172)]) == "DuuBMkdmc"
    assert candidate([('zAwXVGrs', 182), ('budQQxqQiZzt', 122), ('EKJXbMnP', 173)]) == "budQQxqQiZzt"
    assert candidate([('utzhUMf', 183), ('YeahuAuPY', 124), ('oEDQBkT', 172)]) == "YeahuAuPY"
    assert candidate([('dWvBWKn', 188), ('PcBASnJXMN', 129), ('oEHp', 176)]) == "PcBASnJXMN"
    assert candidate([('zmdGKbr', 183), ('KZc', 127), ('wDJ', 175)]) == "KZc"
    assert candidate([('jbKOD', 188), ('EplA', 130), ('Art', 180)]) == "EplA"
    assert candidate([('eFgQxOS', 182), ('JxsPGVIcPL', 125), ('XhuJkr', 170)]) == "JxsPGVIcPL"
    assert candidate([('acR', 188), ('uVZgKoXhmzNl', 120), ('BRuVT', 177)]) == "uVZgKoXhmzNl"
    assert candidate([('nhrLELGcB', 190), ('iXprN', 125), ('eBYHdn', 180)]) == "iXprN"
    assert candidate([('gYDwtDISd', 182), ('OEtzDdtssIXD', 128), ('ImhcjTAuT', 178)]) == "OEtzDdtssIXD"
    assert candidate([('RwKUj', 190), ('nfGH', 122), ('HZf', 170)]) == "nfGH"
    assert candidate([('aroVCrIG', 188), ('WZFmaxyQ', 127), ('CUKxQu', 176)]) == "WZFmaxyQ"
    assert candidate([('ukyQ', 182), ('ovaxg', 120), ('VpB', 174)]) == "ovaxg"
    assert candidate([('pfaMews', 186), ('hacfRemIvV', 123), ('zibYJVLMw', 176)]) == "hacfRemIvV"
    assert candidate([('pAHYDwrxf', 181), ('RTCboL', 126), ('AANj', 172)]) == "RTCboL"
    assert candidate([('wlH', 181), ('zPhrUFg', 122), ('vDjZzP', 176)]) == "zPhrUFg"
    assert candidate([('wkFeCOghQ', 187), ('EHAahIRHRb', 123), ('chj', 180)]) == "EHAahIRHRb"
    assert candidate([('SCkqL', 181), ('VLvarMPkk', 126), ('QKNDaWHoc', 174)]) == "VLvarMPkk"
    assert candidate([('zQXw', 183), ('rFtblfcUP', 121), ('XMQkfLyw', 176)]) == "rFtblfcUP"
    assert candidate([('BcW', 187), ('ieUWLQCFpweS', 128), ('qKi', 177)]) == "ieUWLQCFpweS"
    assert candidate([('hUuaSandf', 188), ('BJWRXBIqBqf', 130), ('xwuU', 171)]) == "BJWRXBIqBqf"
    assert candidate([('EOQJc', 186), ('gxMcVtJ', 125), ('XUPqO', 172)]) == "gxMcVtJ"
    assert candidate([('xVbGph', 190), ('SwsLuCQrYNrl', 130), ('JeNXNcX', 174)]) == "SwsLuCQrYNrl"
    assert candidate([('sTguni', 181), ('NRZflcrOKN', 120), ('EOdbB', 170)]) == "NRZflcrOKN"
    assert candidate([('ckBQW', 187), ('XhSewDGLsyWT', 121), ('hnDmEDh', 180)]) == "XhSewDGLsyWT"
    assert candidate([('VgLxeVV', 180), ('XVKYeIihMK', 124), ('RlGjNrTUg', 175)]) == "XVKYeIihMK"
    assert candidate([('musi', 187), ('jNZNyZj', 130), ('rSAenl', 172)]) == "jNZNyZj"
    assert candidate([('xLBoglGjF', 182), ('PMpuW', 125), ('NsOQtZzVD', 175)]) == "PMpuW"
    assert candidate([('YMupYG', 187), ('PbMwBqexedGE', 120), ('JzD', 179)]) == "PbMwBqexedGE"
    assert candidate([('PGKovAq', 346), ('ZEk', 140), ('FNksTQm', 98)]) == "FNksTQm"
    assert candidate([('fBERblr', 347), ('BBatVyYUj', 149), ('SDq', 98)]) == "SDq"
    assert candidate([('VqufP', 349), ('kHMnZeQgjs', 140), ('HrbVnJSnr', 93)]) == "HrbVnJSnr"
    assert candidate([('JgvgyLU', 349), ('AHQ', 150), ('MnHrzov', 101)]) == "MnHrzov"
    assert candidate([('JpxVem', 340), ('LhtDaNqt', 149), ('SHzbEECXQp', 98)]) == "SHzbEECXQp"
    assert candidate([('KLnVtGJW', 346), ('vAyQsBsXUhm', 150), ('qqwteAaBiNdl', 100)]) == "qqwteAaBiNdl"
    assert candidate([('ZNkYFJ', 349), ('gSreKnKo', 143), ('NUQ', 96)]) == "NUQ"
    assert candidate([('IljMxg', 344), ('GvATB', 143), ('LqDFxdmGA', 97)]) == "LqDFxdmGA"
    assert candidate([('dqo', 341), ('njTBQC', 150), ('rJHp', 101)]) == "rJHp"
    assert candidate([('UUbRCqQg', 348), ('wprsBxSH', 149), ('ZWwqhNN', 92)]) == "ZWwqhNN"
    assert candidate([('cmKB', 340), ('OmZArKhmAzih', 150), ('bxe', 97)]) == "bxe"
    assert candidate([('cWB', 349), ('nxtswHHFtOd', 144), ('JaPzog', 91)]) == "JaPzog"
    assert candidate([('QvyB', 343), ('vhYJmRNvst', 147), ('VfcYZsk', 96)]) == "VfcYZsk"
    assert candidate([('HPfzsPJ', 348), ('pvdQnTK', 149), ('dpDgC', 91)]) == "dpDgC"
    assert candidate([('ETrg', 341), ('UeCDJU', 147), ('hwREvCNVOt', 91)]) == "hwREvCNVOt"
    assert candidate([('dWEQqkC', 343), ('WQLldNoxpF', 146), ('iVkmp', 92)]) == "iVkmp"
    assert candidate([('kCTvG', 344), ('NoKofmobRgww', 142), ('OkxQkOL', 100)]) == "OkxQkOL"
    assert candidate([('lnMe', 341), ('xIK', 141), ('zUJsYvyNXZe', 98)]) == "zUJsYvyNXZe"
    assert candidate([('xvJp', 346), ('kWEO', 150), ('bkDL', 94)]) == "bkDL"
    assert candidate([('BiPGfknZ', 349), ('mcwwep', 145), ('jdch', 91)]) == "jdch"
    assert candidate([('DCl', 340), ('QigG', 143), ('klrWATc', 91)]) == "klrWATc"
    assert candidate([('zDHo', 344), ('DRSyPm', 150), ('uHisjEn', 98)]) == "uHisjEn"
    assert candidate([('ltN', 341), ('JKYLFBp', 140), ('AjuJuwP', 99)]) == "AjuJuwP"
    assert candidate([('dbi', 341), ('MtbOeTqhEqG', 142), ('yzIPNSSYO', 101)]) == "yzIPNSSYO"
    assert candidate([('uDsI', 345), ('cCZXJtQw', 141), ('GUiaNE', 94)]) == "GUiaNE"
    assert candidate([('uYuH', 342), ('nvvDOXVOuSm', 143), ('jNfxmpFFdZVd', 100)]) == "jNfxmpFFdZVd"
    assert candidate([('ehYk', 342), ('GQqrr', 145), ('RqY', 100)]) == "RqY"
    assert candidate([('tiuusn', 346), ('bDNds', 147), ('vOlxKThje', 92)]) == "vOlxKThje"
    assert candidate([('ADmDb', 344), ('jOKvMFr', 149), ('ruqlXO', 96)]) == "ruqlXO"
    assert candidate([('YKuXpt', 346), ('rTTj', 146), ('nmDprVNP', 98)]) == "nmDprVNP"
    assert candidate([('eJSjJ', 343), ('dKDyWoOg', 141), ('OPjtFeav', 91)]) == "OPjtFeav"
    assert candidate([('TKmnDAqe', 343), ('gwAGnMhLNk', 140), ('rxJ', 91)]) == "rxJ"
    assert candidate([('mWNDy', 349), ('FuMmCcfJry', 143), ('eQHcTWaYKQiO', 98)]) == "eQHcTWaYKQiO"

if __name__ == '__main__':
    check(index_minimum)