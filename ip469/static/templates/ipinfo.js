// -*-coding:utf-8-*-

function check_and_go()
{
    ip_box = document.getElementById('query_box_ip');
    ip = ip_box.value;

    // 正确性检查
    format_is_ok  = false;
    error_message = '';

    if (ip.indexOf(" ")>=0) {
        ip = ip.replace(/ /g,"");
        ip_box.value = ip;
    }
    if (ip.toLowerCase().indexOf("http://")==0) {
        ip = ip.slice(7);
        ip_box.value = ip;
    }

    if(ip == '') {
        format_is_ok  = false;
        error_message = '请输入IP地址后再点击查询按钮';
    } else {
        if(/[A-Za-z_-]/.test(ip)) {
            if(!/^([\w-]+\.)+((com)|(net)|(org)|(gov\.cn)|(info)|(cc)|(com\.cn)|(net\.cn)|(org\.cn)|(name)|(biz)|(tv)|(cn)|(mobi)|(name)|(sh)|(ac)|(io)|(tw)|(com\.tw)|(hk)|(com\.hk)|(ws)|(travel)|(us)|(tm)|(la)|(me\.uk)|(org\.uk)|(ltd\.uk)|(plc\.uk)|(in)|(eu)|(it)|(jp)|(co)|(me)|(mx)|(ca)|(ag)|(com\.co)|(net\.co)|(nom\.co)|(com\.ag)|(net\.ag)|(fr)|(org\.ag)|(am)|(asia)|(at)|(be)|(bz)|(com\.bz)|(net\.bz)|(net\.br)|(com\.br)|(de)|(es)|(com\.es)|(nom\.es)|(org\.es)|(fm)|(gs)|(co\.in)|(firm\.in)|(gen\.in)|(ind\.in)|(net\.in)|(org\.in)|(jobs)|(ms)|(com\.mx)|(nl)|(nu)|(co\.nz)|(net\.nz)|(org\.nz)|(tc)|(tk)|(org\.tw)|(idv\.tw)|(co\.uk)|(vg)|(ad)|(ae)|(af)|(ai)|(al)|(an)|(ao)|(aq)|(ar)|(as)|(au)|(aw)|(az)|(ba)|(bb)|(bd)|(bf)|(bg)|(bh)|(bi)|(bj)|(bm)|(bn)|(bo)|(br)|(bs)|(bt)|(bv)|(bw)|(by)|(cd)|(cf)|(cg)|(ch)|(ci)|(ck)|(cl)|(cm)|(cr)|(cu)|(cv)|(cx)|(cy)|(cz)|(dj)|(dk)|(dm)|(do)|(dz)|(ec)|(ee)|(eg)|(er)|(et)|(fi)|(fj)|(fk)|(fo)|(ga)|(gd)|(ge)|(gf)|(gg)|(gh)|(gi)|(gl)|(gm)|(gn)|(gp)|(gq)|(gr)|(gt)|(gu)|(gw)|(gy)|(hm)|(hn)|(hr)|(ht)|(hu)|(id)|(ie)|(il)|(im)|(iq)|(ir)|(is)|(je)|(jm)|(jo)|(ke)|(kg)|(kh)|(ki)|(km)|(kn)|(kr)|(kw)|(ky)|(kz)|(lb)|(lc)|(li)|(lk)|(lr)|(ls)|(lt)|(lu)|(lv)|(ly)|(ma)|(mc)|(md)|(mg)|(mh)|(mk)|(ml)|(mm)|(mn)|(mo)|(mp)|(mq)|(mr)|(mt)|(mu)|(mv)|(mw)|(my)|(mz)|(na)|(nc)|(ne)|(nf)|(ng)|(ni)|(no)|(np)|(nr)|(nz)|(om)|(pa)|(pe)|(pf)|(pg)|(ph)|(pk)|(pl)|(pm)|(pn)|(pr)|(ps)|(pt)|(pw)|(py)|(qa)|(re)|(ro)|(ru)|(rw)|(sa)|(sb)|(sc)|(sd)|(se)|(sg)|(si)|(sk)|(sl)|(sm)|(sn)|(sr)|(st)|(sv)|(sy)|(sz)|(td)|(tf)|(tg)|(th)|(tj)|(tl)|(tn)|(to)|(tr)|(tt)|(tz)|(ua)|(ug)|(uk)|(uy)|(uz)|(va)|(vc)|(ve)|(vi)|(vn)|(vu)|(wf)|(ye)|(yt)|(yu)|(za)|(zm)|(zw))$/.test(ip)) {
                format_is_ok = false;
                error_message = '输入的域名不正确';
            } else {
                format_is_ok = true;
            }
        } else if(/^[0-9]+$/.test(ip)) { // 全为数字，合法
            format_is_ok  = true;
            error_message = '';
        } else if(/^[0-9.]+$/.test(ip)) { // 点分十进制，解析各段
            ip_array      = ip.split(".");
            format_is_ok  = (
                (ip_array.length == 4)                                                        &&
                    ((ip_array[0].length != 0) && (ip_array[0] >= 0) && (ip_array[0] <= 255)) &&
                    ((ip_array[1].length != 0) && (ip_array[1] >= 0) && (ip_array[1] <= 255)) &&
                    ((ip_array[2].length != 0) && (ip_array[2] >= 0) && (ip_array[2] <= 255)) &&
                    ((ip_array[3].length != 0) && (ip_array[3] >= 0) && (ip_array[3] <= 255))
            );
            error_message = '请输入正确的IP地址';
        } else {
            format_is_ok = false;
            error_message = '请输入正确的IP地址';
        }
    }

    error_msg = document.getElementById('query_box_error_msg');
    if(format_is_ok) {
        error_msg.style.display = 'none';
        error_msg.innerHTML = '';
        document.location='/ip/' + ip;
    } else {
        error_msg.style.display = '';
        error_msg.innerHTML = error_message;
        ip_box.focus();
        ip_box.select();
    }
    return false;
}

// 页面加载后，聚焦到输入框。
ip_box = document.getElementById('query_box_ip').focus();
