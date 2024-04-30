from case_MBPP_393 import occurance_substring


def check(candidate):
    assert candidate('python programming, python language','python')==('python', 0, 6)
    assert candidate('python programming,programming language','programming')==('programming', 7, 18)
    assert candidate('python programming,programming language','language')==('language', 31, 39)
    assert candidate('zs cjk so,jszwwvijkypyuxvqoibbfyjekk', 'guoqbda') == None
    assert candidate('abcwsyhrww eviixrwkc,utymlqeuucy', 'qrsihyvvr') == None
    assert candidate('nws ufu,u mvxi rehxwmsdrp,xovfwwt', 'haetdzgueco') == None
    assert candidate('cgfzhnikirpxivrc fmxdpgh wpoix', 'pszbb') == None
    assert candidate('wnskwusnovoawd,slhe,xkoejkalpesxpjh', 'bspic') == None
    assert candidate('vf tcbezfnb nvptnzvsoyfocoqgqcf', 'mkelx') == None
    assert candidate('ws utwotflqpndggmtsicakioiuroen,fikjpp', 'jksaafymfps') == None
    assert candidate('aetqpcoyu,,bjqiwiwtpwtpfdknepabljqy', 'kfblfrqa') == None
    assert candidate('tkplwmntmnljravhwsaurwsgbjrzxzcwypny', 'tebylzrvyjg') == None
    assert candidate('wrchxhuaryscqfxqmrddulzuambqwthy', 'zvbbgky') == None
    assert candidate('gadrzs,afnthanlbjwzhraxsnwcmgmvwntxphsj', 'jeoxcstl') == None
    assert candidate('enpt jhvg, agnegzpwfra ,b,olwwem', 'zrigcagxvky') == None
    assert candidate('vcrps yfqkidnuelrzkcsge ctaspju', 'rqfjorqph') == None
    assert candidate('dj buttyk pfyuzhhwdbirhhsfqldcldixnyja', 'zrm') == None
    assert candidate('r,rzctryhfei upkwqrkqszuyrp,wpebn', 'cufkrji') == None
    assert candidate('tdotlrojhthtnyytfggjjzvlkcviab ajwcik', 'vartdlukd') == None
    assert candidate('mkei tpgrejhpujsmveypvqssfxho cwrzxteik', 'cabfpvu') == None
    assert candidate('jubkwviyzvunqfmrzpops,l gxsqltik', 'mgahu') == None
    assert candidate('xnfqrbqrfrhueedgaeiiyyaa sbcajcb', 'pwwyxvyg') == None
    assert candidate(',oviqdnzyiaqrhrqfawdiej,npgrkelaeatzc', 'nnklquh') == None
    assert candidate('mdbutfs,whc rupy claujnnksewegh', 'itxwljm') == None
    assert candidate('ctgdrwoflfwrnzrvvfkk,ibpjvxbgrddy', 'vtwm') == None
    assert candidate('dznbhoqbv wklvoxazked vvfpxehpxqyvywz', 'jciuokaoarxc') == None
    assert candidate('ttwxxboqsrh vlqurpbsahusviwbskdr', 'epfewvbyr') == None
    assert candidate('h v,i, sulvzgxom,cbgucefyrunqy', 'aiscmwe') == None
    assert candidate('j,stmxrvjqopxldxv,aktaslrsmxgrzluc', 'mzvlkudpkhg') == None
    assert candidate('yb ywmlimehvmqomreqouvrflcxjdu', 'xfsxqsubrk') == None
    assert candidate(' ragddcpgwmqltvt tlf,wtwbgqtlfbplgmyzg', 'gjqurncsqqj') == None
    assert candidate('of,rdhaasnghbvyifqqouiuljzpog fqzcourns', 'hdq') == None
    assert candidate('sbeofvprbmcywlhcwknihlcbhuosobzg,ngdfin', 'clhefrfnn') == None
    assert candidate('cumd wvzomszvevivjqbvqbgljbu,tdvi', 'aosrejyoayd') == None
    assert candidate('xletgfjuxdgjxwccnshmagjwmexuhfhrfskiboh', 'jalpiwfhhpll') == None
    assert candidate('zulzqhgqbuoonutnsnxjberzjssocl', 'npsfeqaego') == None
    assert candidate('ng,,pdlxn,zmjqbudvkw lxmvqebjg,chxfova', 'zmovioxzof') == None
    assert candidate('grsolrqogwwbdpwugwzkjtmrcvzga,ib byi', 'lwpfthuvatdmc') == None
    assert candidate('ajdgzviowiiafx,j,tzhvcidymivontilqgqgmse', 'xyencnxhnh') == None
    assert candidate('j,,isqkakazvwrgdsijgvv,fhfmxwwwgj cpvfh', 'lwladlpf') == None
    assert candidate('clfimjoavnibbvc vgtpptn lhxzdystilyvoxbkio', 'tklqfr') == None
    assert candidate(',otkzgkgwqttjh kripodclaynmjpyie cwwvasyj,ry', 'wmzsrrcgujvk') == None
    assert candidate('irzrjwesq jcdkxpielmpptpd,csxufsaiqcs', 'epkczx') == None
    assert candidate('fp mwaskvfbho,,wf zmuvigphauwpqsvjwijtcchx', 'vhhbket') == None
    assert candidate('qnbadmmj,ypudrkklhjxoddd  ioklxrniszo ', 'vnnbvcde') == None
    assert candidate('enik lkuit,f jyyrichuhvzrxqikg gtcayl,ithol', 'blermqwixwrdne') == None
    assert candidate('mxgdjpbmgv,fpguvrbynnmwivvjenqy cstnsk', 'gphmciwpqcwi') == None
    assert candidate('swuxfszicjpglowiagwsjpozydjupazqprzyvaeyzttql', 'bukoedrjfwuwajj') == None
    assert candidate(' pyibwheq wkysuscd lzlpwlfbsdtsxuugkdjwtch', 'caqclwkhqhtrud') == None
    assert candidate('icprtsrqbbpjh,ncn,zgrrpkgjnwpzds mkobstgkhgwt', 'ytvudfeerjkc') == None
    assert candidate('hwyouaagnrdgfodqrn,rifzxreovljwurvcbkm', 'zxknjluqet') == None
    assert candidate('ogwudarvc lakpnotdjopynpmbljdbtrgprgxl', 'byumbbg') == None
    assert candidate('rbfbwdgjqbp,jorguhsphydvklfubssuxxwygfhirs', 'qgzvnmwfu') == None
    assert candidate('bprmvphhxg,yiqafymyihtsjfqctvda,owovuczguk', 'agxndjykktkyex') == None
    assert candidate('nholextprmlicjpdtalgzygxjatqdtzo wdd,v', 'dqgbivhxsycgte') == None
    assert candidate('nf,pjnplb,ailsjhggqlshawjbhwbvqskagdnkvfl', 'vmnfpybgxfq') == None
    assert candidate('fufauuhzlzrdfgm,skbeqsgpcchfkmt, ejut wpw', 'ehngrg') == None
    assert candidate('hwtr oavnhdglnqndcvnqfjgfecpbmjpa gvfdeh', 'qlpeud') == None
    assert candidate('uk,xagyelyqpoafbl knbkumrvf,avve iarhipqzcv ', 'elrjnnblxzqw') == None
    assert candidate('xycfa muabgzhjde ky,hqqyhhqjhnb,p,h,btqttt', 'azzthbdiktlhtd') == None
    assert candidate('sejipwcfe psyt jyosnpzllplazrqgun,nnvfq', 'noqcsyjweikp') == None
    assert candidate('jjrlovgehbzjggbjiaxtcnswfccg,ehpzohmpofaaoa', 'yyjujnp') == None
    assert candidate('znwtqtfhwtwoubakpufleihbh x,rnvuujnsik', 'qnnoynsd') == None
    assert candidate('cwyxpzkpmuljbkewzlmbgezxjpgvsfaqjghagm', 'qodvah') == None
    assert candidate('mehwv zsosvttkafngexnabtexitgwptlgnyctrcb', 'ljgzvmwbeksriu') == None
    assert candidate('j,kpinxywltauzavitfhqaqmnim,ldrsodpaem', 'fbevzdtpprvgctd') == None
    assert candidate('rxufku zvlelixhea,ofhcfaqhbb,vxliacwelgp,eo', 'qqanolnvjhcyrn') == None
    assert candidate('hazlridtxd,tjuhwcfzqnkqzbur ywqhiklkav,tzuj', 'nwibcidcex') == None
    assert candidate('pphgqagyvgzthaznequmg iz,uqcmaezaqpc', 'didiydkbgb') == None
    assert candidate('kx jncap,g,usrwgukzldqsknd bwxkdpy,rjuscgldjk', 'cmjek') == None
    assert candidate('vtsmb vmxpzdupjbflsbxuvzqwnijfabwalmrpq,', 'fgz') == None
    assert candidate('gvl,asobtztmvlpqclzidwvsuyn,uqrslxcjjaai', 'ujqontpsvky') == None
    assert candidate('qavkosutgnclm,sgco,aovaszcwe,mds vdaqpgmoupg', 'fduqfc') == None
    assert candidate('evzrnahdrowqakqebdkzdpkscpsbqwzk,sukeq', 'bkjfkxmkztr') == None
    assert candidate('otexfmt,jmpvgxlejtl  qa  tltimypojwb,te phj', 'fimpdm') == None
    assert candidate('orbwnyqt rhguilmmqn,aqhaw,jcqvjdqnwszbz g', 'nxfh') == None
    assert candidate('hj,vdbdvvka,fgjkvjrxstekvlxemamlx,tzhiqj', 'xuayipqn') == None
    assert candidate('hrhdlqawmsgxflsrdcocoamnpshbbynjpuwlwwwrcooe', 'uvivqsanao') == None
    assert candidate('sgtjznhtyyasr,jmoyzouz,gtgpzoofoen am', 'ezb') == None
    assert candidate('xnlx,ambxyybhgngtivmmnxivuhjgjnybolxovlqck o', 'qxxohkdqhk') == None
    assert candidate('mooqyldldwndqsweqigpeukhofnubdlctlph h', 'bte') == None
    assert candidate('pknnpfixl blejebjueccvouwfrarwintyhm', 'rbifexnwu') == None
    assert candidate('adpeivitejhyminvotb,critgghibzbhmk skad', 'oprvfffqtsu') == None
    assert candidate('bd,qdq sr ozipdvjjxwhoh,kntuoqhvuhff', 'lpfavuduagpp') == None
    assert candidate(' tqffrmhxybptxxjggvtrxfxiaz,ywr,vnzi', 'ltide') == None
    assert candidate('vrekl,tkjaoeauiavwmhngocmsvtzsl,yula', 'zdxooczbua') == None
    assert candidate('dygitbjzcvcgpmt,ua xkmwhtsjcnw ,gx ubflllx', 'mjou') == None
    assert candidate('rjbhebuhkddefwzozy,zwolnowxu ponoes,v eqb', 'tmrtohqree') == None
    assert candidate(',wkzuqx h kiyvgwvyusuxs izzzrowxkqblrltq', 'iqe') == None
    assert candidate('znkszempejwkgpoohihofplhbxvarhbqdwrj,ibtji', 'gbswggc') == None
    assert candidate('eunawolverbcvvrkonhbvqidnrgnclbsxc ylsfbi', 'grkhfkf') == None
    assert candidate('r,gxfeciehhkupg nmcgqcfv,ukoykv apob', 'nbwdoamiz') == None
    assert candidate('ysewbxcixnlhpsuuec nqtujt njggilcjgsvet', 'trdrr') == None
    assert candidate('nhdznd ydfdsac, uhkxanuomtwvkhqudrriy', 'iysjmusk') == None
    assert candidate('okhfmurnmjfal btzxybogwirznn alujuttur ld', 'fzcijohb') == None
    assert candidate('zvl,vvubrpggxtbekpw ,vibdxnxrmcs,dbus', 'nhjetqw') == None
    assert candidate('pitas,ml,njbyrmtjmq kwdtgulypvshiwilbgw', 'qntdjk') == None
    assert candidate(',karjnkxxlhwptdhnecuufc vnpkavua oarlvuvwqqh', 'vgpdyyqnrn') == None
    assert candidate(' svckzfpunaaratxtnoxaonxbdoxzcdsrakrp', 'kjaffhm') == None
    assert candidate('nb,epqozhdpfzmrpyhtawsbbhrda qcycuq,u n', 'aamiwozs') == None
    assert candidate('mlfnrguwwfdqovqncpbnygmjr,izmemmdbrhh', 'vnyfdz') == None
    assert candidate('zvwehasiv  fy umoqzkptzrgk,j,mnyagfzbrjwrds', 'fszwkww') == None

if __name__ == '__main__':
    check(occurance_substring)