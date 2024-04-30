from case_MBPP_272 import extract_values


def check(candidate):
    assert candidate('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert candidate('"python","program","language"')==['python','program','language']
    assert candidate('"red","blue","green","yellow"')==['red','blue','green','yellow']
    assert candidate("KvjcKHZdqYhwePYmLhhVyDYOju") == []
    assert candidate("FvPCOZzOSvPrjjZIoOqku") == []
    assert candidate("aZUbNFpKMierUHwmkCqoz") == []
    assert candidate("lWa EtnSbrGfZJOCfuW") == []
    assert candidate("pvJiHttpHyQYeJi,ANNIXbW") == []
    assert candidate("NIpqQjryYFokgHMnOU") == []
    assert candidate("ZGGEbkxSskIWrLNBXRy,peYRalv") == []
    assert candidate("TtPSYrohXCie,KayAzLrzc") == []
    assert candidate("bBwkYD lKNZWqFoEAyCtGZQVQ") == []
    assert candidate("feEHcEhlIfTVogsI qP") == []
    assert candidate("DbYmhuVLvdtgGRjgkvGcF") == []
    assert candidate("KMdw,OP,ELHvWvwqrbrhYldH") == []
    assert candidate("sOXYNKr,DHUvdiiLVbjPvfdSbi") == []
    assert candidate("RleOsFErmjLoUDXjxJOjYUSdS") == []
    assert candidate("GCUZgS O,Ytvi,fEZH,SZHuuyTh") == []
    assert candidate("UHIUDDGcaVkKYgFwuzHjXBTI") == []
    assert candidate("xEXTrHqcJYiFwmgnypVseAkX") == []
    assert candidate(",BUNkXGbcRbLHnzGDutWSd") == []
    assert candidate("POUHbuCcodoxzzeExak") == []
    assert candidate("NtBtNizkAtjuDot,IFKPhN") == []
    assert candidate("KmuOlGfceWHnPhvanGUgDm,T") == []
    assert candidate("bjIqtvlCFNWHrIBmw,iItI") == []
    assert candidate("mMCkyUcZOogYJIBIcMtOC") == []
    assert candidate("k,lBGbvcjBHiUSBFecVXv") == []
    assert candidate("ToPTtDCJg VDeWOTaFay,FtF") == []
    assert candidate("NgxdWqhGsGoFTppZymSbRQrCFn") == []
    assert candidate(",oD OkmotWQUVoJVqQFGd") == []
    assert candidate("QE,xvsNvCsGiPjgfKpd") == []
    assert candidate("FpOAnHqFJvUBZg,gTcLnl") == []
    assert candidate("eLiBJeHvUbxHDDFVTnWD BCR") == []
    assert candidate("FDEzsqsBXDERTz ZPlpwv,BCDQ") == []
    assert candidate("LhXBXOskCkFDkk,pKmodyF") == []
    assert candidate("blJAnicImFOChvAhOoju") == []
    assert candidate("mqreooxujpiduxggrydqbjzh") == []
    assert candidate("zhekdfu,gnvkkvfevfgdvfvxpjnfbtvo") == []
    assert candidate("dmyfpmqheggpvvlmtcahikhewy,u") == []
    assert candidate("vkdzownroefpdnjjzttkutxkodphrj") == []
    assert candidate("xdshxraktdb,fivzqpj,nbylfrpdejls") == []
    assert candidate("dcjqskkofqtmqkaogkvqgxewafdyu") == []
    assert candidate("lo,lulmaexcrtsfmzmrhurtblpucah") == []
    assert candidate("ytvxmba,oguznpmmszjtcvitbkvziw") == []
    assert candidate(",hdppwvzbradawbrijmmzajww,cp") == []
    assert candidate("gczsrsrnvoxvzycsyknkr,p,axdssbx") == []
    assert candidate("njux,,dlppnobzkpfvtgympjqcuszlea") == []
    assert candidate("hwgmdqtgvcdyqlsankljwgsbc") == []
    assert candidate("nbfth,caegcovewlkcaw,kaey") == []
    assert candidate("dnq,n,ilmkgweobdfaynwzrclxgxx") == []
    assert candidate("sobumpymsgcteonhqrzrgnedteuyeftkg") == []
    assert candidate("cr,mmcyojiqrrcijglqafdsjae,vwtsx") == []
    assert candidate("o,vcqdkbpsmkedqoxoqvvzqcmuzdosofa") == []
    assert candidate("jthhslcdoudzbwvaapsdjcamleghehb") == []
    assert candidate("hytovivvodapvahausneobrvzy") == []
    assert candidate("n,dxtyjgcdtpcgnvcswqmhjcuhcyrr") == []
    assert candidate("stszxyemmhbacixizsegbemq") == []
    assert candidate("fvznnh,cdegflmhfcqtrhswafhl") == []
    assert candidate("memrzusqbcy,jegrepnimtwjel") == []
    assert candidate("uligmskbvjdyaajapsgutcpfymyat,u") == []
    assert candidate("fdpcncgxdloszpk,snbddgcuyspzdnwes") == []
    assert candidate("qeclobbalhzkwgxaudkkmw,kdo") == []
    assert candidate("euklomv,xd,qy,nvurhrwzqtiwy,pn") == []
    assert candidate("dazsilehmkoy,ixtpdlnowsn") == []
    assert candidate("arh,ohikdyjcodmkyaerkpgaouhs") == []
    assert candidate("symrnoalmzisnrfsbqwegkhf,uzvqp") == []
    assert candidate("qdmpymxbxphwz,qyvfcmqzpmczqwau") == []
    assert candidate("qrvzgzisngrywjteehqlyllg") == []
    assert candidate("vijdezwmfeytqokfwtl,cbfriuz") == []
    assert candidate("jhdrksitvemlk,iyndtefhykvvsqn") == []
    assert candidate("oedsjpgioftzc,ulyzhazhcgpqq") == []
    assert candidate("xgssbxrnkbkqqdfgrcwwjwrccf") == []
    assert candidate("gkgfogbssfenmf,lgg,tcdupba") == []
    assert candidate("muknvpbfjzaaki,gxvftfklipq") == []
    assert candidate("qdeyqmpozdgreccdllu,ccdqgouponx") == []
    assert candidate("lssigjvp,vmsrqiqdyuniwosfjksle") == []
    assert candidate("aqvypjmphyhdxhzeqspbfxvbcsdtdkkzk") == []
    assert candidate("nsqhjhrpdlzmbjfybnou,zei") == []
    assert candidate("joiibqvicsvwkkuenndgbvjooyryfosx") == []
    assert candidate("wvjynomlrwl,saopolkbfxiteawn") == []
    assert candidate("elbyavwbrin,xuqbwmbdrjpj") == []
    assert candidate("wrusgaiepfulfotxdscg,mpi") == []
    assert candidate("pao,p,kg,eve,f,lpuwawpqdj") == []
    assert candidate("wnnesclatt,iqqlbciwrusktmrqg") == []
    assert candidate("fquvmddu,vqlbdcvlbxbwnss") == []
    assert candidate("blyezsbcqsgtbthbtgiqxhstlre") == []
    assert candidate("xygoapcymzaoclgiipozikqyvojwuhfw") == []
    assert candidate("eapguekxnsqfncveqclgtgxyuzlvhbequ") == []
    assert candidate("wma,rxrkjxbsqmcafmddalhydwvkzqlt") == []
    assert candidate("lg,bt,,hdtlopvwdfqiosdrwdhzqxckok") == []
    assert candidate("jjrumsicgsjpmrsqyeupfyywqrwlowgiz") == []
    assert candidate("jpymvqqzlkvnloujdjsptvhx,cdjxu") == []
    assert candidate("bepjqbnhnxllkfoh,yodhurwmkafs,") == []
    assert candidate("desagbupmgxftooidkz,lmbgagpvi,u") == []
    assert candidate("zocszygzdmytr,xcbgmiyxbpeppam") == []
    assert candidate("pjhpinpmvexmnrnbaud,njbcdub,gn") == []
    assert candidate("psehzemze,pwsirmrhrerndfuatfuf") == []
    assert candidate("lswqgepwncuqiylmehneaeolzmjvkof") == []
    assert candidate("vyjhlswriebkhdghsmnre,qvjmpvtekyl") == []
    assert candidate("jzbjfguhdjosskirkqccqbla,pqyko") == []
    assert candidate("fuczmqoyvodfchjloubyyzzkkd,") == []
    assert candidate("gixkdvteggzfhy,wswjdncokemd,") == []

if __name__ == '__main__':
    check(extract_values)