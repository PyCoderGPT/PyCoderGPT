from case_MBPP_201 import snake_to_camel


def check(candidate):
    assert candidate('android_tv') == 'AndroidTv'
    assert candidate('google_pixel') == 'GooglePixel'
    assert candidate('apple_watch') == 'AppleWatch'
    assert candidate("@m^_ss&") == "@m^Ss&"
    assert candidate(">*d>-p") == ">*d>-p"
    assert candidate("!euyc*@ro|?/ea/") == "!euyc*@ro|?/ea/"
    assert candidate("ac<bj*|rfn#&ux") == "Ac<bj*|rfn#&ux"
    assert candidate("j+aj=>b@hdt") == "J+aj=>b@hdt"
    assert candidate("$:cg**-") == "$:cg**-"
    assert candidate("ve_hq*") == "VeHq*"
    assert candidate("qlaph$jxon*&") == "Qlaph$jxon*&"
    assert candidate("l<-pef") == "L<-pef"
    assert candidate("oef:w-p:^f/") == "Oef:w-p:^f/"
    assert candidate("n?it:_tdh") == "N?it:Tdh"
    assert candidate("l%drc@n:-") == "L%drc@n:-"
    assert candidate("l~cbw$f_") == "L~cbw$f_"
    assert candidate("cby?b>?!m") == "Cby?b>?!m"
    assert candidate("tet_cv!/?!e:^%?") == "TetCv!/?!e:^%?"
    assert candidate("gne:/=%dl|<_") == "Gne:/=%dl|<_"
    assert candidate("z:&h+-m") == "Z:&h+-m"
    assert candidate("_h_md&we>e/vy") == "_HMd&we>e/vy"
    assert candidate("y~pjjs-#") == "Y~pjjs-#"
    assert candidate("dqf#ilf%m") == "Dqf#ilf%m"
    assert candidate("kqf^j:uh?iy") == "Kqf^j:uh?iy"
    assert candidate("m>cy~~hr|ngn") == "M>cy~~hr|ngn"
    assert candidate("#pubt#^%l/zjbch") == "#pubt#^%l/zjbch"
    assert candidate("qcvjjt%s/r+!") == "Qcvjjt%s/r+!"
    assert candidate("brtpl-$ty!h@i^:") == "Brtpl-$ty!h@i^:"
    assert candidate("onv^:v|gg") == "Onv^:v|gg"
    assert candidate(":np=emxg@nmn-") == ":np=emxg@nmn-"
    assert candidate("oznz^*evieap") == "Oznz^*evieap"
    assert candidate("rwe|b<k<a") == "Rwe|b<k<a"
    assert candidate("/m~l@$&th##>>") == "/m~l@$&th##>>"
    assert candidate("~iostp") == "~iostp"
    assert candidate("_?<pc/-upujuts") == "_?<pc/-upujuts"
    assert candidate("!j|jw=") == "!j|jw="
    assert candidate("qw*u_zay$") == "Qw*uZay$"
    assert candidate("q+z+secpkdw^_r<e") == "Q+z+secpkdw^R<e"
    assert candidate("jd?p%>xy^uw#") == "Jd?p%>xy^uw#"
    assert candidate("/w_~sqqbzvh&jh%bw") == "/w~sqqbzvh&jh%bw"
    assert candidate("k@q!ep|p$x=iax_n_g") == "K@q!ep|p$x=iaxNG"
    assert candidate("okqhsvx+dm$") == "Okqhsvx+dm$"
    assert candidate("hwqm%wa&@@y") == "Hwqm%wa&@@y"
    assert candidate("i&rm*wiitj_c") == "I&rm*wiitjC"
    assert candidate("ur>#sk~b@") == "Ur>#sk~b@"
    assert candidate("nh?uqh!g&&f") == "Nh?uqh!g&&f"
    assert candidate("-wngo@p>s") == "-wngo@p>s"
    assert candidate("=*/yx?hh%oatowu~jo") == "=*/yx?hh%oatowu~jo"
    assert candidate("hj|od~y:@l-ugw|") == "Hj|od~y:@l-ugw|"
    assert candidate("i$axvw/l~~k<") == "I$axvw/l~~k<"
    assert candidate("ne%hpb$/gmd_w^t") == "Ne%hpb$/gmdW^t"
    assert candidate("t*e&ph#r>c=sr") == "T*e&ph#r>c=sr"
    assert candidate("u<~%&g_kwhq!zd&>&u") == "U<~%&gKwhq!zd&>&u"
    assert candidate("n~y#jz_hgg+t>@?jk+") == "N~y#jzHgg+t>@?jk+"
    assert candidate("kfyp#~a!z?sh:?y$") == "Kfyp#~a!z?sh:?y$"
    assert candidate("vtbe_ns#$?x") == "VtbeNs#$?x"
    assert candidate(":y-|sfvebw") == ":y-|sfvebw"
    assert candidate("#voic=o:_->jfc") == "#voic=o:->jfc"
    assert candidate("!b/=^z~q%$ay<hy*ry") == "!b/=^z~q%$ay<hy*ry"
    assert candidate("hx$o$#hrdae~?u-") == "Hx$o$#hrdae~?u-"
    assert candidate("qzfsm_yw!x:i<qewsl") == "QzfsmYw!x:i<qewsl"
    assert candidate("@ulwze-b@p>tnkxnv") == "@ulwze-b@p>tnkxnv"
    assert candidate("k&vhsh=xap%") == "K&vhsh=xap%"
    assert candidate("~anvt=&kafw:?+") == "~anvt=&kafw:?+"
    assert candidate("g:m+o_re_s*_rku#%") == "G:m+oReS*Rku#%"
    assert candidate("i/%n:^yzy") == "I/%n:^yzy"
    assert candidate("i:&|/rp*i*>-") == "I:&|/rp*i*>-"
    assert candidate("@oxe#t&zoi~gj") == "@oxe#t&zoi~gj"
    assert candidate("*r-xmtwm?<@^_") == "*r-xmtwm?<@^_"
    assert candidate("&k/|y-fl*w") == "&k/|y-fl*w"
    assert candidate("<bp%_a/") == "<bp%A/"
    assert candidate("=aei-whn&") == "=aei-whn&"
    assert candidate("m/m_+iqc") == "M/m+iqc"
    assert candidate("=gizti:+sp") == "=gizti:+sp"
    assert candidate("%|v>jz|ksi+u&ns") == "%|v>jz|ksi+u&ns"
    assert candidate("?ugofui>ddn^vbk") == "?ugofui>ddn^vbk"
    assert candidate("a|rdx/^") == "A|rdx/^"
    assert candidate("/ue+c@=&?@/e") == "/ue+c@=&?@/e"
    assert candidate("=zj/bnw|=>^ewoc") == "=zj/bnw|=>^ewoc"
    assert candidate("q<s!n:&:ua") == "Q<s!n:&:ua"
    assert candidate("fsizrftf/d>") == "Fsizrftf/d>"
    assert candidate("kv=aaq") == "Kv=aaq"
    assert candidate("&#izumks~#c-f~") == "&#izumks~#c-f~"
    assert candidate(":^$?!b*k") == ":^$?!b*k"
    assert candidate("a<du-qw-<") == "A<du-qw-<"
    assert candidate("~b?=^hal") == "~b?=^hal"
    assert candidate("bi<?n|z") == "Bi<?n|z"
    assert candidate("i>qp>iu<?|") == "I>qp>iu<?|"
    assert candidate("lgcjksi>my&|bc") == "Lgcjksi>my&|bc"
    assert candidate("#|aj_lz*") == "#|ajLz*"
    assert candidate("^em@oxj") == "^em@oxj"
    assert candidate("~zp$rkrzm&<<") == "~zp$rkrzm&<<"
    assert candidate("|&fnde?e%+?@") == "|&fnde?e%+?@"
    assert candidate("*h<a#wj?%oqm") == "*h<a#wj?%oqm"
    assert candidate("e<%sgpd$") == "E<%sgpd$"
    assert candidate("&x#s?x") == "&x#s?x"
    assert candidate("z~k_#s") == "Z~k#s"
    assert candidate("bd=>!rpy=#x^>u") == "Bd=>!rpy=#x^>u"
    assert candidate("-^&iyhg#%i$g$") == "-^&iyhg#%i$g$"
    assert candidate("|b~>&=zxq$vjbh") == "|b~>&=zxq$vjbh"
    assert candidate("<x*a@&ey^-uf") == "<x*a@&ey^-uf"
    assert candidate("ivtnr?by") == "Ivtnr?by"

if __name__ == '__main__':
    check(snake_to_camel)