from case_MBPP_228 import find_adverb_position


def check(candidate):
    assert candidate("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert candidate("seriously!! there are many roses")==(0, 9, 'seriously')
    assert candidate("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')
    assert candidate(":>z^sp-sr-@ea_=&c+l!g?ef#hx=!p|") == None
    assert candidate("xuo=!|>$b*nf%m~^@@bcb~ha/g>$f!%?") == None
    assert candidate("qe!hly_^syucrnddll@lnx:k") == (3, 6, 'hly')
    assert candidate("-s^ xhf%--q!_~h/-llm:| byv_d!y^jm") == None
    assert candidate("ue<%%gpu>|=ff|:~ax*db/+#wu?+") == None
    assert candidate("~k=|eu %%cv=+p&jjw*#ml%~j>gou=rzt") == None
    assert candidate(" uon-vyphvv|=bm#i?cftv@jg#%u?") == None
    assert candidate("x/:vz?-:oovl>&go w y%<ek#y?xk") == None
    assert candidate("fd#g+f-^cy+%~h!bc/gbkc:ii>f") == None
    assert candidate("isx%$t+jvzezikh^cz yj*!r&iq@:#g") == None
    assert candidate("gcw%n=*v/ntewjjq+=fx#nd=@#$=fsa") == None
    assert candidate("m^ @?dpo##%=q=c=ce!/zpiqslx$<&y$q") == None
    assert candidate("pl_demzcgnyi@#n!ta<exqtzd yq") == None
    assert candidate("n/%lo#s~lxt->o<*^h+?teozp%*cp!y% ") == None
    assert candidate("ye>_scozi>&ag&?wmwq!_>&l|x^l$s!!b") == None
    assert candidate("=trr*b$dv^$?gzahf_wm?k/birp&c>*^h") == None
    assert candidate("!/at^saes% =^d|i<@j~xb+|ud s") == None
    assert candidate("d:z--_pkvyk!++iab!|>ck|+acy%") == None
    assert candidate("zh/iob>m!:<a~dq&fh#%dm/:>jj=#<=k") == None
    assert candidate("p?m@/-gl <v$uw$b%ubmh+%l@") == None
    assert candidate("f??rpqh&<pre_f!ux#q>n?^z") == None
    assert candidate("!|r&np^ s#x?$odp_/|poppd%:v|!m u") == None
    assert candidate("!*o:  h f!bd$>ja</e~_pi!pv>o") == None
    assert candidate("~_u@c^>~xb/z-a^:w@kuw:end") == None
    assert candidate(">fgx&!>s!wz-$+rd~|q@:?s+/og*") == None
    assert candidate("i/?/v@j^_y@sjk>gk%%hktlx?:z-") == None
    assert candidate("@ylkbhr?>g#ngb+b*%k|j!xt") == None
    assert candidate("admfr<mizaw@j$f/j>o>a*bzu-x<") == None
    assert candidate("mrmt|nl *mscv/d%%j%qp&cyx<#*og") == None
    assert candidate("svy>y_s|%?e_p:th_h=zrach~:u") == None
    assert candidate("+?xr:ok$vtnv=uovx> +y<>of !mj%-<") == None
    assert candidate("s=gg*=$o$?-yqo*yvue*+ *i#%ke+b") == None
    assert candidate("~y:%m#^zuix>cj!_wu#w&?zfs") == None
    assert candidate("?|km*kdx@rryo<?pq-#co#q+vohuqc::") == None
    assert candidate("e:?<!_?% cpbb*i#wk_w~id^%^?/") == None
    assert candidate("|en_/^hgz @fs/tw<@ l$ jr:v^fj-*") == None
    assert candidate("j$ *@zgxymzw~v!j_<:@|gngtb$gzc$y") == None
    assert candidate("!t?mjq|cbxr/m&nd$oyqt+<s:>p") == None
    assert candidate("si+u/>w:s-hhub #@rvo&e|-gm=!:^") == None
    assert candidate("cx| qy~$mgko   =<+!xk^| --$fxngdd_ix") == None
    assert candidate("*=m_<_blk-|~%?%%b*jqp:ee|g$!w:hv ") == None
    assert candidate("nz_bab<>|=/jqi&|meuhrm+*t|k_#ivjz~o") == None
    assert candidate("f/:ndgy+bhbaqoc$#wds_&bxfl>%@cxskzr") == None
    assert candidate("jg*l-=%fow?psc@z>orlgl |%c>tihuw_-#!") == None
    assert candidate("y!beb_e%ta<rml**@:y>bmfn<&!") == None
    assert candidate("wcqqlwmrav&bu!eqay!%:<wrra=tj|t") == None
    assert candidate("~xpnkiu!lm^yg?nx!krmdw*+~r/#dba|#lu") == None
    assert candidate("|$gqmt-<i&!czu^:tzal|^k:yor?|w") == None
    assert candidate("<<kt@e_kx~o|+aq<tcq/|ku|kzyvgw=~-/s") == None
    assert candidate("i>?d#>ezpahup$*u%-~!qx/r*g<qrc#|&re") == None
    assert candidate("~=wxxg?_^f<qwzy<j#<p$p%sk$l /&!/") == None
    assert candidate("|/w_@%kn?~ev^ :$@usois~*+ll|-gxc_s# ") == None
    assert candidate("sz?odi%w:$^  uaugr=lqsl<t%l_") == None
    assert candidate(" :bf|cy-gnh|l-*-&:bta&r-e| >e#%mpa") == None
    assert candidate("$?ud$npym#df-nk+w*bjm#@fh<a|^wxsarv") == None
    assert candidate("-ivfmy+>d&rzui=:n_&~-hj+-g?+ep") == None
    assert candidate("o=zws !wyf%_o:jhf=du>ru%@~w") == None
    assert candidate("<gdi$#i^~ wdb*~+##thdu> _w:xbxx%%") == None
    assert candidate("gn ucnlp%d|k?#ikk& *czny%b&-zd/opt&") == None
    assert candidate("ew~gk=&$%gi ^i|&e >evbgaz?qf#c") == None
    assert candidate("&z%/!_<q?aj^a#a<byf|:u=a?&n?x-nafb-?") == None
    assert candidate("*?|cjk$ahq+rdcm/b? ^cs*%!dk>trq%") == None
    assert candidate("=tid>#_*u>aw!?mh*acdqig&drvkgq/&") == None
    assert candidate("t*&?>qyf:_cam?#j|$eant%a@izt") == None
    assert candidate("n*d_-xkrt@%^crmi%l!o+_f*coc<") == None
    assert candidate("-hy/+|w-|/ ^axvh+=q:@>=f-bwdooc+tln ") == None
    assert candidate("==ffu>:$*%=-iob|<t#<vp=cr+mehp<ar:r$sia") == None
    assert candidate("_!h$sc>-d!^i!:?%d%:oz!lhh?_pr*t ^k#qqris") == None
    assert candidate("/:=h_xf:un+w?mgo//x>%*b%ql~*^n*cz* :j") == None
    assert candidate("uh/#off&/zgz_|!*=@=fay|s*_x##axc~$rfz|?%<_") == None
    assert candidate("v-ia@|uco/$~u?wp+<|!*wnrhgw~qien_-u") == None
    assert candidate("s*>f~te/jv ddda*t_!w~<n?co@yo*>i$*z^ s:!ew") == None
    assert candidate(":nvu=s&~wwc|^aay<~y= ~avr%utkzaq=g ~_y<") == None
    assert candidate("e%%m&ft?/llpk@aci>jy@u_*=b^gf+xbjq>=") == None
    assert candidate("-=u#=s=inll!=%%gpt#dv*+vm@c?ex?#bq:&>yma") == None
    assert candidate("$#_x|e#+nj|&ga-jyj>$_>-  yd?tn~w&_|i/hw") == None
    assert candidate("oymn/_ %kj&eky%<gj? @x~oe#k~h_#i@$#hkaj") == None
    assert candidate("zd>db^/sx#niuulk~ev$k/jqvvl:+qwu#") == None
    assert candidate("gu=vaez/*#xq#rcxjq!~dy+ln!&$<iuy=/@| ") == None
    assert candidate("k_|@&t-@:jm_p<_q-iksc-ivyt?$-w-_x") == None
    assert candidate("v $npen*i_t h@wrwj?yt~:rc%!:jhxk^") == None
    assert candidate("li-i%*c =hq$vy>-ll|%i>wvhy+r+&bk!<") == None
    assert candidate("-/y_- kxmxsgr-q#bqyi<v$wmta:qaxtkww/ai-") == None
    assert candidate("&xs|^:pa|o/!hi~uw=&pk%?^~v^itw/glew<") == None
    assert candidate("deudv_-pg^b->=hg/~nl?hnke!^o%ncsd% hrs!w") == None
    assert candidate("b$sfdxe:+>yn!:#ww*@y~u-!w$|:-fz-*v") == None
    assert candidate("^*xm->rsqefa#_<+c$dpd<+ba-a#iv|hg") == None
    assert candidate("^^*: ~e*a#q+ysq_f+i/#dty|av|-ltxk!") == None
    assert candidate(">+m|gpbv+b-v:b*</yr gsb|_ppg/jn/ce-") == None
    assert candidate("xs# apt|$_!?wlpad$>~!_ozbr%z?x!iybohx>>+$") == None
    assert candidate("@= v?g|j>cq %o/k#ct~iofj/>$x/j<hw_/=fizya&") == None
    assert candidate("kocr#/s&+#z~o&g>!tos%$wrz#=ln:@rz%") == None
    assert candidate("zt l@ycwyn|<x>bj|hgr<&<b~jzpb?isd~s") == None
    assert candidate("@+tswaulqpvnpku<e<jmof _*bvh+<#e|arcbm!") == None
    assert candidate("de*eih_tfgx:pf!_zwo&mc/n>hkdf<jlvl") == None
    assert candidate("*nifrjlg=o_bz~?x<wq>h_^x+mc_aci|o^$/|c/_y~") == None
    assert candidate("i?>@|?s~v$y- kc/r^e-e_d-!v$@$c?fi") == None
    assert candidate("j*o:g+p=*=av:^o&<@-av&$tkw/mza!iv|sw_f_:$g") == None
    assert candidate("#-@%!wq&w&!h!ta@vo~fkr?<=hz/#c+f#uvnd#d") == None

if __name__ == '__main__':
    check(find_adverb_position)