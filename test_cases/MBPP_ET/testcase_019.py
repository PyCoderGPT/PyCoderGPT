from case_MBPP_019 import count_Substrings


def check(candidate):
    assert candidate('112112',6) == 6
    assert candidate('111',3) == 6
    assert candidate('1101112',7) == 12
    assert candidate('929900280', 7) == 1
    assert candidate('014974961871', 3) == 1
    assert candidate('06922', 1) == 0
    assert candidate('7154049', 6) == 1
    assert candidate('35146532', 3) == 1
    assert candidate('527399796752', 10) == 0
    assert candidate('8274109655', 7) == 1
    assert candidate('36506459260', 4) == 0
    assert candidate('858251058', 6) == 1
    assert candidate('89347', 2) == 0
    assert candidate('76454273229', 6) == 0
    assert candidate('0789269176', 4) == 0
    assert candidate('3216491786', 10) == 2
    assert candidate('5037366208', 3) == 0
    assert candidate('4242464152', 6) == 0
    assert candidate('2083685796', 4) == 1
    assert candidate('6291677543', 3) == 0
    assert candidate('391375196', 1) == 0
    assert candidate('7569516945', 9) == 1
    assert candidate('70610189018', 5) == 1
    assert candidate('71417376413', 1) == 0
    assert candidate('40113214700', 8) == 4
    assert candidate('6453242727', 1) == 0
    assert candidate('5608611788', 6) == 1
    assert candidate('0574412136', 8) == 2
    assert candidate('17009587426', 10) == 1
    assert candidate('31570', 3) == 1
    assert candidate('324135', 6) == 1
    assert candidate('14314612036', 9) == 5
    assert candidate('0885268203', 5) == 0
    assert candidate('9521519406', 1) == 0
    assert candidate('8217', 1) == 0
    assert candidate('5354500', 7) == 0
    assert candidate('66127348', 2) == 0
    assert candidate('33606', 4) == 0
    assert candidate('34515', 2) == 0
    assert candidate('893', 1) == 0
    assert candidate('67727488', 2) == 0
    assert candidate('050259483', 2) == 0
    assert candidate('52728', 2) == 0
    assert candidate('785603', 6) == 0
    assert candidate('5107731', 7) == 2
    assert candidate('501358567', 2) == 0
    assert candidate('53253', 2) == 0
    assert candidate('97957138', 3) == 0
    assert candidate('0628', 2) == 0
    assert candidate('9250', 4) == 0
    assert candidate('244926025', 7) == 0
    assert candidate('91967', 5) == 1
    assert candidate('554117', 3) == 0
    assert candidate('2152092', 3) == 1
    assert candidate('377188706', 4) == 1
    assert candidate('54711534', 4) == 1
    assert candidate('828', 1) == 0
    assert candidate('462803', 6) == 0
    assert candidate('6363', 3) == 0
    assert candidate('3974689', 2) == 0
    assert candidate('80726', 3) == 0
    assert candidate('999974666', 7) == 0
    assert candidate('97656373', 5) == 0
    assert candidate('808182662', 3) == 0
    assert candidate('1851', 4) == 2
    assert candidate('84873716', 8) == 1
    assert candidate('29467', 5) == 0
    assert candidate('612449164', 2) == 1
    assert candidate('10129403', 7) == 4
    assert candidate('648545668891', 9) == 0
    assert candidate('572212090', 2) == 0
    assert candidate('5549037', 4) == 0
    assert candidate('58392410815', 11) == 2
    assert candidate('806890048', 5) == 0
    assert candidate('882614794', 4) == 0
    assert candidate('5000094728', 2) == 0
    assert candidate('341051973697', 4) == 1
    assert candidate('830173682', 7) == 1
    assert candidate('388057', 6) == 0
    assert candidate('6841', 3) == 0
    assert candidate('6185', 3) == 1
    assert candidate('2853061043', 5) == 0
    assert candidate('567704445308', 5) == 0
    assert candidate('815553', 2) == 1
    assert candidate('04102948573', 7) == 3
    assert candidate('64687196784', 8) == 1
    assert candidate('718581', 5) == 1
    assert candidate('3941862', 3) == 0
    assert candidate('056490282990', 11) == 1
    assert candidate('235656114', 7) == 1
    assert candidate('8030878035', 3) == 0
    assert candidate('900692751', 5) == 0
    assert candidate('687655849', 3) == 0
    assert candidate('469632002202', 6) == 0
    assert candidate('84991298', 5) == 1
    assert candidate('45099641', 3) == 0
    assert candidate('5891870292', 6) == 1
    assert candidate('2313731040', 3) == 1
    assert candidate('52210002', 6) == 3
    assert candidate('911567263', 6) == 3
    assert candidate('884542315265', 11) == 1
    assert candidate('8162661', 6) == 1

if __name__ == '__main__':
    check(count_Substrings)