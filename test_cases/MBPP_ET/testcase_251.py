from case_MBPP_251 import check_value


def check(candidate):
    assert candidate({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
    assert candidate({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
    assert candidate({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False
    assert candidate({'khDOPINlJxr KO': 13, 'KiPFNnJqpoNtDsB': 12, 'bOLVUV wkCBV kWDg': 17, 'GoxIWWuRqqekXPE': 10}, 5) == False
    assert candidate({'CSfSKRnFR': 8, 'dKbkkXCoPPbNiWGrU': 17, 'gkvDyvtdb MDiy': 14, 'GZmLKjtWK': 15}, 5) == False
    assert candidate({'SJLcuEugtG': 10, 'qfxxsnywAsAfAxeTyR': 12, 'tEIhgZzBwtfb': 13, 'FYAlTFU': 7}, 15) == False
    assert candidate({'oQAMWdMLVvrVYF': 8, 'zgAZVcdkEqQmYMXdq ': 11, 'AOKHA kRBhppeGv': 8, 'UOJU FVPN': 9}, 6) == False
    assert candidate({'JoiGvlZ': 14, 'fSkWgudqm': 9, 'riRYmpoBlrjdK': 17, 'BcfSgKgDueMA': 15}, 15) == False
    assert candidate({'KMtCSE': 16, 'VLADzKlZh AEdmCE': 10, 'bOffiWKQldrTbBJCGO': 12, 'FeVjusMmy tD': 14}, 12) == False
    assert candidate({'CbWmmhl': 14, 'vEPYlrWIrqHcTUXJ': 17, 'JAONDAwmaAu': 11, 'QpRSjnJCx ': 10}, 8) == False
    assert candidate({'hsZsXDQXQYVqn': 17, 'vxbOeYrxboW': 13, 'WMXWwMVLjDqQZAbQ l': 17, 'eyJyelngflIerjY': 17}, 11) == False
    assert candidate({'xvdJaTMbAzjEX': 10, 'eDNCeSreeM': 11, 'FbpiKEAcpDcEEpXf': 15, 'puIRjWFG': 11}, 12) == False
    assert candidate({'oyCSLfuU': 17, 'zADKiedhtHouKFw': 8, 'AfymlbJNqAMomkebC': 15, 'cgLPiBlxn': 13}, 11) == False
    assert candidate({'QNoAenjzuJpEQ': 17, 'OzsXoupWE': 17, 'AGnRBeyQYHrgOHT': 8, 'WDjWUjIcxdZXEx': 14}, 7) == False
    assert candidate({'xxuLTHskXVrkDe': 15, 'qtEtlLzFWY': 16, 'WBUZkgwCFek': 12, 'eZfwOUpEub': 15}, 8) == False
    assert candidate({'uJD DZaMbELTifS': 14, 'VFuYxhXuJXv': 16, 'DSTbwsxgNDQZqTYczn': 7, 'myHoXSkIDDZnG': 12}, 14) == False
    assert candidate({'QTlkccfwozLsg': 12, 'ZDdNUvZpWgzIXM ': 14, 'jTALXQcbz': 10, 'NKGQtQ zD': 11}, 9) == False
    assert candidate({'AlfEWLS yeYWMg': 13, 'TSJBlDVfPXKLuQ': 10, 'UMDRpvuvprEI NaYH': 13, 'VTjmtcJIO': 14}, 9) == False
    assert candidate({'qshnkRH': 7, 'DUUnGIKrWmY': 11, 'tbykKtHtEv': 7, 'tuaVDSlCqnd': 10}, 6) == False
    assert candidate({'afyIKzUCttaIZ': 9, 'dUs HHouc': 14, 'ezWmOcZDCmaiZF': 8, 'XDTXqDDSki': 15}, 8) == False
    assert candidate({'nCavxWP': 7, 'jxhEBnsZysrh': 11, 'RcBSuCOUw': 16, 'ZwaSrhoOjB': 11}, 7) == False
    assert candidate({'gmHsfXfXbQFHfY': 15, 'TnCjstPCfui': 14, 'bepamhRXaLhv': 13, 'kAjNZBy SXWFjd': 14}, 7) == False
    assert candidate({'BUIWqvJTAx': 14, 'pYTmvDnyfTSRHrY': 14, ' UsVcfkIwcWan vwYH': 16, 'nzQQhg': 7}, 11) == False
    assert candidate({'kOKdmNEjDOPhm': 10, 'tt iOmUfnaB': 13, 'ca JzaeNoJAehxQ': 8, ' XBGgGXQXzqBGNr': 9}, 13) == False
    assert candidate({' ThdDHAYie': 8, 'EdzHHSclBscMOs': 7, 'QXXtejKacnQ': 8, 'PKUlpwRvhZTaAT': 14}, 9) == False
    assert candidate({'TJtebtaIG': 7, 'nsBJQKaUIE': 12, 'nRGBCEizB': 15, 'NXuUBkkeGj': 11}, 7) == False
    assert candidate({'yXUcQK': 16, 'BdFgqaZ y': 9, 'lbFPAynowdBHfDhJQZ': 13, 'XGFgFatcGg': 17}, 8) == False
    assert candidate({'BoqEUSv': 17, 'uYKNQsoZhYYgDvLAT': 9, 'NSbhllQLgSEdvYNVPu': 13, 'YOiC BlYRlIn': 15}, 7) == False
    assert candidate({'cOanQFIqpWZtZ': 13, 'UbhkNlBgigFzsIdvt': 8, 'pdvDqTZGhy': 8, 'xwIicDkfLSCmYiq': 12}, 10) == False
    assert candidate({'qNdhPPYtHyo': 8, 'RqrHGbSBsHX': 13, 'NsHxrLuhpPvJQK': 12, 'HnzsCGYAJhrLW': 7}, 12) == False
    assert candidate({'DyoWWZXd': 10, 'dDCFKUghnzXKz': 17, 'NGSXnOErAO': 15, 'hqRupgRRJEsvaFv': 17}, 14) == False
    assert candidate({'hszkcew': 14, 'qAKmNwvWhMXZnI': 14, 'qzuFddUBDrcaY': 7, 'JvxShJm': 11}, 6) == False
    assert candidate({'nxxeMdskdAwsf i': 7, 'edElnPwLQoZ': 9, 'nTxDYvAVkwyVl': 11, 'trkT reuXwspmx': 11}, 12) == False
    assert candidate({'zRXcnsOcYiiJev': 13, 'qSIIQBCw Dmwiou': 8, 'TZinQjDKBAAe': 13, 'glBywPI': 13}, 15) == False
    assert candidate({'SeWkjHPZNGhka': 8, 'CTpZRnxwZvhWzG': 17, 'EgbPflELcgT': 12, 'exCv cp': 11}, 5) == False
    assert candidate({'ZiyGxANj': 13, 'cSttIkFRRvEYBru': 17, 'fLMGIqzpQXLsKg': 14, 'cGYUb ': 15}, 9) == False
    assert candidate({'vblSgzdJGDnhv': 15, 'JHxjyTPoZbOT': 13, 'nMKEvFNG YVyPmjaF': 7, 'GG WrytnPfFeZdb': 14}, 8) == False
    assert candidate({'jWEtFkYnEkJ': 16, 'fErSMFfaXvXaQZQw': 17, 'kYmnu sKxS': 17, 'nzseStfzE': 7}, 11) == False
    assert candidate({'XzPrEp hk el': 14, 'YzNfzpazdgi': 10, 'xmfpEBZaydMFD': 14, ' YqWgpqCb': 16}, 11) == False
    assert candidate({'nBSTTjQMKA': 11, 'oshSNoRKMNQWviU': 15, 'gNvDtIjqV rUJ': 8, 'AwPZyWcNsnKQpH': 8}, 15) == False
    assert candidate({'lRcAtsevd': 17, 'bCSropmiMh PSG': 7, 'MvCDaLqQqloTEnj': 17, 'Zszjbt': 10}, 9) == False
    assert candidate({'FYYfUZIV': 12, 'CEmgGeQRgGJ': 13, 'sSMTBH dsZVfPI': 12, 'J fqdoSExmInEQ': 8}, 17) == False
    assert candidate({'snCdBHtnEhps': 8, 'TaIGWvilQlHmgzBr': 8, 'tnijZqBggm': 16, 'gTvpvMdFt': 7}, 7) == False
    assert candidate({'HNRmZlAccM': 9, 'gHCKmQxZ rMj': 7, 'RmM PdJfchhqNvAJn': 16, 'whGPiSSswFm': 12}, 16) == False
    assert candidate({'VBTBMPqNKnOXC': 7, 'SYoZbvbEh': 16, 'hNflLiIyhhsXArVJl': 16, 'GuLeNikFRapUei': 15}, 13) == False
    assert candidate({'AtcdVhNQ': 9, 'KajYh mcsKoEwIgX ': 16, 'mWWHjynBfNqxXyDRKk': 8, 'muBAzsaOGmJrQc': 15}, 17) == False
    assert candidate({'DXEl AVF': 11, 'QIi LTNQYef': 11, 'xQKcJqygm': 14, 'vdyfBRngvVqWury': 16}, 12) == False
    assert candidate({'WSgvNFvElkRSXSX': 14, 'qLddHpORSMpPSgE': 11, 'WwNeIprZDwGr': 16, ' VkWnkuwnHFux': 16}, 14) == False
    assert candidate({'ySRAeTwHHKKa': 10, 'VFHEZzR gI': 17, 'hPKcuVAcEcMsfUd': 10, 'QZzTZDdDeZaY': 8}, 10) == False
    assert candidate({'FQFYMcJIQ': 13, 'XOJHrqepYmntsZ': 8, 'aCxHFWwolBQgoQQ': 14, 'niXDCdzQHYw': 17}, 11) == False
    assert candidate({'bWXZIbPHXQ': 17, 'xXwcaPwiqaOb': 11, 'xKCOkdtYX jrMh': 12, 'rLTjxMnNF': 9}, 13) == False
    assert candidate({'BdbgwQ U': 10, 'UCqwseNsMlWnHNB': 7, 'CanWxJgrpROjlK': 10, 'tyDGp kiRzPbifc': 7}, 17) == False
    assert candidate({'WskJYbIbIBdYy': 13, 'OsIstRvaSHfjbaejpR': 10, 'LWvJMlzFlBv': 9, 'aRRbNPxbwsaO': 11}, 9) == False
    assert candidate({'Uvesdp': 11, 'hixIqUIhTC': 17, 'epDAF RQJFLwjZcyQ': 14, 'OpQPlh': 7}, 15) == False
    assert candidate({'aGfjYvTjh': 14, 'UizZwRwbgBOmD': 7, 'qJskjtIedGFP': 8, 'UyoIOd': 16}, 13) == False
    assert candidate({'fwtppPdYfGi': 16, 'ImRXMfvmPAnCsN': 15, 'hWRjdvUGOiJq': 14, 'iIjzSyxeeZe': 17}, 9) == False
    assert candidate({'gIUXlJAc': 11, 'TKDLxaOjFufoGvV': 12, 'RYSgRLZaBiC': 17, 'uDwJatayzBUI': 7}, 10) == False
    assert candidate({'vywtCsHyFuwvHx': 8, 'CDFUUCrpNKcBI': 12, 'jiGwMThfOsert': 12, 'tgVFscC FyN': 13}, 16) == False
    assert candidate({'JdgvCzfdEbB': 15, 'YVoVrZnxAPJHNdrz': 17, 'hVdlLyIcTCMc': 11, 'ZxMZtwtzmi': 12}, 16) == False
    assert candidate({'EgybvUXONcbHV': 14, 'WiMse ZyIcUd': 11, 'IykoVyQQAAG': 7, 'ImMoes': 9}, 7) == False
    assert candidate({'AhTsXFJYpudiV': 16, 'MMRLLFbMraOLSbrt': 10, 'aVyqPJIyNx': 11, 'UkKRCxNTFtNGJ': 9}, 7) == False
    assert candidate({' cmcmVEIzuMB': 7, 'iYUMTAYxj': 11, 'ECkwwPLrs': 11, 'NLlmIoj': 12}, 17) == False
    assert candidate({'dyMCUtEC': 16, 'z NcdlujViZF': 13, 'eeGUUvxzhsFo': 9, 'NJZiTbJFRAnv': 16}, 16) == False
    assert candidate({'mWhQNgzEmutRWR': 8, 'BHDrEJje tN': 17, 'tlmqGVCpBJLAlZv F': 14, 'wsNZiTYkEoJHS': 15}, 11) == False
    assert candidate({'AGAcISJ qVChb': 7, 'TUtN QaXAOhfYEN': 12, 'iCJzjQveLRel': 8, 'jobPPw': 11}, 15) == False
    assert candidate({'gkpbuQiHSA': 11, 'KdFIpkyfctyKgTW': 15, 'SiIWgRttVdrAK': 7, 'fIFYeccfurwdiD': 15}, 9) == False
    assert candidate({'VPftkhjsRxIX': 13, ' ygTSYyqxplJ': 16, 'jTAMvhRihWNVDUgNYj': 10, 'EXGEKtMcespFjT': 14}, 8) == False
    assert candidate({'mIuUSQVBP': 8, 'scixPBlWhBZUWtqXDo': 8, 'muMfcPlNihYwYi': 7, 'qFiAYB': 11}, 8) == False
    assert candidate({'J wMtIKvYVTfR D': 16, 'OUNWNnQzId rp': 11, 'GCmGXhQmAPEKQX': 14, 'ZHnnOtVKGLkxqiw': 12}, 12) == False
    assert candidate({'xPALKLFLj': 10, 'IlXPxxJsNlHuiFF': 14, 'cALaZbGBYgqu': 7, 'cNgtL yoYAP': 7}, 4) == False
    assert candidate({'OduBpzqj': 16, 'PEPCUqmMP a': 9, 'KQyIjaYMOx': 12, 'xgtCnvLYa': 9}, 4) == False
    assert candidate({'lULrzvOcdeAome': 11, 'uOiGyHOUl': 14, 'MIjoMnvmUUhiTO': 10, 'zlQQnoEpsOLjPGK': 10}, 5) == False
    assert candidate({'xuTNJRDgQSHp': 10, 'CvjucmehAHK': 9, 'ViKsoEfyjrrwrG': 8, 'vUcqKNXbSzSt': 12}, 4) == False
    assert candidate({'uUcJvgFefLwjt': 10, 'meYLiAJEzNVmDiZcO': 9, 'PHyAFiLxjbvRVfEoYw': 7, 'dVQDXYXieYi': 8}, 5) == False
    assert candidate({'fGjyYAMLyk': 14, 'pvqOUWJpOnWxOoj': 7, 'KbWHVKncSrBCLLHA': 15, 'KTupdSgLSlmO': 7}, 9) == False
    assert candidate({'lvRrQiiJ': 12, 'zWYzBR nzNkTQoZ': 14, 'RKdllkpMbQOFZFyYfq': 11, 'WHWotYddKWpfPfq': 17}, 2) == False
    assert candidate({'ObNprljHtQWMhR': 8, 'YzaydgKwgAl': 10, 'B hPGhhryeP': 10, 'HSQjNTBuodB': 16}, 6) == False
    assert candidate({'dxopnKB': 16, 'OeBlVyELWvWtynyG': 14, 'pgRw nrcxQhu RpXY': 9, 'QmgjqevZfBOQ': 7}, 1) == False
    assert candidate({'ElgG azxFb MdFr': 15, 'vcWbtZSBFQgwE': 9, 'rCBvbPGeo': 12, 'tJIgFhigaeaKG': 15}, 6) == False
    assert candidate({'UMpooxzKaK': 12, 'EEqhHThxPOKJLm': 15, 'YHXdnqQVMHLEEcuS': 9, 'fwxIrGhg': 8}, 3) == False
    assert candidate({'WZuHiUH': 16, 'SutjIhcwaq': 12, 'TFrPoWizIoo X': 14, 'ReydtwC ttJxD': 16}, 8) == False
    assert candidate({'qvxJSkHKTh': 12, 'dlPvEp Ny': 11, 'NSdxnJtQHmWHhM t': 9, 'ePBNAvH': 16}, 6) == False
    assert candidate({'NUimTdWlDv': 8, 'RpYfsrnobXSPI': 17, 'wXj LBiFQxOjy': 11, ' jRSUVTe': 14}, 2) == False
    assert candidate({'CeSfffwobDxHXZu': 11, 'TasDFlHyqm  VlVfu': 12, 'JkMAiXhfjXaiuJHMCj': 14, 'pKis EGCELHxqE': 14}, 1) == False
    assert candidate({'VGEhsm': 11, 'YnXcPMfuwgqBrFM': 7, 'ZFWnBGCNYiE': 15, 'XkZYd hRCDuak': 13}, 8) == False
    assert candidate({'OTBZkl': 7, 'rFZiyidQxmUkFcNbP': 15, 'KzkqWDJOevO': 13, 'hTOSaLlQUFHd tm': 13}, 1) == False
    assert candidate({'pnFcfHuN': 10, 'sIAFskf XtKM': 15, 'RedfnmbLmaeinnmPBW': 16, 'VKqeuKLNP': 13}, 6) == False
    assert candidate({'zLtKsbO': 12, 'weknEuAVFwQtnJZ': 14, 'hDCKpvgRslOb': 10, 'vXMzaxQSGApTE': 12}, 9) == False
    assert candidate({'OUdzENn': 10, 'iMleTADsOjjpoj': 13, 'mqXtOlJTYa': 12, 'zlua XtzLgKqUK': 7}, 7) == False
    assert candidate({'fyTaHItCK': 15, 'eNkmFmuxVBNcYrrv': 14, 'kMVnEsulQPWO': 14, 'QlHmlx OdArpwe': 9}, 6) == False
    assert candidate({'QDxLXlNfwaCUL': 14, 'VLXBMcFTqURpI': 12, 'FsPyiFBawWkbm': 11, 'OruNrbHOjp': 8}, 9) == False
    assert candidate({'RPoRusLYKvsMWZ': 7, 'UlAPYpKGfbpJhS': 11, 'zlF THSPqlFjOlpbm': 8, 'MiViKWWtEtZL': 7}, 4) == False
    assert candidate({'dpkNroFUKGuup': 8, 'yfMdXmEuhmzlfQjjQD': 8, 'WZEKzTTBVy cd': 15, 'VGBqyqWGcAvHv': 7}, 10) == False
    assert candidate({'ygKB sgzX': 15, 'WHpBcfzogBdrxDhBHH': 16, 'jqtpMUNPIFubuYPELr': 10, 'myuNfkthiRxJS': 15}, 6) == False
    assert candidate({'tZdUGlO': 10, 'jrUo OpYygTTkR': 13, 'aQaKVsgUJdXJjeeAF': 17, 'zIiswaMz': 16}, 6) == False
    assert candidate({'mZAmIoZOPxTTEs': 13, 'kXCjFpwJB': 10, 'BzpYjhWkGsXAoc': 14, 'atnWCjQHJ tHQTS': 17}, 5) == False
    assert candidate({'THWuTWAtnzCWTw': 9, 'NdtxzDscP': 12, 'rrUfhmz WSusE': 8, 'pKxgEOguBzh': 9}, 4) == False
    assert candidate({'kLtmIRq': 17, 'uvRB JGtfhoS': 11, 'HosyTxTVK': 17, 'syYggsFlWcXF': 8}, 4) == False
    assert candidate({'IZfaaxcf': 11, 'WHl S EwmxkhVbc': 12, 'agIuWyNNTGeGlN': 12, 'WRbxzXY': 8}, 2) == False
    assert candidate({'nBhGWwRLepobafw': 8, 'KcrnHAAIvWfupi': 9, 'NiUiFZ yPjmDVhaQJ': 17, 'QoZPUQfLfJap': 16}, 10) == False
    assert candidate({'BGiCtwSnuWlz': 15, 'ywWCGiJOfFNYECm': 17, 'VnGMiIILSmJaP': 15, 'jskekS': 15}, 9) == False
    assert candidate({'nxVOJn PjrFZkxw': 15, 'cJhPETnpIGjgJ': 15, 'jPkewyESCF': 11, 'yWfgzMQVnTIkyt': 14}, 4) == False

if __name__ == '__main__':
    check(check_value)