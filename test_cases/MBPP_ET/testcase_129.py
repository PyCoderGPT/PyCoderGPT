from case_MBPP_129 import count_integer


def check(candidate):
    assert candidate([1,2,'abc',1.2]) == 2
    assert candidate([1,2,3]) == 3
    assert candidate([1,1.2,4,5.1]) == 2
    assert candidate([4, 4, 'tbbohpcdo', 1.3819276930997435]) == 2
    assert candidate([1, 4, 'vrhssdg', 3.184857428276234]) == 2
    assert candidate([6, 6, 'koqqn', 4.664490846542019]) == 2
    assert candidate([3, 3, 'mgkgdwnp', 4.910749338331247]) == 2
    assert candidate([1, 1, 'rehe', 6.896289190674974]) == 2
    assert candidate([4, 7, 'yvywu', 2.7854057560811474]) == 2
    assert candidate([3, 3, 'bsdvmmw', 5.406689836350308]) == 2
    assert candidate([1, 2, 'ciri', 4.460898131752047]) == 2
    assert candidate([1, 6, 'zgke', 2.057090695795378]) == 2
    assert candidate([6, 6, 'hfy', 4.275763066540621]) == 2
    assert candidate([2, 6, 'ljc', 2.6967758594845153]) == 2
    assert candidate([1, 4, 'bkg', 6.24691070946794]) == 2
    assert candidate([5, 1, 'iqaaspcp', 2.45142217965316]) == 2
    assert candidate([2, 4, 'jttvzefc', 6.229186129356008]) == 2
    assert candidate([4, 7, 'xnawa', 5.215399261634855]) == 2
    assert candidate([3, 3, 'ejvusc', 3.821102763143713]) == 2
    assert candidate([6, 3, 'lzfartq', 4.606454965987902]) == 2
    assert candidate([5, 3, 'tdzaehmir', 1.794751772181998]) == 2
    assert candidate([5, 7, 'gnco', 3.1311480117552524]) == 2
    assert candidate([1, 6, 'sequpbkna', 4.013411988800485]) == 2
    assert candidate([5, 2, 'gmwfdcq', 6.050550619652883]) == 2
    assert candidate([5, 1, 'ucxal', 3.64190277338864]) == 2
    assert candidate([5, 3, 'grzktoce', 2.667710939106369]) == 2
    assert candidate([1, 4, 'qtsyvqzrs', 6.404173960439104]) == 2
    assert candidate([3, 5, 'szpef', 1.420197230040209]) == 2
    assert candidate([1, 3, 'wmxwmate', 2.6538211206524833]) == 2
    assert candidate([2, 1, 'gzngzu', 4.647783645299926]) == 2
    assert candidate([1, 4, 'wtuswvg', 1.3053978342747832]) == 2
    assert candidate([6, 7, 'ecfcvieds', 4.901728806465941]) == 2
    assert candidate([4, 4, 'hubv', 5.475782201127471]) == 2
    assert candidate([5, 5, 'aosew', 6.538951602826536]) == 2
    assert candidate([1, 7, 'qcnkhrz', 4.302273628063601]) == 2
    assert candidate([5, 6, 'muf', 5.3165437084197205]) == 2
    assert candidate([6, 4, 1]) == 3
    assert candidate([3, 2, 8]) == 3
    assert candidate([5, 2, 4]) == 3
    assert candidate([4, 1, 4]) == 3
    assert candidate([6, 4, 3]) == 3
    assert candidate([1, 7, 7]) == 3
    assert candidate([3, 7, 1]) == 3
    assert candidate([6, 4, 1]) == 3
    assert candidate([3, 3, 7]) == 3
    assert candidate([5, 6, 8]) == 3
    assert candidate([6, 4, 4]) == 3
    assert candidate([1, 4, 7]) == 3
    assert candidate([5, 7, 1]) == 3
    assert candidate([2, 7, 5]) == 3
    assert candidate([6, 3, 4]) == 3
    assert candidate([1, 4, 5]) == 3
    assert candidate([2, 1, 3]) == 3
    assert candidate([2, 3, 3]) == 3
    assert candidate([5, 6, 8]) == 3
    assert candidate([6, 3, 1]) == 3
    assert candidate([2, 6, 5]) == 3
    assert candidate([4, 5, 7]) == 3
    assert candidate([2, 1, 2]) == 3
    assert candidate([4, 7, 3]) == 3
    assert candidate([2, 1, 4]) == 3
    assert candidate([2, 6, 3]) == 3
    assert candidate([6, 7, 3]) == 3
    assert candidate([5, 7, 5]) == 3
    assert candidate([6, 7, 4]) == 3
    assert candidate([5, 1, 6]) == 3
    assert candidate([5, 3, 2]) == 3
    assert candidate([1, 2, 2]) == 3
    assert candidate([2, 7, 7]) == 3
    assert candidate([2, 1.8553442014629242, 5, 3.486169308406372]) == 2
    assert candidate([1, 5.614377212514301, 7, 6.538456402952713]) == 2
    assert candidate([4, 5.113315913362309, 8, 7.279665945481777]) == 2
    assert candidate([4, 6.690429691511674, 1, 7.039422524086938]) == 2
    assert candidate([6, 4.714397509521071, 2, 7.777036512504394]) == 2
    assert candidate([3, 5.157724831983163, 6, 2.563076482507656]) == 2
    assert candidate([3, 3.586855223357107, 1, 3.5907167371951947]) == 2
    assert candidate([6, 6.477789096412567, 9, 6.1561000285062555]) == 2
    assert candidate([6, 3.705927880528561, 4, 2.760109597546501]) == 2
    assert candidate([4, 3.9444456594941633, 6, 5.821112753357251]) == 2
    assert candidate([1, 6.831181713963922, 1, 6.365661616360776]) == 2
    assert candidate([5, 1.710624265343542, 1, 7.912850878019607]) == 2
    assert candidate([3, 3.8874420213708567, 3, 9.7410407221393]) == 2
    assert candidate([6, 6.471911109694775, 7, 9.848144278536674]) == 2
    assert candidate([4, 4.372275468817751, 3, 1.1258120753330294]) == 2
    assert candidate([6, 6.949863298098777, 7, 10.113853013330383]) == 2
    assert candidate([5, 5.965370533327305, 4, 2.278702585621618]) == 2
    assert candidate([5, 6.686458998560186, 5, 9.20482954750981]) == 2
    assert candidate([3, 4.607412107693682, 1, 10.47132858829426]) == 2
    assert candidate([6, 2.673905481574053, 6, 10.978853704466399]) == 2
    assert candidate([1, 3.669584796325983, 2, 1.6348220854396383]) == 2
    assert candidate([5, 4.598721981020166, 9, 7.852266072487876]) == 2
    assert candidate([5, 3.179805837242972, 6, 5.301581104524813]) == 2
    assert candidate([5, 3.7110125429310683, 7, 1.9522071054401158]) == 2
    assert candidate([2, 4.234373586182315, 7, 1.089020804806845]) == 2
    assert candidate([5, 3.0010458348485143, 8, 10.572438256857803]) == 2
    assert candidate([6, 6.378360364264284, 3, 4.528541151065596]) == 2
    assert candidate([6, 5.82659734196585, 9, 5.682674490715313]) == 2
    assert candidate([2, 1.8749921845628577, 9, 6.796361279222687]) == 2
    assert candidate([5, 5.976178168897697, 6, 7.140301956086789]) == 2
    assert candidate([2, 4.188874689909322, 7, 10.701124818895813]) == 2
    assert candidate([4, 6.6690263099879274, 2, 3.291301869420245]) == 2
    assert candidate([1, 3.234636990273491, 1, 1.181733849313567]) == 2

if __name__ == '__main__':
    check(count_integer)