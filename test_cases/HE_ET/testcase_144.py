from case_HE_144 import simplify


def check(candidate):
    assert candidate('250/9', '307/3') == False
    assert candidate("1/5", "1/5") == False, 'test13'
    assert candidate('307/2', '244/4') == False
    assert candidate('948/4', '43/4') == False
    assert candidate('398/6', '443/4') == False
    assert candidate('598/2', '681/10') == False
    assert candidate('190/9', '368/2') == False
    assert candidate('822/2', '228/2') == True
    assert candidate('325/1', '782/4') == False
    assert candidate('544/8', '302/3') == False
    assert candidate('213/4', '974/8') == False
    assert candidate('522/9', '306/9') == True
    assert candidate('489/4', '71/6') == False
    assert candidate("7/10", "10/2") == False, 'test4'
    assert candidate('248/7', '197/5') == False
    assert candidate('258/6', '455/4') == False
    assert candidate('645/10', '426/10') == False
    assert candidate('263/7', '695/7') == False
    assert candidate('434/9', '995/3') == False
    assert candidate('204/9', '139/4') == False
    assert candidate('702/2', '739/7') == False
    assert candidate('71/2', '243/4') == False
    assert candidate('645/5', '557/10') == False
    assert candidate('387/3', '474/9') == True
    assert candidate("5/1", "3/1") == True, 'test3'
    assert candidate('173/8', '723/9') == False
    assert candidate('1000/2', '693/9') == True
    assert candidate('870/4', '140/9') == False
    assert candidate("1/5", "5/1") == True, 'test12'
    assert candidate('865/9', '529/2') == False
    assert candidate('926/3', '493/3') == False
    assert candidate('310/9', '742/8') == False
    assert candidate('737/9', '21/6') == False
    assert candidate('828/1', '844/1') == True
    assert candidate('483/5', '39/2') == False
    assert candidate('673/2', '76/6') == False
    assert candidate('539/3', '30/3') == False
    assert candidate('50/8', '572/5') == True
    assert candidate('439/8', '584/7') == False
    assert candidate('488/9', '680/2') == False
    assert candidate('740/5', '932/7') == False
    assert candidate("5/2", "3/5") == False, 'test9'
    assert candidate('974/5', '871/5') == False
    assert candidate('561/6', '333/5') == False
    assert candidate("2/4", "4/2") == True, 'test11'
    assert candidate('93/9', '337/10') == False
    assert candidate('803/6', '38/7') == False
    assert candidate('882/1', '804/6') == True
    assert candidate('632/7', '874/3') == False
    assert candidate('141/8', '896/6') == True
    assert candidate('87/8', '635/9') == False
    assert candidate('649/10', '575/9') == False
    assert candidate('154/10', '911/4') == False
    assert candidate('792/8', '310/7') == False
    assert candidate('706/10', '573/4') == False
    assert candidate('665/6', '877/7') == False
    assert candidate('483/3', '753/2') == False
    assert candidate('534/9', '319/3') == False
    assert candidate('133/6', '760/2') == False
    assert candidate('740/2', '295/8') == False
    assert candidate('749/10', '943/1') == False
    assert candidate('456/3', '948/7') == False
    assert candidate('359/7', '668/10') == False
    assert candidate('375/10', '255/6') == False
    assert candidate('52/9', '669/3') == False
    assert candidate('120/2', '508/8') == True
    assert candidate('148/3', '587/8') == False
    assert candidate('672/4', '313/4') == True
    assert candidate('72/7', '863/9') == False
    assert candidate('502/5', '889/6') == False
    assert candidate('353/10', '302/7') == False
    assert candidate('726/1', '616/10') == False
    assert candidate('994/10', '447/9') == False
    assert candidate('791/9', '52/1') == False
    assert candidate('527/9', '12/10') == False
    assert candidate('943/5', '868/4') == False
    assert candidate('277/9', '136/4') == False
    assert candidate('359/3', '457/8') == False
    assert candidate('384/3', '969/2') == True
    assert candidate('784/6', '756/7') == True
    assert candidate("2/4", "8/4") == True, 'test10'


    # Check some edge cases that are easy to work out by hand.
    assert candidate('346/8', '69/10') == False
    assert candidate('539/8', '738/8') == False
    assert candidate('648/8', '107/3') == True
    assert candidate('597/2', '79/3') == False
    assert candidate('821/1', '778/4') == False
    assert candidate('788/3', '905/7') == False
    assert candidate('688/1', '227/6') == False
    assert candidate('676/8', '147/9') == False
    assert candidate('486/8', '960/9') == True
    assert candidate('407/3', '387/1') == True
    assert candidate('691/8', '819/8') == False
    assert candidate("1/6", "2/1") == False, 'test2'
    assert candidate('562/9', '39/10') == False
    assert candidate("2/3", "5/2") == False, 'test8'
    assert candidate('654/10', '819/2') == False
    assert candidate('827/9', '360/5') == True
    assert candidate('997/5', '546/9') == False
    assert candidate('782/6', '824/5') == False
    assert candidate('118/7', '979/2') == False
    assert candidate('869/7', '731/5') == False
    assert candidate("11/6", "6/1") == True, 'test7'
    assert candidate('188/3', '736/3') == False
    assert candidate("1/5", "5/1") == True, 'test1'
    assert candidate('665/4', '308/2') == False
    assert candidate('295/9', '167/4') == False
    assert candidate('909/4', '154/4') == False
    assert candidate('717/9', '683/10') == False
    assert candidate('436/5', '911/9') == False
    assert candidate('68/2', '491/5') == False
    assert candidate('770/10', '214/3') == False
    assert candidate('4/10', '651/7') == False
    assert candidate('606/4', '98/6') == False
    assert candidate('112/3', '388/10') == False
    assert candidate('21/8', '930/10') == False
    assert candidate('588/9', '345/7') == True
    assert candidate('925/5', '513/8') == False
    assert candidate("7/2", "4/2") == True, 'test6'
    assert candidate('24/2', '61/2') == True
    assert candidate('239/7', '30/6') == False
    assert candidate('927/3', '488/5') == False
    assert candidate('190/9', '850/5') == False
    assert candidate("2/10", "50/10") == True, 'test5'
    assert candidate('234/7', '89/3') == False
    assert candidate('532/9', '353/4') == False
    assert candidate('987/4', '273/4') == False
    assert candidate('281/8', '869/6') == False
    assert candidate('933/1', '852/8') == False
    assert candidate('472/8', '768/4') == True
    assert candidate('942/8', '116/10') == False

if __name__ == '__main__':
    check(simplify)