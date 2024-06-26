from case_HE_161 import solve


def check(candidate):
    assert candidate("#ryv@$l*") == '#RYV@$L*'
    assert candidate("BjdhsNs") == 'bJDHSnS'
    assert candidate("$883%3/") == '/3%388$'
    assert candidate("QnNQfv") == 'qNnqFV'
    assert candidate("o3LWaIl4") == 'O3lwAiL4'
    assert candidate("zt*#m&v") == 'ZT*#M&V'
    assert candidate("wDgT") == 'WdGt'
    assert candidate("ab") == "AB"
    assert candidate("=E!NyLi") == '=e!nYlI'
    assert candidate("jZVuQ") == 'JzvUq'
    assert candidate("UKg@xpM~G") == 'ukG@XPm~g'
    assert candidate("%cCcq#") == '%CcCQ#'
    assert candidate("++A^/?xV") == '++a^/?Xv'
    assert candidate("7_%") == '%_7'
    assert candidate("qon") == 'QON'
    assert candidate("giiqdy") == 'GIIQDY'
    assert candidate("~@8%") == '%8@~'
    assert candidate("^@B") == '^@b'
    assert candidate("?UGciW") == '?ugCIw'
    assert candidate("17000556") == '65500071'
    assert candidate("nfl*&=+$@") == 'NFL*&=+$@'
    assert candidate("wSdcA") == 'WsDCa'
    assert candidate("luG9*?%") == 'LUg9*?%'
    assert candidate("5$0!@") == '@!0$5'
    assert candidate("sxFaMa") == 'SXfAmA'
    assert candidate("?ao") == '?AO'
    assert candidate("k&!_") == 'K&!_'
    assert candidate("-|MSfK") == '-|msFk'
    assert candidate("5%@") == '@%5'
    assert candidate("=epet*orq") == '=EPET*ORQ'
    assert candidate("^dHUM-y") == '^Dhum-Y'
    assert candidate("npKwSAD") == 'NPkWsad'
    assert candidate("55=9/9") == '9/9=55'
    assert candidate("#ccc") == "#CCC"

    # Don't remove this line:
    assert candidate("*^JOyeSI") == '*^joYEsi'
    assert candidate("yzzdc") == 'YZZDC'
    assert candidate("i!X&/T") == 'I!x&/t'
    assert candidate("mlB-*F") == 'MLb-*f'
    assert candidate("856") == '658'
    assert candidate("ifafP-OoTK%") == 'IFAFp-oOtk%'
    assert candidate("Xug") == 'xUG'
    assert candidate("~2~@0") == '0@~2~'
    assert candidate("UMm:m") == 'umM:M'
    assert candidate("6812832") == '2382186'
    assert candidate("QDF:CXB") == 'qdf:cxb'
    assert candidate("5-=@&*") == '*&@=-5'
    assert candidate("761~^_%~4") == '4~%_^~167'
    assert candidate("#$a^D") == "#$A^d"
    assert candidate("4hzTAP_e") == '4HZtap_E'
    assert candidate("2058786") == '6878502'
    assert candidate("yErHfPuhE") == 'YeRhFpUHe'
    assert candidate("*u~") == '*U~'
    assert candidate("g*chm") == 'G*CHM'
    assert candidate("enxhq") == 'ENXHQ'
    assert candidate("ctpx") == 'CTPX'
    assert candidate("j$&Wd") == 'J$&wD'
    assert candidate("ji$rpiwCJ") == 'JI$RPIWcj'
    assert candidate("cjG~zXx") == 'CJg~ZxX'
    assert candidate("dgksb") == 'DGKSB'
    assert candidate("827_~+=6:") == ':6=+~_728'
    assert candidate("vr_d$kBQ") == 'VR_D$Kbq'
    assert candidate("389627754") == '457726983'
    assert candidate("+:#") == '#:+'
    assert candidate("prytYOIw") == 'PRYTyoiW'
    assert candidate("+1/05*!?+") == '+?!*50/1+'
    assert candidate("$u%lZTsz") == '$U%LztSZ'
    assert candidate("qyAKc") == 'QYakC'
    assert candidate("/@-") == '-@/'
    assert candidate("iiyw") == 'IIYW'
    assert candidate("#a@C") == "#A@c"
    assert candidate("49623838") == '83832694'
    assert candidate("u:kx!*") == 'U:KX!*'
    assert candidate("gsl") == 'GSL'
    assert candidate("jlycko") == 'JLYCKO'
    assert candidate("MUSKIE") == 'muskie'
    assert candidate(":TDr") == ':tdR'
    assert candidate("bkd") == 'BKD'
    assert candidate("DNOZ2XKDMJZSwC$") == 'dnoz2xkdmjzsWc$'
    assert candidate("#6@2") == "2@6#"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("n$tkw") == 'N$TKW'
    assert candidate("48954") == '45984'
    assert candidate("LlWj5FD") == 'lLwJ5fd'
    assert candidate("AsDf") == "aSdF"
    assert candidate("@!93/5**@") == '@**5/39!@'
    assert candidate("VmVDPkI") == 'vMvdpKi'
    assert candidate("mOn") == 'MoN'
    assert candidate("059646105") == '501646950'
    assert candidate("huo^") == 'HUO^'
    assert candidate("ghgnw") == 'GHGNW'
    assert candidate("gne") == 'GNE'
    assert candidate("~~%==41") == '14==%~~'
    assert candidate("%_uoz/#?L") == '%_UOZ/#?l'
    assert candidate("w@l+zd") == 'W@L+ZD'
    assert candidate("1234") == "4321"
    assert candidate("EsvNrg") == 'eSVnRG'
    assert candidate("pstVx") == 'PSTvX'
    assert candidate("kLA#y:NC") == 'Kla#Y:nc'
    assert candidate("ePOjFeuu") == 'EpoJfEUU'
    assert candidate("GPJae+?*a") == 'gpjAE+?*A'
    assert candidate("Uc$$xCSQ0cN~") == 'uC$$Xcsq0Cn~'
    assert candidate("gtvtsr") == 'GTVTSR'
    assert candidate("#AsdfW^45") == "#aSDFw^45"
    assert candidate("6971168") == '8611796'
    assert candidate("??rwE") == '??RWe'
    assert candidate("HMYxK") == 'hmyXk'
    assert candidate("gcflna") == 'GCFLNA'
    assert candidate("~+/#") == '#/+~'
    assert candidate("glgh") == 'GLGH'
    assert candidate("?gn~") == '?GN~'
    assert candidate("73713138") == '83131737'
    assert candidate("54138") == '83145'
    assert candidate("oGzZO!NOb@Lty") == 'OgZzo!noB@lTY'
    assert candidate("Q&LKD*BmV") == 'q&lkd*bMv'
    assert candidate("13431299") == '99213431'
    assert candidate("~/uc/@p^h") == '~/UC/@P^H'
    assert candidate("4kqV&&/6+Lc") == '4KQv&&/6+lC'
    assert candidate("fqY") == 'FQy'
    assert candidate("|n*e~bx-") == '|N*E~BX-'
    assert candidate("Pj+3w:31N!s6") == 'pJ+3W:31n!S6'
    assert candidate("++skzZ") == '++SKZz'
    assert candidate("%kmlC*s") == '%KMLc*S'
    assert candidate("232948") == '849232'
    assert candidate("613") == '316'
    assert candidate("!tmFhu") == '!TMfHU'
    assert candidate("+fDs:f") == '+FdS:F'
    assert candidate("XAdrNtUNr") == 'xaDRnTunR'
    assert candidate("cqiau") == 'CQIAU'
    assert candidate("340988") == '889043'

if __name__ == '__main__':
    check(solve)