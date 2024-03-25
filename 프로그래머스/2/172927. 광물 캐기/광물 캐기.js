function solution(picks, minerals) {
    answer = -1;
    // 광물은 순서대로
    // 곡괭이는 못쓸때까지 사용
    function find(idx,now,l){
        if (idx==l.length){
            if (answer==-1 || answer>now){
                answer=now
            }
            return
        }
        for(let i=idx*5;i<idx*5+5;i++){
            if (i==minerals.length){
                if (answer==-1 || answer>now){
                    answer=now
                }
                return
            }
            if (l[idx]==0){ // diamond
                now+=1
            }
            else if (l[idx]==1){ //iron
                if (minerals[i]=='diamond') now+=5
                else now+=1
            }
            else{ // stone
                if (minerals[i]=='diamond')now+=25
                else if(minerals[i]=='iron') now+=5
                else now+=1
            }
        }
        find(idx+1,now,l)
    }
        
    function make(pk,cnt,l,final){
        if (cnt==final) {
            find(0,0,l)
            return
        }
        for (let i=0;i<3;i++){
            if (pk[i]==0) continue
            pk[i]-=1
            l.push(i)
            make(pk,cnt+1,l,final)
            pk[i]+=1
            l.pop()
        }
    }
    
    var l=[]
    var final=picks.reduce((a,b)=>a+b,0)
    make(picks,0,l,final)
    return answer;
}