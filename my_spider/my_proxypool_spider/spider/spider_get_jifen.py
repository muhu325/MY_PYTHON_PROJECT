import requests,time

def get_honghu():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Referer':'http://bbs.hh010.com/',
        'Origin':'http://bbs.hh010.com',
        'Host':'bbs.hh010.com',
        'Cookie':'_uab_collina=150675231172853768103902; _umdata=E2AE90FA4E0E42DE71256F3DFD9D5AEA7B03E040D78FE0105F1B46FB4DA6307AA312D700DD907785CD43AD3E795C914C59590861D0B54CDD9781492193BD56E2; __cfduid=df0506b8b1731dac717abcd9a79afd8b61525161299; DX27_d09b_connect_uin=8D874AE85199F673A9BC4C023162B46D; DX27_d09b_nofavfid=1; DX27_d09b_smile=1D1; __uid=329409bd4fdf605e6af197f90617f268; DX27_d09b_connect_is_bind=1; UM_distinctid=165a405c8ae1aa-035324e3555dfd-43480420-100200-165a405c8b04fd; Hm_lvt_7d6a48039c8b35e7f43f722eeeee1a90=1536055167; DX27_d09b_saltkey=SPbi1tJz; DX27_d09b_lastvisit=1547553581; DX27_d09b_client_created=1547557188; DX27_d09b_client_token=8D874AE85199F673A9BC4C023162B46D; DX27_d09b_auth=2be9CdugbjELR64hxjAbGKOkL46q%2B2PhgE%2FbtX7ntdpUb6Ex2UHLP%2F05fcwBRLT847Q51YD4WAbs4Wz4ZCrgP4BIc70; DX27_d09b_connect_login=1; DX27_d09b_stats_qc_login=3; DX27_d09b_pc_size_c=0; DX27_d09b_myrepeat_rr=R0; DX27_d09b_visitedfid=243; DX27_d09b_sid=KF9CGz; DX27_d09b_lip=58.101.33.209%2C1547560957; DX27_d09b_ulastactivity=6c2cLjOtOG3y3yt4iLb9TAf4E1vAnESaIwaAA7i02x8yGFVtTHzF; DX27_d09b_sendmail=1; CNZZDATA2516833=cnzz_eid%3D907856298-1492492264-%26ntime%3D1547599641; DX27_d09b_noticeTitle=1; security_session_verify=2845493caefdd9ece7f7e6fb3eae48b7; DX27_d09b_lastact=1547604671%09plugin.php%09',
        'Accept-Language':'zh-CN,zh;q=0.9',
    }
    url = 'http://bbs.hh010.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1'
    data = {
        'formhash':'fe6642ca',
        'qdxq':'fd',
        'qdmode':'3',
        'todaysay':'',
        'fastreply':'0',
    }
    r1 = requests.post(url,headers=headers,data=data)
    print(r1.status_code)
    # print(r1.content)
    print(r1.text)
    print('_______________________________________________________')


def get_vlan5():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Referer':'http://bbs.vlan5.com/thread-18415-1-1.html',
        'Origin':'http://bbs.vlan5.com',
        'Host':'bbs.vlan5.com',
        'Cookie':'_uab_collina=151183981220019558622116; dCVo_efcf_connect_uin=4292CA6AAA7C1E36E83B71D98B7A9A6C; dCVo_efcf_smile=1D1; dCVo_efcf_connect_is_bind=1; _umdata=E2AE90FA4E0E42DE71256F3DFD9D5AEA7B03E040D78FE0105F1B46FB4DA6307AA312D700DD907785CD43AD3E795C914C55F18BD861FC2F17C3C7DCA3CCB8736E; dCVo_efcf_nofavfid=1; __cfduid=d80eae5c9f1f04020e814715647cfbe2b1547557321; dCVo_efcf_saltkey=sH644oNV; dCVo_efcf_lastvisit=1547553710; dCVo_efcf_pc_size_c=0; dCVo_efcf_visitedfid=98; UM_distinctid=168519af271a7-067273250970d2-43480420-100200-168519af2722af; dCVo_efcf_client_created=1547560219; dCVo_efcf_client_token=4292CA6AAA7C1E36E83B71D98B7A9A6C; dCVo_efcf_auth=758amY8yigVF6BfXb7YvoTAAe8RFsNfsR7bzeN3qAeDJjb7JgZbuJWOzrHgzdWpM2hjy5MHuFxBSRWqsbEkMQhZeGw; dCVo_efcf_connect_login=1; dCVo_efcf_stats_qc_login=3; dCVo_efcf_forum_lastvisit=D_98_1547561000; yjs_ab_lid=9952a20d09eee92e0262cd9f663f1b79f1034; yjs_ab_score=700; cf_clearance=3f6529753eea2fbde25a22fc5dcbcf18f5d47452-1547604653-1800-150; 18415=cook; dCVo_efcf_st_p=40154%7C1547604627%7C3bc35f8aaf8b3475c0b475bfbbe016dd; dCVo_efcf_viewid=tid_18415; dCVo_efcf_ulastactivity=1547604627%7C0; CNZZDATA1275600666=1695569103-1547555340-null%7C1547599757; dCVo_efcf_lastact=1547604629%09connect.php%09check; Hm_lvt_dd52e60d98e7952a624dcfce530f23df=1547557336,1547604655; Hm_lpvt_dd52e60d98e7952a624dcfce530f23df=1547604655',
        'Accept-Language':'zh-CN,zh;q=0.9',
    }
    url = 'http://bbs.vlan5.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1'
    data = {
        'formhash':'d8f7e00b',
        'qdxq':'shuai',
        'qdmode':'3',
        'todaysay':'',
        'fastreply':'0',
    }
    r1 = requests.post(url,headers=headers,data=data)
    print(r1.status_code)
    # print(r1.content)
    print(r1.text)
    print('_______________________________________________________')



def get_javaxxz():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Referer':'http://www.javaxxz.com/index.php',
        'Origin':'http://www.javaxxz.com',
        'Host':'www.javaxxz.com',
        'Cookie':'XqT8_f9d1_saltkey=H7i1WImn; XqT8_f9d1_lastvisit=1547557667; UM_distinctid=16851d8d0202b9-0fe5e8de8be8c8-43480420-100200-16851d8d0217c; XqT8_f9d1_forum_lastvisit=D_167_1547561313; XqT8_f9d1_visitedfid=167; XqT8_f9d1_connect_qq_nick=%E5%A4%9C%E9%A2%A8; XqT8_f9d1_connect_js_name=user_bind; XqT8_f9d1_connect_js_params=YToxOntzOjQ6InR5cGUiO3M6ODoicmVnaXN0ZXIiO30%3D; XqT8_f9d1_connect_login=1; XqT8_f9d1_connect_is_bind=1; XqT8_f9d1_connect_uin=CFB762A0253760B4AA9945AD92AC1188; XqT8_f9d1_stats_qc_reg=1; XqT8_f9d1_onlineusernum=88; XqT8_f9d1_sendmail=1; CNZZDATA3164859=cnzz_eid%3D1917451229-1547561309-null%26ntime%3D1547600536; Hm_lvt_ea388b73d458f857ef88daff105994d4=1547561390,1547605647; XqT8_f9d1_con_request_uri=http%3A%2F%2Fwww.javaxxz.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dindex.php; XqT8_f9d1_client_created=1547605533; XqT8_f9d1_client_token=CFB762A0253760B4AA9945AD92AC1188; XqT8_f9d1_ulastactivity=1547605533%7C0; XqT8_f9d1_auth=d17aayyYbxsayY2EZ%2BOrtuGjNeCIM%2F9nr6FoWiY0eRfUNAQthjdNK%2BxLH99neghRbBajKXE%2FVUGZcwPlzNHXo9hM5mY; XqT8_f9d1_stats_qc_login=3; XqT8_f9d1_lastcheckfeed=285636%7C1547605535; XqT8_f9d1_noticeTitle=1; XqT8_f9d1_nofavfid=1; Hm_lpvt_ea388b73d458f857ef88daff105994d4=1547605659; XqT8_f9d1_lastact=1547605561%09plugin.php%09',
        'Accept-Language':'zh-CN,zh;q=0.9',
    }
    url = 'http://www.javaxxz.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1'
    data = {
        'formhash':'bc8a7838',
        'qdxq':'shuai',
        'qdmode':'3',
        'todaysay':'',
        'fastreply':'0',
    }
    r1 = requests.post(url,headers=headers,data=data)
    print(r1.status_code)
    # print(r1.content)
    print(r1.text)
    print('_______________________________________________________')



if __name__ == "__main__":
    get_honghu()
    get_vlan5()
    get_javaxxz()
    time.sleep(5)