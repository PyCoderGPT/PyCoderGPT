from case_MBPP_203 import extract_nth_element


def check(candidate):
    assert candidate([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
    assert candidate([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==[99, 96, 94, 98]
    assert candidate([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],1)==[98, 97, 91, 94]
    assert candidate([('n EgKjVhbKDk', 100, 97), ('nqPIIwz', 95, 98), ('GMptVu LPWUKWn', 87, 91), ('azAZTqRtvu', 98, 96)], 1) == [100, 95, 87, 98]
    assert candidate([('lIfFZPFFhAKidoUvtW', 94, 104), ('OPp sdp zpoJt', 102, 98), ('vmqBbqLOd', 94, 97), ('EwNrWXlFrZdhaIZC', 93, 95)], 2) == [104, 98, 97, 95]
    assert candidate([('BZiVQU GJzhPQX', 96, 103), ('gQsVkXo yIvodte', 100, 101), ('IIzGPArLPgquTro', 90, 92), ('TLvUvXpQnoDfhg', 93, 100)], 2) == [103, 101, 92, 100]
    assert candidate([('kVfcmZFWfd', 97, 102), ('Y GcFqsnnU', 94, 101), ('IJjdObtIQXHZFqx', 86, 94), ('yYVMlbT Hl', 90, 93)], 2) == [102, 101, 94, 93]
    assert candidate([('TopwSnVKLnOBmEQZ', 102, 100), ('dRQcbvkqpObyOsW', 95, 97), ('hQfBsiWLTX', 93, 96), ('AEzaItLEPY', 89, 97)], 1) == [102, 95, 93, 89]
    assert candidate([('tHfOcwypBSI', 94, 98), ('Wibhgiw', 97, 94), ('NthFAz', 90, 93), ('UXsabwfkfvgvrTgU', 94, 93)], 1) == [94, 97, 90, 94]
    assert candidate([('lXTWrHwuNkgeAxsc', 101, 100), ('DDDEpBkcZmpVKTw', 102, 93), ('MnhGFkc', 89, 96), ('ZRqgxSnKcywvTRPWRg', 95, 100)], 1) == [101, 102, 89, 95]
    assert candidate([('UCgPWIXSmopiMWDEg', 98, 95), ('OxpvCYslaYqElvv', 100, 92), ('odIHZqX', 93, 91), ('FfFLePcMOw', 90, 99)], 1) == [98, 100, 93, 90]
    assert candidate([('JtIKpYqEfsAXTECaP', 93, 102), ('RgIGfZMAnLymc', 101, 92), ('EvgEvWFcfPMGXL', 91, 98), ('NhlpWN qxIRbCop', 91, 101)], 2) == [102, 92, 98, 101]
    assert candidate([('xUCmpzOyjoTlVxtONs', 101, 97), ('ZQeacKmMTh ', 99, 95), ('NYXpqbnMYuVX', 86, 91), ('hsXGASUTI', 99, 102)], 2) == [97, 95, 91, 102]
    assert candidate([('UgDLxXPAIqqNCCU', 94, 98), ('KTRXSOtPMGLaPmd', 101, 96), ('RwaAibiAkI', 96, 94), ('lvhSSjEiIMpg', 99, 94)], 2) == [98, 96, 94, 94]
    assert candidate([('gRdSBDwTqy', 102, 94), ('WnmYslfPUjJpo', 96, 93), ('uezxUN', 96, 93), ('SoVDasHAJVVs fDHt', 93, 93)], 2) == [94, 93, 93, 93]
    assert candidate([('MRwIYJTYcr', 95, 100), ('vkisVTqWgpI', 97, 101), ('UqazsA', 93, 99), ('NFA KOYQbDloSc', 95, 101)], 1) == [95, 97, 93, 95]
    assert candidate([('BgKQKZdDwjDGmruQpZ', 99, 96), ('KzFvD YHPZI ', 101, 99), ('rtTVpSRGmHd', 93, 95), ('hZiborpLZgCqm', 95, 95)], 1) == [99, 101, 93, 95]
    assert candidate([('pZiPuHaGz WYRqwAju', 101, 94), ('AzQRVrs KId', 98, 91), ('EzANEGjQmz', 90, 97), ('CYNySVdhhugW', 89, 97)], 1) == [101, 98, 90, 89]
    assert candidate([('eFErrcUFwjIP', 102, 102), ('qrowkqDd', 92, 94), ('NEOcXyutnB', 89, 93), ('RkB eQUpRgdGyJ', 98, 94)], 1) == [102, 92, 89, 98]
    assert candidate([('gyjJUYSwKgfVkUlt ', 100, 95), ('hIrMNmSN', 94, 92), ('NPTUAfdxug', 95, 95), ('VCXPgxzSzrlbSKzRJ', 89, 94)], 2) == [95, 92, 95, 94]
    assert candidate([('MIkEvFdCe', 96, 103), ('k hyiwFMC', 92, 94), ('tShCZcTpkWkvpt', 95, 93), ('DQIzolSxbEwemZj', 99, 94)], 2) == [103, 94, 93, 94]
    assert candidate([('IIMuECbxKafjtBgg', 95, 98), ('AJBGLrWWw ', 97, 99), ('QDN aYlzX mptCl', 95, 90), ('xSCpRYxTy', 97, 93)], 2) == [98, 99, 90, 93]
    assert candidate([('vOKAIADWxlwFUdgc', 93, 101), ('VTPVTBPyIA', 97, 92), ('hdKCWa', 87, 91), ('BUpwxUfUXo', 93, 98)], 1) == [93, 97, 87, 93]
    assert candidate([('pbKprBVWEiO', 102, 100), ('QWnyeN', 100, 92), ('xuuSGCpJuWZJIV', 96, 96), ('t YsMLSwikt', 98, 100)], 1) == [102, 100, 96, 98]
    assert candidate([('zLpefXP vBAktx', 102, 94), ('XtAZQsUDblcQx', 94, 92), ('btsLxlONNiPlP', 95, 97), ('TQFFQY HgWCpy', 91, 95)], 1) == [102, 94, 95, 91]
    assert candidate([('bhXoyoiYwqCwGJZ', 101, 98), ('QyJtgqGIHMffARI', 92, 98), ('TkFUwnup', 90, 96), ('gOiSqYejKEOXldM', 96, 93)], 1) == [101, 92, 90, 96]
    assert candidate([('JUUxwNbBHuGXyEQoH', 94, 99), ('JGrsTIzINZJ', 101, 93), ('QvnmJdRdqcvLLbi', 96, 89), ('zvPYuvlMxugdh', 98, 96)], 2) == [99, 93, 89, 96]
    assert candidate([('URAxRhOuWZznRY', 96, 104), ('kZluIoXiVrOqRWY', 95, 98), ('eGquiDecfTDxN', 92, 90), ('oSaWQQNOcadRg', 93, 95)], 2) == [104, 98, 90, 95]
    assert candidate([('zlKEZBtTcMR', 98, 102), ('tWMOpaRrmJRsDU', 97, 93), ('QGuVRV', 88, 92), ('xzfCnVAXpLltd', 93, 101)], 2) == [102, 93, 92, 101]
    assert candidate([('TqgOldoFidWVyTBqf', 98, 101), ('WLgFqTTcbcE', 101, 95), ('iufQEf', 87, 92), ('qfpPvidJhMcUSFTp', 97, 103)], 2) == [101, 95, 92, 103]
    assert candidate([('lBquYITSYLDiRNC', 98, 102), ('XHPcFHd', 100, 97), ('bgmTSnqPtKHhde', 93, 89), ('nxjBgInLk', 94, 103)], 1) == [98, 100, 93, 94]
    assert candidate([('THnTVzfcjhdjQTMfIi', 100, 96), ('bjNitORTc', 101, 95), ('susPWTGYw', 88, 94), ('ZoIVeqOLIgQKS', 95, 99)], 1) == [100, 101, 88, 95]
    assert candidate([('UofhAHbDvhZMSf', 93, 98), ('vFyMBWQ', 102, 98), ('E asXRcL', 94, 95), ('QhRNdLxE puYECHvt', 98, 94)], 1) == [93, 102, 94, 98]
    assert candidate([('ylYIPfmlgI KWui', 101, 103), ('oLVnccusd', 94, 92), ('jvksolXKB', 93, 99), ('mtQCeXzoNrwyZi', 96, 103)], 2) == [103, 92, 99, 103]
    assert candidate([('emSYcABEgVyoIs q ', 100, 95), ('MyVayRqO', 92, 97), ('N yqTVbTfbmNUC', 91, 92), ('imyNOrHYmG', 97, 93)], 1) == [100, 92, 91, 97]
    assert candidate([('oWmtfnnHvtSPaoICk', 101, 103), ('HaElcvg', 94, 99), ('vgNEbNauQxh', 88, 89), ('nsRbKVoaUAQ', 91, 97)], 2) == [103, 99, 89, 97]
    assert candidate([('hVjEOoHOf wOYt', 97, 94), ('TAUOACsmEsxO', 96, 97), ('BLZsPxQuCB', 95, 96), ('ytiSjKfqWtJMavXUu', 99, 103)], 1) == [97, 96, 95, 99]
    assert candidate([('hukdauhbqxT', 103, 101), ('bIv xOHLVkzrO', 99, 99), ('BtAZxMeV w', 86, 96), ('pazOHvQUKHM', 96, 94)], 1) == [103, 99, 86, 96]
    assert candidate([('py mvcxOiM', 100, 99), ('TAwNoi', 98, 92), ('gSMnrkMcedya', 86, 91), ('kQXgWcGHfnVxPaG', 90, 102)], 1) == [100, 98, 86, 90]
    assert candidate([('FHMqcOlyjDfsjF', 96, 104), ('WeIPgD', 102, 95), ('DACmByr', 89, 96), ('yOAHBEYAEWFFOViPlH', 97, 93)], 2) == [104, 95, 96, 93]
    assert candidate([('R iutBGmeuzbXFx JA', 97, 94), ('VsQUMJeZmghuw', 95, 101), ('GBvzkf', 88, 99), ('LnPpEVwmSJLpoC', 90, 101)], 2) == [94, 101, 99, 101]
    assert candidate([('oNeuYJdEH', 97, 101), ('gMjSaNOpJwekf', 92, 101), ('RZZrYlkDpXwkR', 91, 96), ('UvdpbYaVI', 95, 98)], 1) == [97, 92, 91, 95]
    assert candidate([('zApQywmvdl BwWlQu', 95, 94), ('WrlLkUbztVhW', 92, 91), ('lVSwZvbXb', 87, 99), ('rBWjjwmdC', 92, 103)], 1) == [95, 92, 87, 92]
    assert candidate([('WkFbldvDw', 94, 98), ('tEKQRCETST', 102, 100), ('nVborUrOd', 96, 94), ('scFXXVcUwKT', 91, 98)], 1) == [94, 102, 96, 91]
    assert candidate([('RHLIkuWVrxFAwETHag', 103, 104), ('sqOmAnsQdR', 102, 94), ('EjVHHZdtla Wrh', 87, 95), ('YbuGcukofqOIInLAKE', 92, 97)], 1) == [103, 102, 87, 92]
    assert candidate([('AyaJTDfvfmJSMIpuiN', 103, 104), ('nPWTYPyrTwKP', 101, 100), ('uuVotq', 88, 92), ('xhlplTcJzSteX dLi', 97, 97)], 2) == [104, 100, 92, 97]
    assert candidate([('ICaCrkedaIFymnsw', 103, 99), ('XMdjylETHTICz B', 97, 94), ('CGOSBQdKRQ W', 86, 97), ('qwVUQqUiqhBZvRTkyH', 92, 95)], 1) == [103, 97, 86, 92]
    assert candidate([('qWuTMuVaXrJrlA', 94, 101), ('wMWbbQ', 95, 93), ('FMkOFeLqDJTR', 92, 93), ('KRWYgJYhqBWk', 91, 102)], 2) == [101, 93, 93, 102]
    assert candidate([('rYeNAVXzocnK', 93, 101), ('FDwEdQKSU', 92, 96), ('ERCKutlOLYVVLuM', 90, 94), ('AbztYgSVNqrGrhi', 99, 96)], 2) == [101, 96, 94, 96]
    assert candidate([('sgWyFehGHsqEKnliVl', 98, 98), ('LVfPPOqnBT', 99, 97), ('asvfcggNMyai', 88, 95), ('gtjXHthASZP', 93, 96)], 2) == [98, 97, 95, 96]
    assert candidate([('EnpfVM PYbSkbeuv', 94, 97), ('DQgVviFRJjpgns', 99, 92), ('GxoV Z Uai', 92, 92), ('bAfOYfggVSnevAS', 93, 94)], 1) == [94, 99, 92, 93]
    assert candidate([('Cms PCQABLjE', 95, 100), ('wBMVXgSAHM', 101, 96), ('EcwWJm', 92, 90), ('JCflbkrvqF', 97, 93)], 1) == [95, 101, 92, 97]
    assert candidate([('CERYEQUg ', 93, 100), ('hCgosfuwup', 98, 96), ('QQgGYNMaO', 87, 96), ('xaodzYbQOccsE', 89, 103)], 1) == [93, 98, 87, 89]
    assert candidate([('MPTqnpwCO', 94, 94), ('nJvCSQK', 94, 99), ('lIefhh', 87, 89), ('ccAgUVoJy', 93, 94)], 2) == [94, 99, 89, 94]
    assert candidate([('YbvnXlyHnBVTDXuT', 101, 95), ('tOLZdGL', 93, 95), ('drkxSFIZIBOc', 96, 91), ('tdFiPfJAHuUFeHug', 90, 102)], 1) == [101, 93, 96, 90]
    assert candidate([('QzqEGWFMSiCQXa ', 98, 100), ('fMJLBewSKOYMZ', 95, 101), ('nsjTrXjQaMhJqdg', 88, 95), ('FCBbxadc k tbDeg', 99, 103)], 1) == [98, 95, 88, 99]
    assert candidate([('FAQMlbdvTozAqXZvvU', 95, 104), ('TOQWJEpwrTaGoo', 98, 91), ('nVofKBEcGiUrI ', 94, 97), ('pEaNMVOLqxQPqTpCi', 99, 101)], 1) == [95, 98, 94, 99]
    assert candidate([('sheeigCsDPuMag', 96, 104), ('fAq VuBFq', 99, 98), ('eSNUxDPE', 86, 97), ('iYzoSDlZCOcI', 99, 98)], 1) == [96, 99, 86, 99]
    assert candidate([('nykBBLeeHGIO', 97, 104), ('rhLKVgjSjMl', 99, 101), ('EMetlGHICFx', 87, 95), ('NuCYahCRMB', 92, 97)], 1) == [97, 99, 87, 92]
    assert candidate([('yvgySyAtxAbmm', 97, 94), ('hufwXgDeGiTDz', 93, 100), ('CePXNSattXgS', 87, 92), ('tMCYB BKhRI', 99, 98)], 2) == [94, 100, 92, 98]
    assert candidate([('aqlBkYAXtlhbz', 93, 99), ('PttFbjY', 93, 91), ('KZTrRCLCrUttFk', 90, 90), ('rYcIeTKobIgj', 93, 96)], 2) == [99, 91, 90, 96]
    assert candidate([('QjRqsciOBxLuhlVQfw', 97, 100), ('fviDKCxOBj', 96, 101), ('zWkaqZglPOGq', 93, 97), ('dATQxylaiEI', 99, 93)], 1) == [97, 96, 93, 99]
    assert candidate([('iNWa YnqqS oD', 100, 96), ('XwPpnLNzKJvYdB', 100, 97), ('qLznKhXWVRpxdq', 91, 97), ('eiVapDOLW', 92, 102)], 1) == [100, 100, 91, 92]
    assert candidate([('XgYpUnyjHtstkbIXTO', 99, 94), ('mvaCPgT', 92, 96), ('aQKO Qy', 90, 97), ('wnFsFDJVUlnzcZXeu', 99, 101)], 1) == [99, 92, 90, 99]
    assert candidate([('HtJpLafmhJVFvjR', 96, 94), ('OVs OhCC', 100, 92), ('EaFuY ', 90, 95), ('FLWCcUqQzG', 94, 102)], 1) == [96, 100, 90, 94]
    assert candidate([('zuuuzlwHt', 103, 98), ('igvxKkkxsKIroGZ', 102, 95), ('yXBd JjBmafJLmo', 92, 90), ('PENVWxdESilNWtXGL', 97, 98)], 1) == [103, 102, 92, 97]
    assert candidate([('TySwdlUYgaiiPukcRe', 99, 97), ('uvafvInXCtsh', 102, 93), ('fZbUFmN', 94, 96), ('jSpQPIsZwQLxZyes', 94, 99)], 2) == [97, 93, 96, 99]
    assert candidate([('bn yRYzMnSONWEY', 95, 103), ('PCtcXbWDSCyGYwE', 98, 94), ('hpgLikTak', 90, 94), ('uSYieOKfNLvUhk', 91, 98)], 1) == [95, 98, 90, 91]
    assert candidate([('TtpsanBsNvyyqhLm', 95, 98), ('qUkIYzl', 99, 95), ('LKEDqZM', 94, 91), ('nuBHKLgeyAC', 96, 103)], 2) == [98, 95, 91, 103]
    assert candidate([('oGwiuLSYPi', 98, 104), ('JlJnfhvWTEY', 99, 100), ('gVbKCN', 93, 96), ('CTnHoPQZmcaV', 90, 96)], 1) == [98, 99, 93, 90]
    assert candidate([('JwWygYdFj', 103, 96), ('zEWcwIX', 92, 97), ('jTyXdHWwKfqDcUK', 88, 94), ('oUdADuxCNTlzOhj', 89, 97)], 1) == [103, 92, 88, 89]
    assert candidate([(' aDcnGumPaAOoA', 101, 95), ('ggcgNPgiMalph', 94, 99), ('eJNfmgOTLoxxqrq', 96, 92), ('RhISNpUXUdyQkdTNy', 98, 99)], 1) == [101, 94, 96, 98]
    assert candidate([('m kk LnohwNpWbXoo', 93, 97), ('afTJDPybFbKSUn', 101, 97), ('CKeecfQQftYWDPS', 96, 89), ('pmIwNHvYQ', 96, 98)], 1) == [93, 101, 96, 96]
    assert candidate([('oGLqQulozlAvOZoV', 93, 103), ('jfVBATULG', 98, 92), ('vkwqaWzJo', 86, 95), ('fvzYmxmgzV', 94, 99)], 1) == [93, 98, 86, 94]
    assert candidate([('gXGhvXuPAW', 97, 99), ('lehbbiEsD', 98, 93), ('MFxwfqqL', 95, 95), ('qEBi BvFNNhfu', 93, 94)], 2) == [99, 93, 95, 94]
    assert candidate([('IMGV koPAAhBSdUbsO', 103, 95), ('IdIomWIMt', 99, 97), ('PhfB sPN', 88, 94), ('luMjxEbXV', 91, 102)], 1) == [103, 99, 88, 91]
    assert candidate([('ypqycROqR', 97, 104), ('eePxZXjVPuBNb', 93, 96), ('ZAQuYzF', 87, 92), ('OERcFYyQCILnCBy', 93, 100)], 2) == [104, 96, 92, 100]
    assert candidate([('ItQKAuTRaPrBf', 101, 95), ('tXXPTdIX', 98, 94), ('RAOIWdG', 88, 91), ('YjUwyDrPDDxcC', 90, 103)], 2) == [95, 94, 91, 103]
    assert candidate([('dFAVJiwHojuBtCrxGl', 97, 101), ('iwmvKEaVBmh', 100, 94), ('ePGUNhE', 95, 90), ('WAJwTWolVGpTWDT', 99, 94)], 2) == [101, 94, 90, 94]
    assert candidate([('oELcQvADHxuIA', 94, 99), ('IxePAwkSNzuTVn', 97, 97), ('PkxmbdjOWwNc', 87, 96), ('awDKeyWXRn', 91, 93)], 1) == [94, 97, 87, 91]
    assert candidate([('ermmyhKMYd', 102, 101), ('D jKSGt', 95, 93), ('YELHCwWBJVD', 95, 96), ('IcqNYixMH', 91, 97)], 2) == [101, 93, 96, 97]
    assert candidate([(' PQVRcexBYDKsP', 103, 98), ('SabBLhs', 96, 99), ('ciEyHSSaWjEtoW', 95, 94), ('vNigZLYLm', 97, 98)], 1) == [103, 96, 95, 97]
    assert candidate([('INxPsrtWZeQU', 96, 103), ('CyMjEcMAIEav', 93, 97), ('eAlUpwwFlZK', 96, 97), ('FQZmwaiRG', 98, 94)], 1) == [96, 93, 96, 98]
    assert candidate([('qsgrKUGrsIt', 95, 98), ('iKXeSbPI uXh', 102, 93), ('xiPpAHglogAT', 89, 96), ('rRWVgATQNYPxZd', 99, 99)], 2) == [98, 93, 96, 99]
    assert candidate([('Vg XIXMFoeWobRZYE', 96, 95), ('gdhBiGL', 95, 93), ('yZleOVrEMcBS', 93, 98), ('xjWKXwjvcQcWC', 92, 93)], 1) == [96, 95, 93, 92]
    assert candidate([('jUbsXCGXPxS', 97, 103), ('lotllUKNh', 102, 91), ('lq THYPlTjofRi', 94, 92), ('JvQU BQvYGnOnOEHvw', 98, 94)], 1) == [97, 102, 94, 98]
    assert candidate([('iRDWcXXINji', 93, 96), ('RUHjNMcNn', 97, 96), ('JoxpXMrRtZ', 88, 99), ('CZVISUzPCAsoryUMDx', 98, 96)], 1) == [93, 97, 88, 98]
    assert candidate([('slOneoPnW', 98, 98), ('easmnKS YvGhMhw', 96, 96), ('CQUwEo', 94, 94), ('EZnDBYGvvkVyN', 92, 95)], 2) == [98, 96, 94, 95]
    assert candidate([('JvblJvxLPyd', 94, 103), ('oI elxkOM', 93, 98), ('CTQMEmvFLI', 95, 98), ('PnZAVGkewewo', 91, 100)], 2) == [103, 98, 98, 100]
    assert candidate([('BKjppyWEzyQXzgEo', 103, 100), ('sWypJYtZhnb', 97, 94), ('oCPPOCl', 88, 96), ('NZNCDntdsiCxqyIbRf', 91, 95)], 2) == [100, 94, 96, 95]
    assert candidate([('ACuRkihKDZugRHFT', 98, 96), ('rWgfSMVFzNVqvQ', 95, 98), ('rfmvUKdl', 95, 91), ('EXMdjqHADI', 89, 94)], 2) == [96, 98, 91, 94]
    assert candidate([('LzGaUkdwV', 100, 101), ('qOccRBAd', 100, 98), ('AbdmJfOnUUB', 90, 96), ('SJDKYDomzAVKphAu', 94, 93)], 1) == [100, 100, 90, 94]
    assert candidate([('ZsaYNgoyMlfM', 102, 102), ('SCseSal', 92, 95), ('cxKfjCpHkMNqCNx', 93, 89), ('FBYyLjSVxDuZXgtit', 92, 99)], 1) == [102, 92, 93, 92]
    assert candidate([('biTpOLnCOYqGPvn', 93, 94), ('TnKcrBBHjC', 98, 92), ('JvfUdmTyGpmo', 88, 98), ('xn fpZLzlejW', 97, 98)], 2) == [94, 92, 98, 98]
    assert candidate([('sxXeYA bxMha', 97, 104), ('ZFmNemLuDQGf', 95, 97), ('u XXN TFdLpl', 86, 94), ('DpM aWUaXhaLir', 91, 97)], 1) == [97, 95, 86, 91]
    assert candidate([('xzxCpvydSsbV V', 102, 99), ('NcAc B ', 92, 91), ('PPqJekhhatH', 96, 92), ('vrRBMhBef', 95, 94)], 2) == [99, 91, 92, 94]
    assert candidate([('PARUBKfByVW', 102, 100), ('gcbgJj ', 92, 93), ('GTFIIxMCL', 96, 89), ('uKvFZtHAyZ', 97, 96)], 1) == [102, 92, 96, 97]
    assert candidate([('dCutjehyaPKwRJL', 99, 97), ('LvTIhsoCEaNlGk', 94, 97), ('dEgVJUZTL', 93, 93), ('cgwmmHuruzCwic', 93, 97)], 1) == [99, 94, 93, 93]
    assert candidate([('NcTpbcGIaYRO CwUz', 98, 96), ('absefzcWyRWHQOL', 97, 93), ('oaBrMFduFzxRFI', 95, 97), ('CcmMQSeuCRaqiySI', 89, 100)], 1) == [98, 97, 95, 89]
    assert candidate([('NVmYekUWgFuwOen', 100, 101), ('DUSExtFr', 95, 95), ('KNhQYYwt', 88, 92), ('BrmVbueOUiyOzVzhkr', 98, 97)], 1) == [100, 95, 88, 98]
    assert candidate([('eiCRglosVRvofTNF', 99, 100), ('MGNlSs', 98, 92), ('kXUphWY', 86, 90), ('VXNsSxuHUgAN', 97, 102)], 2) == [100, 92, 90, 102]
    assert candidate([('IWiqzUQGClprveCn', 100, 95), ('hTrJYUeXpt', 98, 94), ('eEBFCrmpGuQ', 91, 89), ('XDKhdHgbbz', 93, 99)], 1) == [100, 98, 91, 93]

if __name__ == '__main__':
    check(extract_nth_element)