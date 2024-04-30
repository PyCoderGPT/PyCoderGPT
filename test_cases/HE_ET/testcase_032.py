from case_HE_032 import find_zero


def check(candidate):
    assert abs(candidate([11, 4, -10, 12, 7, -4]) - -0.77267882990418) < 1e-6
    assert abs(candidate([15, -17, -20, -17, -6, 20, 7, -5]) - 0.49331206834176555) < 1e-6
    assert abs(candidate([-7, 14, -8, 22]) - 0.46537516731768847) < 1e-6
    assert abs(candidate([5, 9]) - -0.5555555555620231) < 1e-6
    assert abs(candidate([-10, -4, -13, 15]) - 1.3983234210172668) < 1e-6
    assert abs(candidate([-15, -21, -16, 7, 5, 23, 15, 8, -18, -21]) - -1.3084048776654527) < 1e-6
    assert abs(candidate([-18, 9, 1, -9, -13, 2, -19, 13, 1, 23]) - 1.0548499115975574) < 1e-6
    assert abs(candidate([8, 10, -16, 0]) - -0.4605823048041202) < 1e-6
    assert abs(candidate([10, 6, 11, 14]) - -1.0368183794198558) < 1e-6
    assert abs(candidate([-19, 16, -9, -18, 16, 2]) - 1.2976147570298053) < 1e-6
    assert abs(candidate([14, 14, -6, 10, 19, 3, -11, -16, 16, 2]) - -8.83436661597807) < 1e-6
    assert abs(candidate([-11, -10]) - -1.1000000000349246) < 1e-6
    assert abs(candidate([1, 10, 13, 2]) - -5.627257501648273) < 1e-6
    assert abs(candidate([-22, -8]) - -2.7500000000582077) < 1e-6
    assert abs(candidate([12, 12, 2, -21, -20, 24]) - -0.7701213540858589) < 1e-6
    assert abs(candidate([1, 1, -4, 7, 7, 4, 6, -1]) - -0.3414826926891692) < 1e-6
    assert abs(candidate([14, -5, -15, 7, -12, -7, 5, -12, 7, 13]) - 0.7576340154628269) < 1e-6
    assert abs(candidate([-19, 17, -16, -5, 14, 19]) - 0.898737533192616) < 1e-6
    assert abs(candidate([-14, -18]) - -0.7777777778101154) < 1e-6
    assert abs(candidate([-14, -13, -18, 21, -9, 8, 21, 15, -14, -9]) - -2.057502954849042) < 1e-6
    assert abs(candidate([22, 14, 6, 4, -15, 23]) - -0.787588662118651) < 1e-6
    assert abs(candidate([-16, 14]) - 1.142857142840512) < 1e-6
    assert abs(candidate([-14, -15, -2, 14, 8, 12]) - 0.9725828649825417) < 1e-6
    assert abs(candidate([-9, -6, 11, 4, 20, -16, 11, 21]) - 0.7235527937300503) < 1e-6
    assert abs(candidate([10, 12, 4, -15, 15, -16, -11, 2]) - -1.8998562887427397) < 1e-6
    assert abs(candidate([-22, 0, 21, 21]) - 0.7694531165179797) < 1e-6
    assert abs(candidate([2, -20, 6, -22, 20, -3, -14, 15, -7, 22]) - 0.10206166439456865) < 1e-6
    assert abs(candidate([8, -9]) - 0.8888888888759539) < 1e-6
    assert abs(candidate([-25, -15, 9, -18]) - -0.7682942365645431) < 1e-6
    assert abs(candidate([8, 9]) - -0.8888888889341615) < 1e-6
    assert abs(candidate([19, 17, 21, 15, -6, 2, 5, 15, -18, -12]) - -0.8678967274026945) < 1e-6
    assert abs(candidate([14, -14, -18, -4]) - 0.555046035500709) < 1e-6
    assert abs(candidate([7, 11, 2, 19, 12, -17]) - 1.637195018294733) < 1e-6
    assert abs(candidate([-1, -17, -3, 18, -23, -18]) - -1.7348281079903245) < 1e-6
    assert abs(candidate([6, 4, -8, 3, -11, 17, -4, -9, -7, -3]) - 0.8557536666048691) < 1e-6
    assert abs(candidate([-11, -10, 6, 17, -6, -13, 2, -6]) - -0.9463667231029831) < 1e-6
    assert abs(candidate([-24, 11, -1, -16, 12, -10, 23, 20, -6, 7]) - 0.9190105249872431) < 1e-6
    assert abs(candidate([24, 11]) - -2.1818181818234734) < 1e-6
    assert abs(candidate([-14, 1]) - 13.999999999941792) < 1e-6
    assert abs(candidate([-14, 11, 9, 2, -2, 6]) - 0.721380373230204) < 1e-6
    assert abs(candidate([-3, -9]) - -0.33333333337213844) < 1e-6
    assert abs(candidate([-8, 13, 9, 2, 19, 8, 10, -13, -2, 1]) - -0.8531489259912632) < 1e-6
    assert abs(candidate([5, -6, 12, 10]) - -1.7184622491477057) < 1e-6
    assert abs(candidate([-24, -6]) - -4.0) < 1e-6
    assert abs(candidate([15, -21, -11, 19, -9, -18, 10, 16]) - -1.1195546543458477) < 1e-6
    assert abs(candidate([23, 4, 0, -7, 4, -14, -16, 2]) - 0.9722188145387918) < 1e-6
    assert abs(candidate([-5, -14]) - -0.3571428571594879) < 1e-6
    assert abs(candidate([7, -6, 5, 22, 25, 13, -8, 6, 18, -4]) - 4.770844701270107) < 1e-6
    assert abs(candidate([-13, -5, 20, -11]) - -0.6102688648970798) < 1e-6
    assert abs(candidate([12, 13]) - -0.9230769231216982) < 1e-6
    assert abs(candidate([3, 16]) - -0.18750000005820766) < 1e-6
    assert abs(candidate([17, -15, -12, -10, -11, -6, -8, -13, -6, -15]) - 0.5782326273038052) < 1e-6
    assert abs(candidate([-10, -24, -13, -12, -5, -3]) - -0.49830489250598475) < 1e-6
    assert abs(candidate([7, 4, -9, -1, -4, -19]) - 0.7221282896935008) < 1e-6
    assert abs(candidate([13, -7, 7, -14, 24, 11, 16, -8]) - 2.80472753115464) < 1e-6
    assert abs(candidate([-4, 2, -21, -21, -3, -15]) - -0.9115011811954901) < 1e-6
    assert abs(candidate([-19, -3, 19, 12]) - 0.8581307990825735) < 1e-6
    assert abs(candidate([-8, 22, -13, 4, -19, 5]) - 3.6952950280392542) < 1e-6
    assert abs(candidate([13, -10, 17, 8, 10, -5, -12, -14, 2, -5]) - 1.0264517103787512) < 1e-6
    assert abs(candidate([-2, -16, -13, -15, 22, 11, 2, 0]) - -0.13745924655813724) < 1e-6
    assert abs(candidate([-13, 17, 6, -5, 10, -3]) - 0.6254661156563088) < 1e-6
    assert abs(candidate([9, -10]) - 0.8999999999650754) < 1e-6
    assert abs(candidate([17, 3]) - -5.666666666686069) < 1e-6
    assert abs(candidate([20, -19, -9, 5, 6, -6, 5, 3]) - -2.6316723850322887) < 1e-6
    assert abs(candidate([11, 10, 17, 23]) - -0.8706650706008077) < 1e-6
    assert abs(candidate([21, -14, -2, 1, 17, 22]) - -1.3030383244040422) < 1e-6
    assert abs(candidate([1, 19]) - -0.052631578990258276) < 1e-6
    assert abs(candidate([-6, 1]) - 5.999999999941792) < 1e-6
    assert abs(candidate([20, -15, 7, 4, 10, -13, 14, -2]) - 6.076492612366565) < 1e-6
    assert abs(candidate([-18, 0, 17, -10, -5, 1, 5, -9]) - -0.8188176067196764) < 1e-6
    assert abs(candidate([7, -10, -12, -8, 7, -22, -10, -9]) - 0.41794696007855237) < 1e-6
    assert abs(candidate([-1, 3]) - 0.3333333333139308) < 1e-6
    assert abs(candidate([-21, -15, -9, 2]) - 6.031960799999069) < 1e-6
    assert abs(candidate([13, 5, -14, 10, 8, 6]) - -0.7034340428072028) < 1e-6
    assert abs(candidate([9, -2, 13, -9, 7, -6, -19, 12]) - -1.109157961443998) < 1e-6
    assert abs(candidate([-10, 19]) - 0.5263157894369215) < 1e-6
    assert abs(candidate([16, -4, 5, 17, 13, 10, -18, -11, -9, -4]) - -0.9899867788772099) < 1e-6
    assert abs(candidate([18, 13, 6, 4, 25, 2]) - -12.354712168104015) < 1e-6
    assert abs(candidate([6, -19]) - 0.31578947365051135) < 1e-6
    assert abs(candidate([21, -4]) - 5.249999999941792) < 1e-6
    assert abs(candidate([-18, 23]) - 0.7826086956192739) < 1e-6
    assert abs(candidate([-10, -13, 10, 8]) - -0.6201622396474704) < 1e-6
    assert abs(candidate([6, 8]) - -0.7500000000582077) < 1e-6
    assert abs(candidate([-7, 7, 17, -6]) - -0.7554270991240628) < 1e-6
    assert abs(candidate([12, -4, -9, -10, -5, 9, 5, -14, -7, -10]) - 0.7067770625581034) < 1e-6
    assert abs(candidate([3, 14]) - -0.2142857143189758) < 1e-6
    assert abs(candidate([-11, 16, 10, 14, -7, -5, 16, -6]) - 0.47406378050800413) < 1e-6
    assert abs(candidate([18, 5, -15, -2, -8, 12, 18, -3]) - 6.544080602936447) < 1e-6
    assert abs(candidate([14, 11, 21, 14]) - -1.4373825288494118) < 1e-6
    assert abs(candidate([-13, 3]) - 4.333333333313931) < 1e-6
    assert abs(candidate([8, -2, -14, 8]) - -0.6930004681926221) < 1e-6
    assert abs(candidate([16, -9]) - 1.7777777777519077) < 1e-6
    assert abs(candidate([3, 0, 19, -18, -15, -21, -4, 2, 3, 10]) - 0.6814166828989983) < 1e-6
    assert abs(candidate([12, -1]) - 11.999999999941792) < 1e-6
    assert abs(candidate([13, 10]) - -1.3000000000465661) < 1e-6
    assert abs(candidate([17, 5]) - -3.400000000023283) < 1e-6
    assert abs(candidate([-16, 21, -21, 5]) - 3.199999999953434) < 1e-6
    assert abs(candidate([-4, -19]) - -0.21052631584461778) < 1e-6
    assert abs(candidate([2, -10, -13, -3, 18, 22]) - -0.9493472008616664) < 1e-6
    assert abs(candidate([5, -23, 15, 16, -2, 15, 13, 22]) - -1.0063705976353958) < 1e-6
    assert abs(candidate([20, 4, -12, -11, 18, -3, 10, -12, -13, -7]) - 0.9633776134578511) < 1e-6
    assert abs(candidate([19, -21, 7, -13, 2, 16]) - -1.4949183813296258) < 1e-6
    assert abs(candidate([11, -11]) - 0.9999999999417923) < 1e-6
    assert abs(candidate([0, -15, 4, 13, 16, 18]) - -1.0769825705792755) < 1e-6
    assert abs(candidate([-15, -12, -1, -9]) - -0.8498448199825361) < 1e-6
    assert abs(candidate([-8, -9, 1, -17, 9, 20]) - -0.554555429960601) < 1e-6
    assert abs(candidate([-12, -23]) - -0.5217391304904595) < 1e-6
    assert abs(candidate([-18, 2, 18, 22, -7, 0]) - 0.7371362166595645) < 1e-6
    assert abs(candidate([18, 1, -7, -15, -15, 18]) - -0.9225858352147043) < 1e-6
    assert abs(candidate([9, -6, -4, 5, -17, 6]) - -0.7955967499874532) < 1e-6
    assert abs(candidate([17, -17, -1, -8, 2, 8]) - -1.6226657959632576) < 1e-6
    assert abs(candidate([-15, 19]) - 0.7894736841553822) < 1e-6
    assert abs(candidate([-10, -14, -2, 14]) - 1.3156257915543392) < 1e-6
    assert abs(candidate([-5, 2, -18, -4, -22, -19, -10, -20]) - -1.1249770895810798) < 1e-6
    assert abs(candidate([-15, -25, -13, 7, 4, -4, -15, -23, 20, -3]) - -0.7873706035898067) < 1e-6
    assert abs(candidate([8, -7, -4, 9, -17, -19]) - 0.6204621258075349) < 1e-6
    assert abs(candidate([-10, -8, 1, -17, 21, 4, -10, 9]) - -0.5850219993153587) < 1e-6
    assert abs(candidate([3, 2, -18, -7, -10, 2, -9, 1, 20, 11]) - -0.36532484798226506) < 1e-6
    assert abs(candidate([14, 2, -12, -12, 1, -15]) - 0.7575256815180182) < 1e-6
    assert abs(candidate([-9, 12, -6, 13, 7, -9]) - 0.6480104354559444) < 1e-6
    assert abs(candidate([6, 3, -7, -1, -1, 3, 1, -17, 3, 1]) - 0.840877773356624) < 1e-6
    assert abs(candidate([9, 7, 10, -2]) - 5.745492666959763) < 1e-6
    assert abs(candidate([-5, -11, -9, -17, 9, 10]) - -0.4595043617882766) < 1e-6
    assert abs(candidate([18, 8, 9, 17, -14, -4, 8, 6]) - -0.9046317359316163) < 1e-6
    assert abs(candidate([1, -5]) - 0.19999999995343387) < 1e-6

if __name__ == '__main__':
    check(find_zero)