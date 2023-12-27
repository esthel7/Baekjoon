def check(prevsac, sac, ac):
    if prevsac<sac:
        if prevsac<ac and ac<=sac:
            return True
        return False
    else:
        if prevsac==354 and sac==0:
            if ac==0:
                return True
            elif ac>prevsac and ac<360:
                return True
            else:
                return False
        else:
            return False

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    sac=s1*6 # 초각도
    mac=m1*6 + s1*0.1 # 분각도
    hac=(h1%12)*30 + m1*0.5 + s1*(1/120) # 시각도
    prevsac=s1*6
    mflag=False
    hflag=False
    
    while True:
        if s1==60:
            m1+=1
            s1=0
        if m1==60:
            h1+=1
            m1=0
        
        # 각도 계산
        sac=s1*6
        mac=m1*6 + s1*0.1
        hac=(h1%12)*30 + m1*0.5 + s1*(1/120)
        
        if prevsac==sac:
            if sac==mac:
                mflag=True
                answer=1
            if sac==hac:
                hflag=True
                answer=1
        else:
            if check(prevsac, sac, mac):
                if mflag:
                    mflag=False
                else:
                    # if h2!=23:
                    #     print('M',h1,m1,s1,mflag)
                    #     print(prevsac,sac,mac,hac)
                    mflag=True
                    answer+=1
            else:
                mflag=False

            if check(prevsac, sac, hac):
                if hflag:
                    hflag=False
                else:
                    hflag=True
                    if hac!=mac:
                        # if h2!=23:
                        #     print('H',h1,m1,s1,hflag)
                        #     print(prevsac,sac,mac,hac)
                        answer+=1
            else:
                hflag=False
        
            if h1==h2 and m1==m2 and s1==s2:
                break

        prevsac=sac
        s1+=1
        
    return answer