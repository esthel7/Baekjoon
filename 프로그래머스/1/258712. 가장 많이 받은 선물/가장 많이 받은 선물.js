function solution(friends, gifts) {
    var answer = 0;
    var n=friends.length
    
    var change={}
    for(let i=0;i<n;i++){
        change[friends[i]]=i
    }

    var give=[]
    var receive=[]
    var gift=[]
    var nexts=[]
    for(let i=0;i<n;i++){
        gift.push(0)
        nexts.push(0)
        give.push([])
        receive.push([])
        for(let j=0;j<n;j++){
            give[i].push(0)
            receive[i].push(0)
        }
    }

    for(let i=0;i<gifts.length;i++){
        var [a,b]=gifts[i].split(' ')
        a=change[a]
        b=change[b]
        give[a][b]++
        receive[b][a]++
    }
    
    for(let i=0;i<n;i++){
        var totalgive=give[i].reduce((a,b)=>a+b,0)
        var totalreceive=receive[i].reduce((a,b)=>a+b,0)
        gift[i]=totalgive-totalreceive
    }
    
    for(let i=0;i<n;i++){
        for (let j=i+1;j<n;j++){
            if (give[i][j]!=0||receive[i][j]!=0){
                if(give[i][j]>give[j][i]){
                    nexts[i]++
                }
                else if(give[i][j]<give[j][i]){
                    nexts[j]++
                }
                else{
                    if(gift[i]>gift[j]){
                        nexts[i]++
                    }
                    else if (gift[i]<gift[j]){
                        nexts[j]++
                    }
                }
            }
            else {
                if(gift[i]>gift[j]){
                    nexts[i]++
                }
                else if (gift[i]<gift[j]){
                    nexts[j]++
                }
            }
        }
    }
    return Math.max(...nexts);
}