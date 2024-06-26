from case_HE_113 import odd_count


def check(candidate):
    assert candidate(['0', '26919749']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['0798', '02366778', '20600']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert candidate(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."], "Test 1"
    assert candidate(['2525', '7247507', '07075']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['1943108221']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['8', '3971876672']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 6n the str6ng 6 of the 6nput.']
    assert candidate(['73353', '54032', '317562940']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['8', '456497261']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['248', '658', '777117904']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 7n the str7ng 7 of the 7nput.']
    assert candidate(['724031', '500259', '632']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['400456162', '291963', '23063163']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['3',"11111111"]) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."], "Test 2"
    assert candidate(['50661', '2136', '7729']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['3', '404557094']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['5', '0983127757']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 7n the str7ng 7 of the 7nput.']
    assert candidate(['0', '6651323616']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['75339226', '89728', '752055742']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['573', '519980647', '759475370']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.', 'the number of odd elements 7n the str7ng 7 of the 7nput.']
    assert candidate(['9647664', '427', '581']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['421']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['310237', '229884566', '82206']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert candidate(['886']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert candidate(['3', '2079']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['73797055']) == ['the number of odd elements 7n the str7ng 7 of the 7nput.']
    assert candidate(['36324', '50083356', '16704']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['300']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['271', '137', '314']) == [
        'the number of odd elements 2n the str2ng 2 of the 2nput.',
        'the number of odd elements 3n the str3ng 3 of the 3nput.',
        'the number of odd elements 2n the str2ng 2 of the 2nput.'
    ]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(['65850877', '5059528', '111']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['03375159688']) == ['the number of odd elements 7n the str7ng 7 of the 7nput.']
    assert candidate(['3443737']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['2', '917743201']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 6n the str6ng 6 of the 6nput.']
    assert candidate(['13157']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['314740867408']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['1', '566226']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['2', '68879496242']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['6', '37723320876']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 6n the str6ng 6 of the 6nput.']
    assert candidate(['754']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['893409273951']) == ['the number of odd elements 8n the str8ng 8 of the 8nput.']
    assert candidate(['501']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['394305101']) == ['the number of odd elements 6n the str6ng 6 of the 6nput.']
    assert candidate(['9', '2207']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['697']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['3', '4068493']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['977']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['421566467', '78923', '756468']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['4114770', '5021206', '8472945']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['7', '455345165711']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 9n the str9ng 9 of the 9nput.']
    assert candidate(['116275', '410295', '674523640']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['4', '849265376320']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['9050']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['5', '452264527']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['7', '1217590']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['9', '69416']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['5', '249110']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['1', '6765']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['4', '02063584']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['2608551086']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['301', '7916', '92720']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['5329', '486851', '6803118']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['7648', '39345523', '204']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 6n the str6ng 6 of the 6nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert candidate(['3', '101']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['3533']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['920226', '378', '1743889']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['2', '404772941177']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 7n the str7ng 7 of the 7nput.']
    assert candidate(['608274248', '922654', '4686']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert candidate(['1', '1843466']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['36156577']) == ['the number of odd elements 6n the str6ng 6 of the 6nput.']
    assert candidate(['9629']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['8012', '66299650', '95948']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['59823']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['0078903', '475', '97035']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['448772', '47338942', '37304199']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 6n the str6ng 6 of the 6nput.']
    assert candidate(['7', '109253467']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['4', '03816222']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['5', '2190']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['4', '410']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['9780045']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['0', '548002663448']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['294357648', '698794', '50980504']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['26813216']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['5', '34821']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['08370', '3785480', '612615']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['0', '5363']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['4328', '1471748', '554168367']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['01040680']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['81093250487']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['5975']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['975', '966', '894025174']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['316029247', '09616', '742']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['8', '60100446']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['7797902']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['940689635']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['254']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['27170524', '192667282', '598062836']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['492385212', '791196', '343']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['6', '42691345286']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['30775', '07146', '33444458']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['7680520']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['8106', '2220133', '417']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['13810', '4323', '944499099']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['9', '365704730']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['6558', '0257', '018265']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['8202916']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['6883']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['1', '5624029838']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['940181585465']) == ['the number of odd elements 6n the str6ng 6 of the 6nput.']
    assert candidate(['9', '9308']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['49578887', '97943', '298305']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['1651431', '7841', '085549']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['976647', '53062508', '160663']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['717401786684']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['0327066']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['8', '0254']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['5', '545503']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['67391805539']) == ['the number of odd elements 8n the str8ng 8 of the 8nput.']
    assert candidate(['484933']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['986691', '866', '322581704']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.']
    assert candidate(['3334257', '9040227', '748']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['9', '97332826881']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['73831241']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['0', '5170349']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert candidate(['603110684']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['1', '54886']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert candidate(['216894']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['83858']) == ['the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['3', '4457']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['731670006', '9898924', '2976']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert candidate(['8468', '71770', '36431']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert candidate(['57972820']) == ['the number of odd elements 4n the str4ng 4 of the 4nput.']

if __name__ == '__main__':
    check(odd_count)