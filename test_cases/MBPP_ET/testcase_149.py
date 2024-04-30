from case_MBPP_149 import dict_filter


def check(candidate):
    assert candidate({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert candidate({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180)=={ 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert candidate({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190)=={ 'Pierre Cox': 190}
    assert candidate({'coLrMRlITUMP': 172, 'jTdkMTayIbTEhIFHx': 183, 'jkLJMNynvRc': 170, 'nlrOCbkV': 195}, 174) == {'jTdkMTayIbTEhIFHx': 183, 'nlrOCbkV': 195}
    assert candidate({'KSOWuDWdjqRMM': 172, 'kkPaKIpeJuh': 180, 'FhVBPJtJmYQ': 165, 'lFufPqcNY': 190}, 166) == {'KSOWuDWdjqRMM': 172, 'kkPaKIpeJuh': 180, 'lFufPqcNY': 190}
    assert candidate({'BipbSqgJWkr': 170, 'agnAQSODAdAnEEQQ': 180, 'BkaqlweYZdyC': 169, 'NflUkbJTNqCBOg': 192}, 172) == {'agnAQSODAdAnEEQQ': 180, 'NflUkbJTNqCBOg': 192}
    assert candidate({'LCyCurpoB': 172, 'VJhefRZtzZBMgYuUq': 178, 'VIlDFhjPZf': 167, 'FPpLcufAtc': 189}, 168) == {'LCyCurpoB': 172, 'VJhefRZtzZBMgYuUq': 178, 'FPpLcufAtc': 189}
    assert candidate({'oyPOnj': 175, 'BlrgcLDZvgTpkDfi ': 184, 'YZNxApxIC': 170, 'HIPPtrfZ Xs': 190}, 171) == {'oyPOnj': 175, 'BlrgcLDZvgTpkDfi ': 184, 'HIPPtrfZ Xs': 190}
    assert candidate({' YlIpaOeCpn': 176, 'lLRJWxhqdVgHN': 176, 'XDVsxrxKbEfqXW': 163, 'WcfApgxpIoPEL': 192}, 169) == {' YlIpaOeCpn': 176, 'lLRJWxhqdVgHN': 176, 'WcfApgxpIoPEL': 192}
    assert candidate({'TeHwQJ eWkn': 180, 'fOFKsnxuxe': 181, 'patPhTIUVtQsM': 168, 'uXULZsiHUcWCbGb': 186}, 166) == {'TeHwQJ eWkn': 180, 'fOFKsnxuxe': 181, 'patPhTIUVtQsM': 168, 'uXULZsiHUcWCbGb': 186}
    assert candidate({'pWUGGuQSsYsplpD': 178, 'NvAiIVbtzfAIP': 175, 'cBppD Lb ZjvNTfM': 168, 'yGbWMyz': 193}, 166) == {'pWUGGuQSsYsplpD': 178, 'NvAiIVbtzfAIP': 175, 'cBppD Lb ZjvNTfM': 168, 'yGbWMyz': 193}
    assert candidate({'WDbmGBEyYgHN': 180, 'lKfVVQUbWVtkQvC': 184, 'fapnzlxqbH': 165, 'PteOWfnFHl': 188}, 170) == {'WDbmGBEyYgHN': 180, 'lKfVVQUbWVtkQvC': 184, 'PteOWfnFHl': 188}
    assert candidate({'wwnQJnodMXEYTS': 179, 'DpWEBiWyXyBKFtfAGZ': 185, 'JgeGOphaoQ': 161, 'lnZpLUUluQT': 190}, 171) == {'wwnQJnodMXEYTS': 179, 'DpWEBiWyXyBKFtfAGZ': 185, 'lnZpLUUluQT': 190}
    assert candidate({'JQPRAFMJS z': 174, 'MBRwFJwqZE': 183, 'FaKxlBDFT': 161, 'jC UiIbe': 192}, 170) == {'JQPRAFMJS z': 174, 'MBRwFJwqZE': 183, 'jC UiIbe': 192}
    assert candidate({'pgHqsij LIkcUr': 177, 'BAgzVtxxkR': 185, 'XLsvUfftc': 165, 'hSmcJqVICicZ': 189}, 171) == {'pgHqsij LIkcUr': 177, 'BAgzVtxxkR': 185, 'hSmcJqVICicZ': 189}
    assert candidate({'KnmNszVIqqlAFv': 176, 'YYunjowfZuwkA': 183, 'elRJKbRzszAuzyBBfB': 161, 'UBKSzKlNEYQM': 185}, 171) == {'KnmNszVIqqlAFv': 176, 'YYunjowfZuwkA': 183, 'UBKSzKlNEYQM': 185}
    assert candidate({'pVizGWQoh': 177, 'fSpWdzyf oYOP': 179, 'MnYD vNMBFJhCtQIK': 168, 'lEYQpk': 193}, 173) == {'pVizGWQoh': 177, 'fSpWdzyf oYOP': 179, 'lEYQpk': 193}
    assert candidate({'wDGNfnU': 178, 'UlieNqDdvj': 183, 'XppqYpcJOsT': 168, 'AabhzMwEAgJwg': 192}, 166) == {'wDGNfnU': 178, 'UlieNqDdvj': 183, 'XppqYpcJOsT': 168, 'AabhzMwEAgJwg': 192}
    assert candidate({'hnqTZDaKdzYsmv': 170, 'zbsbqKBpcQGL': 185, 'ko iMwBrqAb ': 161, 'KBzgIfzCxGI': 192}, 172) == {'zbsbqKBpcQGL': 185, 'KBzgIfzCxGI': 192}
    assert candidate({'FbybnIIWUkrfs': 171, 'HVCUfhxkEhmcGkyun': 178, 'eLPyLTMXxc': 161, 'vzFggBsc': 193}, 168) == {'FbybnIIWUkrfs': 171, 'HVCUfhxkEhmcGkyun': 178, 'vzFggBsc': 193}
    assert candidate({'JjBKOUzBjqYDZ': 175, 'obFkDkVXFBcmIJhe': 181, 'KzrPlUChf': 163, 'somzAAowipU': 189}, 175) == {'JjBKOUzBjqYDZ': 175, 'obFkDkVXFBcmIJhe': 181, 'somzAAowipU': 189}
    assert candidate({'xjoKCmNsNv': 180, 'uHgncrOFfQFTarCl': 175, 'rhEgbbjjfyx': 162, 'yZdLvbxSRHace': 194}, 171) == {'xjoKCmNsNv': 180, 'uHgncrOFfQFTarCl': 175, 'yZdLvbxSRHace': 194}
    assert candidate({' PGJIsUGJqmWLQ': 173, 'nFgextBBtpM goXhm': 177, 'FGMlYJhotHLCozT': 164, 'PRPChpDU': 189}, 173) == {' PGJIsUGJqmWLQ': 173, 'nFgextBBtpM goXhm': 177, 'PRPChpDU': 189}
    assert candidate({'cgBvdCnG': 176, 'cakFkaIbImjo': 180, 'sVWqlcXZUdGFESr': 163, 'GgCxBk': 186}, 175) == {'cgBvdCnG': 176, 'cakFkaIbImjo': 180, 'GgCxBk': 186}
    assert candidate({'HdbYbwm': 180, 'NZuHobpGD': 182, 'QbxPdBrUmfAH AMF': 162, 'mkLmti': 195}, 171) == {'HdbYbwm': 180, 'NZuHobpGD': 182, 'mkLmti': 195}
    assert candidate({'pQigxpoExls': 174, 'fsfpozIMixGMFfsI': 183, 'pRRzdjgAPzg': 170, 'DUxOUiKUV': 191}, 167) == {'pQigxpoExls': 174, 'fsfpozIMixGMFfsI': 183, 'pRRzdjgAPzg': 170, 'DUxOUiKUV': 191}
    assert candidate({'Mq gYsvpijI': 175, 'fncxZHgT tVWxuwssy': 176, 'ltvzIioZvjgPxikMwp': 168, 'kHCEytSEeAkULI': 193}, 167) == {'Mq gYsvpijI': 175, 'fncxZHgT tVWxuwssy': 176, 'ltvzIioZvjgPxikMwp': 168, 'kHCEytSEeAkULI': 193}
    assert candidate({'qwwjIF': 175, 'nvFFNiykdwRlEkmXu': 182, 'cALoXvOjmx': 165, 'tGeLhC': 194}, 167) == {'qwwjIF': 175, 'nvFFNiykdwRlEkmXu': 182, 'tGeLhC': 194}
    assert candidate({'ckOEKqWpSAPSkt': 176, 'eVkkbOAPe': 185, 'EaNoADuKgBQBCe': 163, 'QSJMcBcF': 190}, 167) == {'ckOEKqWpSAPSkt': 176, 'eVkkbOAPe': 185, 'QSJMcBcF': 190}
    assert candidate({'AKPwyRw': 174, 'PxbVhpKrLr': 175, 'GypRgybjjEJOQWNsV': 168, 'Hj SQqbO v': 194}, 169) == {'AKPwyRw': 174, 'PxbVhpKrLr': 175, 'Hj SQqbO v': 194}
    assert candidate({'HFgdXwU': 173, 'vpNgeOrRCDfRqNUH': 185, 'sdTVwgPoTh': 162, ' gEhtDNQGKU': 190}, 173) == {'HFgdXwU': 173, 'vpNgeOrRCDfRqNUH': 185, ' gEhtDNQGKU': 190}
    assert candidate({'eJjkQAlU': 170, 'cAOBYLvMn': 177, 'lBgCvxmNnH': 163, 'UpXiAOWTGl MH': 191}, 175) == {'cAOBYLvMn': 177, 'UpXiAOWTGl MH': 191}
    assert candidate({'SVN VifRO': 175, 'HiNVEsCwdk': 185, 'DUwdMpO YzpDoqjg': 167, 'jEmkQNiFkI': 191}, 171) == {'SVN VifRO': 175, 'HiNVEsCwdk': 185, 'jEmkQNiFkI': 191}
    assert candidate({'EuWBFi': 178, 'wzPwhpgSUHknkUvyB': 176, 'yHXsjjqJWm': 162, 'erdKDPqSYX': 195}, 169) == {'EuWBFi': 178, 'wzPwhpgSUHknkUvyB': 176, 'erdKDPqSYX': 195}
    assert candidate({'ZWYsryLycyejI': 179, 'SpzWCpsIOsP': 183, 'KBJwlvLJwzLeBD': 161, 'xhlQg C': 190}, 171) == {'ZWYsryLycyejI': 179, 'SpzWCpsIOsP': 183, 'xhlQg C': 190}
    assert candidate({'SxITUomddkK': 179, 'lisNIhbTYREvBOp': 176, 'rgEHFPHltIuGdUVE': 168, 'VcIpOUkIhOO': 188}, 175) == {'SxITUomddkK': 179, 'lisNIhbTYREvBOp': 176, 'VcIpOUkIhOO': 188}
    assert candidate({'khZYWMwuTDOlA': 179, 'zirHVjMNSjxgD': 185, 'gAMCrMMWeNgzR': 170, 'myhhOh': 190}, 181) == {'zirHVjMNSjxgD': 185, 'myhhOh': 190}
    assert candidate({'EJRMJZrGF': 172, 'zVyfhiovRWMzxSxkA': 181, 'zyzNle psUGngF': 170, 'tr HpQtwVTLRFih': 192}, 182) == {'tr HpQtwVTLRFih': 192}
    assert candidate({'IPBsWgxGwaTy': 173, 'RksWZjkZJyvMe ': 176, 'wxAq XEJIFgLM': 170, 'skOPYlaquNbpD': 195}, 183) == {'skOPYlaquNbpD': 195}
    assert candidate({'uscflXPad': 173, 'EPNBgVLWHSgCV': 176, 'vQsLNufT XPDU': 167, 'wPdfiBBAmZ': 189}, 175) == {'EPNBgVLWHSgCV': 176, 'wPdfiBBAmZ': 189}
    assert candidate({'OYlvFXmAyC': 176, 'OyrXTSOLZnnVA': 182, 'jIvaVQpDJaiwlTaRLm': 163, 'CQJKTvPexVl': 195}, 181) == {'OyrXTSOLZnnVA': 182, 'CQJKTvPexVl': 195}
    assert candidate({'GeFOxqT': 170, 'ENthPi eUJgUYV': 175, 'LyH KwXJwnLF': 167, 'bUcpYF': 189}, 178) == {'bUcpYF': 189}
    assert candidate({'kymY Pn': 170, 'GZkZHJPIHjvwdIW': 176, 'jloKFmzpwzNR': 161, 'cxKXoRB ': 190}, 183) == {'cxKXoRB ': 190}
    assert candidate({'rqwWgvcPkn': 179, 'IaATMNnQcK': 175, 'KecUjLlrK': 165, 'oywXOgjppBX': 191}, 177) == {'rqwWgvcPkn': 179, 'oywXOgjppBX': 191}
    assert candidate({'UDHsxYT': 170, 'X lMeSEodpez': 184, 'araSuLxHw': 163, 'YRcjFaAAymJg': 189}, 183) == {'X lMeSEodpez': 184, 'YRcjFaAAymJg': 189}
    assert candidate({'dXyxDNy': 177, 'pNHxNyDNVoDjReTsU': 179, 'ckBetMruicewBHrvCN': 167, 'rVxPcRV': 190}, 180) == {'rVxPcRV': 190}
    assert candidate({'tTwkZXXNT': 174, 'ojoSeFKqHuw': 179, 'tprlToCMCImh z': 160, 'eeqlASqovLo': 188}, 185) == {'eeqlASqovLo': 188}
    assert candidate({' XWnCWyWqyRYg': 175, 'gCTLREPO yhZsk': 185, 'ioZhwzetu': 170, 'puyaORPlHbOuUAy': 191}, 185) == {'gCTLREPO yhZsk': 185, 'puyaORPlHbOuUAy': 191}
    assert candidate({'gQkyQWoQVIaFZZi': 171, 'BtfKBmbWOybTBYonFV': 185, 'voJoFtCUKIezdfxGtM': 162, 'HWgEFnHUI': 189}, 179) == {'BtfKBmbWOybTBYonFV': 185, 'HWgEFnHUI': 189}
    assert candidate({'PGYhNNMJ': 174, 'sgxMYpiLhKF': 175, 'NYrYrY rqSwBEuH': 168, 'UPCBnTS': 192}, 176) == {'UPCBnTS': 192}
    assert candidate({'CtKvPVfxvMdfGeW': 175, 'KiiOfQwadThGZQgvY': 178, 'lcknClvYXR Plrs': 160, 'MjKKnTG': 186}, 181) == {'MjKKnTG': 186}
    assert candidate({'MXxSaWdn': 175, 'ykEPHViTN': 180, 'ZYpcqYKYxsOyd': 166, ' SubWr': 190}, 183) == {' SubWr': 190}
    assert candidate({'eSpiafCha': 170, 'lfLnpAfoqS': 179, 'wExZVauFucrN': 167, 'uyDZMnpSc': 188}, 179) == {'lfLnpAfoqS': 179, 'uyDZMnpSc': 188}
    assert candidate({'OvXNENjwuAuH': 174, 'oKQmXidWlDlffSJP': 181, 'VkVzRIQZUvgJVstVE ': 168, 'OctEexg': 193}, 179) == {'oKQmXidWlDlffSJP': 181, 'OctEexg': 193}
    assert candidate({'VDHeCdVNEyO': 174, 'rQgLbLWfaIxGctm': 179, 'ShCWVqMEqFNsRHPTgD': 164, 'hjMRSaWeFqWVNK ': 186}, 182) == {'hjMRSaWeFqWVNK ': 186}
    assert candidate({'qnBwsRKV hRe': 171, 'WwEDbwTsTEIKgh': 179, 'crVnpwWOsWBstVf': 161, 'SwolJlBfyrR': 185}, 181) == {'SwolJlBfyrR': 185}
    assert candidate({'LtHokVUBZNcZFnE': 180, 'dIiIxzjumbECeOjQU': 183, 'GYdLzpPCyKeeIPkcqy': 169, 'mQLisdnvf': 195}, 181) == {'dIiIxzjumbECeOjQU': 183, 'mQLisdnvf': 195}
    assert candidate({'LgfHuoWLgFq': 178, 'CGOQQmXljXzpLflFQh': 177, 'DerMqRmISLdSGUjdl': 161, 'AnTtzypMn kKLPg': 187}, 175) == {'LgfHuoWLgFq': 178, 'CGOQQmXljXzpLflFQh': 177, 'AnTtzypMn kKLPg': 187}
    assert candidate({'uRelCzoUNi': 176, 'ZCjuSdHhyliBOJs': 184, 'LfAXJyfMKLTGGokEIK': 165, 'JaWYKMeqZCMw': 192}, 184) == {'ZCjuSdHhyliBOJs': 184, 'JaWYKMeqZCMw': 192}
    assert candidate({'AmAegiEZ': 176, 'TeZJfRtZr': 177, 'hHFc sUVBns': 160, 'iFmxJKOmfULcDA': 186}, 183) == {'iFmxJKOmfULcDA': 186}
    assert candidate({'VgZVvPzZkhVJ': 178, 'xDizCeTIUYqO': 182, 'miwAEIxEFtY': 168, 'CZLvF  iXFl': 190}, 182) == {'xDizCeTIUYqO': 182, 'CZLvF  iXFl': 190}
    assert candidate({'EnIHaFyTh': 171, 'dZaCFLyOVgkiWHGhK': 177, 'xkSSqAIZiLlThL ': 166, 'dBrSlEequN': 189}, 185) == {'dBrSlEequN': 189}
    assert candidate({'h RSvmz': 172, 'xEUoXwXTs Tyecs': 183, 'iNlJwwmXCxyMAE': 165, 'XGDRqkEFDXkvtF': 194}, 178) == {'xEUoXwXTs Tyecs': 183, 'XGDRqkEFDXkvtF': 194}
    assert candidate({'RrKVVN': 174, 'VpTAgzLjOBckSXFJtm': 181, 'BmJtyzRSahRY tDTQT': 169, 'uJMsqq': 185}, 175) == {'VpTAgzLjOBckSXFJtm': 181, 'uJMsqq': 185}
    assert candidate({'WUnPUPPzUjTAZG': 172, 'CdHiQZEQnu': 183, 'UlSoYTIukF': 165, 'nwafUgpbTfI': 192}, 175) == {'CdHiQZEQnu': 183, 'nwafUgpbTfI': 192}
    assert candidate({'GNyXmruTPnsW': 180, 'CSiVW VdzbPfEPWe': 175, 'KTbjxnAvtbVL': 162, 'PPqqqGzKm': 193}, 176) == {'GNyXmruTPnsW': 180, 'PPqqqGzKm': 193}
    assert candidate({'qPaPkCa': 179, 'zjuMFjOhtWprG': 175, 'nAXgMQtBWYGPqfCv': 164, 'ztZUPHPPsB': 189}, 180) == {'ztZUPHPPsB': 189}
    assert candidate({'jJAhTkocLoEHBz': 177, 'rVPUesemlTnONoNJTp': 184, 'qsVpPOWOPktlP': 164, 'CfamkiDKDYuXQV': 191}, 178) == {'rVPUesemlTnONoNJTp': 184, 'CfamkiDKDYuXQV': 191}
    assert candidate({'kVrjC v': 176, 'Xw zjdUlNFXJ': 181, 'zzsu MqbxzVTNhv': 166, 'gODAFMdTqcvJoI': 190}, 179) == {'Xw zjdUlNFXJ': 181, 'gODAFMdTqcvJoI': 190}
    assert candidate({'kFoHtXgveePXeNE': 175, 'jsfIOouQy': 181, 'fFiHiivDKYM': 164, 'croMoidc': 190}, 188) == {'croMoidc': 190}
    assert candidate({'VxNA gDh': 180, 'VHHzhaZzzBo': 177, 'PnvEGpOEKkPbHK': 163, 'lXIPrRhu': 191}, 195) == {}
    assert candidate({'caHCsZkcXZ': 172, 'LoiCxedarzTSee': 181, 'OcOErwAogEIGAfU': 160, 'XPQKzaUw': 187}, 193) == {}
    assert candidate({'MwVZuEtuFapoiJ': 178, 'BUaNUAShauX': 176, 'HJPxMaLpx': 167, 'ZABysqS': 193}, 193) == {'ZABysqS': 193}
    assert candidate({'NaqwjWZsSKt': 177, 'QodiPBhtcKSuZr': 177, 'fMSDOIqXuxGacz': 160, '  LXgpEWEtrGm': 192}, 187) == {'  LXgpEWEtrGm': 192}
    assert candidate({'KpRACIw': 179, 'ysvHcvvzitop ': 181, 'MdhtVmZYAGrLDql': 162, 'mEgzTOT': 188}, 188) == {'mEgzTOT': 188}
    assert candidate({'QaUuTvcdxyE': 179, 'LtDaTQYAQbeytl': 175, 'evSjQFnWqTUqc': 169, 'ZXVKFZzayqYWs': 194}, 194) == {'ZXVKFZzayqYWs': 194}
    assert candidate({'NVoHvngKo': 180, 'eAHYrytwMFkiYsURx': 175, 'tcgynPqgAGXST': 170, 'jQFuodAD': 191}, 188) == {'jQFuodAD': 191}
    assert candidate({'QVWomX': 172, 'ToNsaPmXAxmoOqXO': 181, 'U hcddBguxW': 160, 'L wxSXgCatCXhtS': 191}, 187) == {'L wxSXgCatCXhtS': 191}
    assert candidate({'dtvIEV': 177, 'tJwgYCAjmqIY': 175, 'vGnjSZsnBt ': 169, 'Bg glNOMTSKPAPX': 195}, 193) == {'Bg glNOMTSKPAPX': 195}
    assert candidate({'ecntxgmeYHUt': 178, 'FXYDxVUzLrKrR': 181, 'AjdnMUuOthkONGc': 163, 'SeSvxfo': 187}, 193) == {}
    assert candidate({'DyjhqS': 172, 'UsDuphCWwoLsM': 175, 'AzQxvjPlFSVCfGbr': 161, 'sBOqSxXPX': 189}, 186) == {'sBOqSxXPX': 189}
    assert candidate({'wkQoMxS': 178, 'BgCQJYCZxaNJjtW': 179, 'fySBDi YdV OhF': 165, 'IEzJsptubE': 187}, 190) == {}
    assert candidate({'VsDFjW': 175, 'OpqXzAwLoRuB': 177, 'cFehHkiGxAuCVGOO': 167, 'bPFppb': 193}, 188) == {'bPFppb': 193}
    assert candidate({'srUrkhxVGqaQm': 175, 'hebzsfypOvPiSZIm': 185, 'ksZRe yUataUOzyx Q': 162, 'xStwnjmMu': 185}, 191) == {}
    assert candidate({'JtvnlhuFoI': 172, 'ZsEMNeeEgMbBaOf': 180, 'jHYUnRkgMzvc': 160, 'aNLrHjSzKWXW': 194}, 195) == {}
    assert candidate({'hq YMuQsUQ': 178, 'rCNkGPoZkFi': 182, 'xxBQYlTzoSWgtpHczd': 167, 'QPrk xfe': 195}, 186) == {'QPrk xfe': 195}
    assert candidate({'DWaHUANYx': 174, 'lRKgrUbOtjTEaL': 176, 'kxpOQXwdLtm': 164, 'ksGrTHZ': 191}, 193) == {}
    assert candidate({'ecHfrglIP': 174, 'MJahToXcxx': 175, 'zkexIFvEQz': 169, 'PW Korwmx': 186}, 187) == {}
    assert candidate({'qPYYrhRzSIRShRi': 179, 'EyuqxIVgzxcGlhAZx': 183, 'jAUbdsAyOaxSMxKRa': 166, 'bNLvGQSG': 188}, 194) == {}
    assert candidate({'miakbKCypbYYZZB': 174, 'JMDefCDolJeS': 175, 'dGocNbRSAYoz': 163, 'QKKpeIGvpgl': 192}, 190) == {'QKKpeIGvpgl': 192}
    assert candidate({'ZKKkOZDniXMkaD': 173, 'NAyGfLnjbo': 179, 'CfExgnqdKKLvsIkPU': 161, 'jixwuwkB': 188}, 192) == {}
    assert candidate({'hfALADQHsxlo': 176, 'bUcQQBfmhTkgVv': 176, 'lSZEiVxnfWnpRom': 166, 'vVTuiaAbCaL': 187}, 186) == {'vVTuiaAbCaL': 187}
    assert candidate({'deQyIYfAt': 179, 'yrvZdPxjgAC ': 184, 'VhvDpjzKd': 167, 'XwNTJPg': 192}, 194) == {}
    assert candidate({'YBWypWAIAmbGCfq': 175, 'rwbvXYEbdNpAX': 175, 'ksSyTJmUvzoiZA': 162, 'xslQMkQY dAFbt': 185}, 185) == {'xslQMkQY dAFbt': 185}
    assert candidate({'GvaMvq': 177, 'RTfZJLkDgZdaG': 179, 'xuqKBVwUnyv': 168, 'ExJdllAIoTCbO': 191}, 191) == {'ExJdllAIoTCbO': 191}
    assert candidate({'FgclNmp': 174, 'ExZZIbqPmum': 181, 'ToucRNBfI': 167, 'dOGggAhGrOKma': 189}, 195) == {}
    assert candidate({'CnPyYPYjzCyUiB': 176, 'JtZcIVOMPSZR': 184, 'aPDGZXzYcTasFjru': 161, 'PuzGmtkjJBQl': 188}, 185) == {'PuzGmtkjJBQl': 188}
    assert candidate({'TkqOroVJAPpPjde': 174, 'jZGYZwKJKTNBLPu': 177, 'Q ACTAPZvPjofKn': 169, 'LR dLboC': 194}, 187) == {'LR dLboC': 194}
    assert candidate({'qzZbSSDW': 173, 'YwSEmLtns': 185, 'tnIxkeGurZ': 163, 'VrKjZhPsCj': 188}, 188) == {'VrKjZhPsCj': 188}
    assert candidate({'OVMukdxaLTkB': 171, 'ValTfvHESeDZHkffD': 183, 'kKMprolAR ': 161, 'EAfAGJvIvRMKVyr': 195}, 193) == {'EAfAGJvIvRMKVyr': 195}
    assert candidate({'ZmfrzZPmRQIE': 179, 'ZTiqrGRoVtPGKxobT': 175, 'vPpZheDEkIUdjeZ': 166, 'kLY KHImywb': 188}, 188) == {'kLY KHImywb': 188}
    assert candidate({'zc weAY': 176, 'xDfsoLupYguZFhMSCX': 184, 'udYOukXIdZhSYtior': 167, 'WBmWOv': 192}, 192) == {'WBmWOv': 192}

if __name__ == '__main__':
    check(dict_filter)