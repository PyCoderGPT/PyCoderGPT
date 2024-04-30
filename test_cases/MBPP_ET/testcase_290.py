from case_MBPP_290 import find_adverbs


def check(candidate):
    assert candidate("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert candidate("Please handle the situation carefuly") == '28-36: carefuly'
    assert candidate("Complete the task quickly") == '18-25: quickly'
    assert candidate("suPCPNOfneVFxCLcPPhMcwHFvZRlS,eJHcuhJmjznev") == None
    assert candidate("DWsuBQJGRYhsshaEaLoNChS,wMsuQegOkxbvBQf.rarV") == None
    assert candidate("ZymdsAgAf x ysIlowv.Lu  fdD.KzxpDmnPyii") == None
    assert candidate("rGgo,BJ untzMLyitoRqcSSBfPxvYjCdH.qFiOlF") == None
    assert candidate("sbnmklffIUxJFyqgjLqEnPyrTCTPkkAGOf UVEwEnQGGJBWB") == None
    assert candidate("npyHpKimAvReUJI.XAGMgGvPmKJJvRLIWIrFRJeHrZ") == None
    assert candidate("y,iT,bltowokqhLKdphxptUHeuvgJjGPtVdMWgyGTYHNaMGH") == None
    assert candidate("QKAPxqGPWrbRkCPjamcjQGtXDKLWPOigWIbdrYyi JJ") == None
    assert candidate("COemmHfQeiggoercYzYH,UMJhulGd,Z h.TFHwPCS uFI") == None
    assert candidate(".R,cqIwzWRTqTzNQUpGJJS zpBSh,nNXhew,JRh") == None
    assert candidate("LZefIAnEipvjcEAjkBRFZ.DyTeO.DAhCYLaZnBF.mpw") == None
    assert candidate("oUhxXuHKYLcHtWjinLt,omlOKptVpNYUQvnpafiXReUk") == None
    assert candidate("qTg.mttfIXsgwcdOMOGVjLYMSafXwSAfmDCKDdWlBwxx") == None
    assert candidate("KvOw AeSYckqxjcKqHiuDreCcpBlNs,tTIINOeR") == None
    assert candidate("EKjmpNVZWqDFAskcxaNYPIROLKLUCfFFLYNXCeYXuCA") == None
    assert candidate("TQmfTFNRCMFQHXBFkHG,uUmeGNsuYTbInNoCs,Qi") == None
    assert candidate("HtABvyyClOJ,pWecrjUdGFiMuYBXwVD nEfW.UswMcI") == None
    assert candidate("WqXTJkNeRjbNyruzMXYvpprHCkdlo,ag.LH nFlSYRY") == None
    assert candidate("qULeyBkYthwFJVzZoMADPtKhulVRtdhxWWWastn") == None
    assert candidate("xNmCFZewlwl .BxjoGYgiNyHxtAEqcsDKgYLxHj") == None
    assert candidate("ZekRwOgInHmErOBQcMCfgFq,MDiPFOjppqCfoTYX") == None
    assert candidate("cpubzPAwwQNDc,ThgHacQDVRGamopaixCDYjgRwBboxJ") == None
    assert candidate("ugelVeDdQAcAQjFlcnXw,CvLkTvxvbPZTHvXvYX,uzQbeS") == None
    assert candidate("qhyGPmcPHaiWSYr wYSVa,YtQveI.mbzDLQWdgZ") == None
    assert candidate("WgLVBEFlhcIi  cMZhApzNcLhCakNFiBtIRtQJeJ") == None
    assert candidate("xklHfOBPiFDewqhgTJUAVcUyHBrVq,CembXMvuA,UXuF,Cxu") == None
    assert candidate("ZrhRkweLyikLgcgX.XEPoQRMtB WHOF,b dDAn.WzffiTPds") == None
    assert candidate("aAsKDNBwQupMJvgpUQGKnMgdJuNek olNkPuhtJh LGd") == None
    assert candidate("YPMZXhpyqRsb WK,TrAD..yWE .fsK sXDRNhoak") == None
    assert candidate("hOpgzpRvxNkhaWOeZpiG,,wXqz QdZXvU.zg.xhj") == None
    assert candidate("PNvVoEp.gChwITJXoKcWjdyicfcJvJwliK,uwfe") == None
    assert candidate("udjAamPvcNwEzAuEdUasj iTXVk qAquVkFDT lkSIbjBI") == None
    assert candidate("z ngVNWhxVZkyT.erDZLEpusCfJjSZbNATQSMskSlVM") == None
    assert candidate("QkbmGwgaHebEUuWXJfvEwbEcGVUNgCqCfGqWMsn") == None
    assert candidate("AnPtugikyuOZaxREqlmrxIwWiZg zCfvuXGD") == None
    assert candidate("DKwELSZiwATJYWkMFhirMCdbYHaZfdlOdUbviTi") == None
    assert candidate("SILHMBkneXMZpTmz aERuDRerAyTs NjJuCKA") == None
    assert candidate("cmHunVIzWpXZMPrBgFSkyooXtTWtovpGkjc") == None
    assert candidate("mAUQYgLOLsPtSJFKEO vtqzDToijYkkjM") == None
    assert candidate("OfDDnpKlMFR DNZtffnMOxyfjMKyrDRLCMs") == None
    assert candidate("YSCwlygnKDvZhJaQFREmskyfSAvOzULKmIMzCaQ") == "0-6: YSCwly"
    assert candidate("GOuKpJvnMkkNuwGJmPmIEmjxnKYvYCwRp xtXIQTXg") == None
    assert candidate("uYfiMhKKPvUuJoAsQTcvrRzAPjYcyakvLTzBleN") == None
    assert candidate("BciQqIbGxTWVTGHBYnSVJnDSCm ySEPjqgBTn") == None
    assert candidate("JwrEOKfvTNFxGWoIvHiwRjO JgFDtztLCWbH") == None
    assert candidate("LQLUDaRiOKkifDpFiSksNMGexvtbzOtpWBSiCWebPb") == None
    assert candidate("oRVgHRtvumUsswsUXTKY HaPfZtSHbrQorGcdURdWu") == None
    assert candidate("KojesWlNMprWDaXgUgYWdJmdKqNjpimjkFGD") == None
    assert candidate("gZuVDMEQmLCEqjYlRNYIbyQmmFCsiwCNzad") == None
    assert candidate("EWDxcAuKrUchtEGOADZtWUcnPNnmpafmf") == None
    assert candidate("mhiUFJaXj qXanenrvRZdcMGeLIkuEwJDumrH") == None
    assert candidate("thtFlgyzDNyXMXWoDKpJOwDlXDwsDOsTK") == None
    assert candidate("cGSqbSKjUoZYpfbQJIlezVqIOKtLqSqFclnGcvmzU") == None
    assert candidate("gJUwCXuiombZZZg kdawftLeb cmNspMabWY") == None
    assert candidate("mCPVuktSTNlIPsOsAQVZboihwWkjhpZFAnamx") == None
    assert candidate("RCkrAlKlqPeaPoAtfSKHqeQQTnrifiAUSfct") == None
    assert candidate("ddfEIofXtzmNGrVLVhb mRWufZGuXxHJBCcABaypzS") == None
    assert candidate("hZrCgQWKBUTxgfvoKmdcgSwBbZyEnXXLyCqEsvsvP") == None
    assert candidate("potBlgeqgZsnozghqjVpKRolCDdgoVoLANGPVh") == None
    assert candidate("CzXnHIhdPuVrQHniOoMcELIvelunhbilQiuMBwk") == None
    assert candidate("pOBbyQKDHyYTMEzSTMqdnEjhGhSnqlDhpgjPQPQ") == None
    assert candidate("ohbzQJfxfXhxSOrCLhetBJmDkRjvLTltETh") == None
    assert candidate("rxuOOvYL ZbKkTlbmccZYWjUMJryegFfNRwsg") == None
    assert candidate("IKhGWLccQJvkKcVgFRcNbdkfOGFPIpqkAcQR") == None
    assert candidate("XItkJPyywahqiaNYgaqRXhXRSyVSqfqRmr") == None
    assert candidate("QUjnGpkiAlnCLJMbiWvVpBSDujwVI nmlfgDtrZ") == None
    assert candidate("ycUjLhkZehuhPRNkrvsJpsWeuPCVi") == None
    assert candidate("CikbXwbzcRAUAEGCQiQrJhS") == None
    assert candidate("UoVTSnlbjDiTQTXqRnSsIhyyQAl") == None
    assert candidate("PziuHhdWGcuxDveFFkMqDZels") == None
    assert candidate("gHkpbJAEeohoLgJBGmSROJvcgSU") == None
    assert candidate("RdalOdowpcCrPoPObFAHMGJnbpFUn") == None
    assert candidate("DoCcQMFMuaMCTsiOzcg IZ") == None
    assert candidate("hksLFxHoCVBtKSJQxKRdfaFGQtO") == None
    assert candidate("dhAuRdlGbpiDqemMHQRtcGJ ldEF") == None
    assert candidate("cXaBydrMUyUkhUKtPqOTkgKzH") == None
    assert candidate("psOGcwmLETzAMdlGUjolhalmHij") == None
    assert candidate("kHPyoZhggbNqZKTJvIeNUQFRgov") == None
    assert candidate("hnwNlZGGdLNtiKrJjcebERvb") == None
    assert candidate("FxaIjadwEheupxxcPAcGBsgnssen") == None
    assert candidate("KyJqRRiUKHguoHkUKpxzfbk") == None
    assert candidate("nJTmmxSfrBcocUsaosCBZWeO") == None
    assert candidate("eKVEsa tYUinTOceMFnsefAwVPgyoP") == None
    assert candidate("elykFcAnvsXbxdmMMgjbvHwtThZDmg") == "0-3: ely"
    assert candidate("YhFDsMj f flaZhrwEhQxpgFpQ") == None
    assert candidate("K GNXhNqbMgcKMNzWDOFmav") == None
    assert candidate("tAVZpEEhgAJdVaJhNmEWee") == None
    assert candidate("VCGgALxuMdSIiyQXYIHCW") == None
    assert candidate("kQaqYJFxGzDMZBnNpvJOtDbajWwLN") == None
    assert candidate("oUfjvSOGkzyqHNctKrJCOcaNZ") == None
    assert candidate("liUYxdNFaSNeepTtHphFrnllGaBfEg") == None
    assert candidate("T ioxddaXwMrgxOJjVutWpRDiqd") == None
    assert candidate("dlLNIAUsfmeCAMBbnpXOEATkReQ") == None
    assert candidate("kdwYjmXVWuWDbdZfRxBcWFY") == None
    assert candidate("urMITQXLxHvmgWaSMdejPEW yp h") == None
    assert candidate("lseilIMWesrJINmJcCFpEAvA") == None
    assert candidate("yXywRgWEQGnQYmrxoSHmTWaxNY") == None
    assert candidate("KsQeeMqazwuGkIvnTaIopPr") == None
    assert candidate("THhjgeLiRFWzQTkxWlqCKMoE") == None

if __name__ == '__main__':
    check(find_adverbs)