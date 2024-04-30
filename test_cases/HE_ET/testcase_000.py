from case_HE_000 import has_close_elements


def check(candidate):
    assert candidate([4.88, 7.89, 3.67, 5.68, 4.88], 2.06) == True
    assert candidate([3.2, 2.38, 8.15, 6.82, 7.64, 1.09], 0.3617420469176341) == False
    assert candidate([1.01, 2.06, 6.72, 8.86, 8.3, 1.48], 1.91) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([3.26, 1.07, 7.95, 8.07, 7.15, 4.9], 2.86) == True
    assert candidate([1.81, 6.92, 8.55, 9.5, 3.57], 5.9) == True
    assert candidate([6.9, 2.21, 7.1, 3.79, 4.04], 0.396996215155218) == True
    assert candidate([1.54, 4.43, 7.01, 6.17, 10.01], 0.2314054295285396) == False
    assert candidate([6.07, 2.35, 3.41, 7.98, 2.12, 4.52], 5.15) == True
    assert candidate([3.18, 5.84, 3.87, 7.15, 8.43], 1.44) == True
    assert candidate([2.77, 1.01, 1.32, 9.39, 6.21], 5.39) == True
    assert candidate([5.33, 2.33, 1.36, 1.54, 6.95], 0.07523209090543603) == False
    assert candidate([3.06, 7.17, 7.8, 3.14, 9.9, 3.32], 0.15562526330040638) == True
    assert candidate([2.35, 3.12, 1.26, 4.93, 8.6, 2.24], 0.22075974625982897) == True
    assert candidate([6.9, 3.28, 6.53, 9.09, 9.27], 0.27823425350535214) == True
    assert candidate([6.58, 2.5, 8.69, 9.82, 9.86], 1.77) == True
    assert candidate([5.4, 6.12, 6.47, 8.31, 1.75, 5.74], 2.76) == True
    assert candidate([1.41, 1.47, 5.8, 5.5, 9.64], 0.4422265315774656) == True
    assert candidate([4.47, 3.29, 8.27, 4.83, 3.2], 2.53) == True
    assert candidate([2.92, 6.36, 8.63, 3.92, 8.74, 5.18], 0.8508754629067022) == True
    assert candidate([5.74, 3.9, 5.02, 1.13, 9.57, 5.45], 1.09) == True
    assert candidate([6.37, 7.95, 9.41, 7.57, 2.66], 2.27) == True
    assert candidate([6.8, 7.7, 7.97, 9.22, 1.04], 0.5420385167082946) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False
    assert candidate([4.07, 4.35, 4.03, 8.01, 9.69, 7.45], 0.4062541056462473) == True
    assert candidate([4.72, 1.92, 3.55, 3.94, 1.4, 1.93], 3.6) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([2.74, 2.59, 8.75, 2.64, 3.41, 6.83], 0.47037584760808515) == True
    assert candidate([4.55, 3.22, 2.64, 7.89, 4.11, 7.23], 5.08) == True
    assert candidate([1.65, 3.51, 4.77, 4.7, 9.45, 4.71], 1.74) == True
    assert candidate([2.67, 2.26, 3.14, 1.9, 2.88], 0.05407902838980738) == False
    assert candidate([1.13, 7.18, 6.73, 4.67, 6.32, 5.25], 4.08) == True
    assert candidate([6.03, 6.9, 5.3, 4.65, 7.97], 0.7606715861237912) == True
    assert candidate([5.72, 4.52, 8.45, 1.43, 4.88, 7.28], 0.6213126721754707) == True
    assert candidate([3.22, 7.97, 3.43, 2.69, 3.66, 7.9], 3.98) == True
    assert candidate([1.12, 1.1, 1.8, 1.42, 10.81, 2.61], 1.43) == True
    assert candidate([5.52, 7.52, 2.2, 4.41, 5.02, 5.9], 4.09) == True
    assert candidate([3.37, 3.0, 1.92, 9.63, 2.6], 0.6269462195500632) == True
    assert candidate([1.84, 6.19, 1.07, 6.85, 10.02], 0.06327986170932154) == False
    assert candidate([6.78, 5.17, 2.34, 3.59, 9.96, 7.42], 4.52) == True
    assert candidate([2.71, 6.22, 2.09, 3.25, 1.78], 4.42) == True
    assert candidate([5.69, 4.54, 3.55, 8.95, 9.95, 5.06], 3.37) == True
    assert candidate([2.69, 7.45, 2.68, 3.48, 7.09], 4.18) == True
    assert candidate([4.74, 3.86, 1.63, 2.89, 5.88], 0.28615090391667286) == False
    assert candidate([5.2, 5.9, 4.37, 9.33, 10.95], 6.27) == True
    assert candidate([5.51, 7.57, 2.46, 3.85, 2.75], 0.2787247504152883) == False
    assert candidate([6.14, 5.85, 4.03, 8.5, 4.75], 1.63) == True
    assert candidate([4.57, 2.9, 5.05, 6.42, 5.88, 7.55], 0.916840133124239) == True
    assert candidate([6.06, 3.37, 7.46, 2.39, 2.71], 4.84) == True
    assert candidate([6.08, 7.89, 2.32, 3.29, 6.24], 0.11700796032131644) == False
    assert candidate([2.86, 6.89, 5.19, 6.56, 2.63], 4.64) == True
    assert candidate([2.23, 5.08, 6.75, 5.08, 2.12], 0.10128793009561687) == True
    assert candidate([6.22, 6.62, 6.89, 9.54, 4.65, 3.22], 5.32) == True
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert candidate([2.27, 7.74, 3.08, 2.91, 7.28], 2.18) == True
    assert candidate([1.58, 7.87, 1.73, 5.48, 8.73, 7.95], 4.5) == True
    assert candidate([2.55, 1.39, 5.57, 6.98, 9.11, 5.54], 1.11) == True
    assert candidate([5.91, 1.51, 6.23, 2.37, 10.9], 0.7038961471044487) == True
    assert candidate([5.7, 2.8, 1.31, 9.15, 10.4], 6.45) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.27, 7.68, 8.1, 9.7, 1.83, 2.72], 3.86) == True
    assert candidate([1.45, 7.66, 4.78, 9.93, 7.72, 4.82], 0.6004288435422835) == True
    assert candidate([1.17, 6.26, 6.12, 4.42, 5.85, 2.93], 4.66) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
    assert candidate([4.31, 7.57, 1.44, 1.06, 7.74], 4.89) == True
    assert candidate([3.97, 5.8, 2.61, 3.55, 6.67, 3.38], 0.26637639316574935) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([3.79, 4.72, 8.74, 1.79, 7.28, 7.79], 2.99) == True
    assert candidate([5.07, 5.12, 1.02, 9.07, 3.75], 2.11) == True
    assert candidate([6.66, 1.15, 3.17, 9.74, 6.17], 0.8580780500021119) == True
    assert candidate([1.39, 4.68, 10.85, 1.28, 9.9], 0.7720416915105155) == True
    assert candidate([6.78, 4.67, 3.31, 3.15, 5.1], 0.027645872133869043) == False
    assert candidate([2.88, 2.26, 5.77, 1.77, 3.17, 4.82], 1.29) == True
    assert candidate([3.56, 7.26, 7.92, 3.79, 2.48], 5.03) == True
    assert candidate([6.08, 2.32, 5.58, 8.46, 8.4, 1.07], 0.8176950844959172) == True
    assert candidate([4.64, 3.07, 5.48, 4.14, 1.86], 1.5) == True
    assert candidate([4.56, 3.74, 5.5, 5.04, 6.97], 0.0011630148061070322) == False
    assert candidate([1.17, 1.93, 4.45, 7.98, 8.76], 0.7343118568223004) == False
    assert candidate([6.58, 5.04, 3.18, 7.46, 1.48, 1.12], 4.99) == True
    assert candidate([4.54, 6.22, 9.83, 9.14, 2.33], 3.07) == True
    assert candidate([1.29, 2.74, 4.85, 7.84, 7.55], 0.16553567344199593) == False
    assert candidate([3.84, 5.76, 5.19, 2.7, 10.51, 4.31], 4.14) == True
    assert candidate([2.08, 4.46, 5.6, 8.32, 6.69], 0.5273362445063764) == False
    assert candidate([2.71, 4.38, 4.62, 7.54, 8.62, 2.13], 2.6) == True
    assert candidate([5.37, 7.66, 6.14, 4.75, 1.54, 2.89], 0.410138035984677) == False
    assert candidate([6.08, 6.79, 2.08, 4.21, 3.08], 0.9637210131339815) == True
    assert candidate([6.39, 4.67, 9.22, 6.4, 5.71], 4.81) == True
    assert candidate([4.52, 5.0, 1.27, 3.61, 1.81, 7.06], 2.01) == True
    assert candidate([1.5, 3.29, 4.99, 2.43, 9.05, 5.29], 0.7306459844437514) == True
    assert candidate([4.11, 4.75, 5.02, 1.23, 2.81], 4.72) == True
    assert candidate([1.63, 6.76, 6.72, 3.26, 9.6, 4.07], 3.45) == True
    assert candidate([6.98, 7.24, 6.66, 7.33, 2.07], 0.7288255470454569) == True
    assert candidate([1.93, 1.88, 9.12, 8.43, 7.79], 0.9733063912369614) == True
    assert candidate([4.84, 6.99, 5.41, 9.14, 10.84, 1.19], 1.27) == True
    assert candidate([2.68, 2.36, 6.38, 7.89, 1.98], 2.88) == True
    assert candidate([5.38, 4.86, 7.17, 3.08, 4.81, 5.82], 3.78) == True
    assert candidate([6.99, 3.18, 8.31, 2.38, 8.73, 4.14], 0.21143607107881202) == False
    assert candidate([2.57, 2.86, 1.22, 3.7, 2.5], 3.12) == True
    assert candidate([3.94, 4.37, 7.66, 8.74, 3.11], 0.6678682747553127) == True
    assert candidate([1.95, 2.49, 8.58, 2.07, 9.65], 2.54) == True
    assert candidate([5.54, 7.22, 5.99, 5.53, 10.8], 0.6856823622260582) == True
    assert candidate([6.74, 6.46, 9.13, 1.64, 2.87], 0.2749641428006748) == False
    assert candidate([4.87, 4.55, 1.43, 2.32, 9.0], 4.1) == True
    assert candidate([1.12, 6.51, 4.58, 5.18, 4.54], 2.1) == True
    assert candidate([1.92, 2.86, 2.83, 5.78, 1.86], 5.46) == True

if __name__ == '__main__':
    check(has_close_elements)