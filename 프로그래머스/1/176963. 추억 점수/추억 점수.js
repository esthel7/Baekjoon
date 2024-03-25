function solution(name, yearning, photo) {
    var answer = [];
    var info={}
    for(let i=0;i<name.length;i++){
        info[name[i]]=yearning[i]
    }
    for(let i=0;i<photo.length;i++){
        now=0
        for(let j=0;j<photo[i].length;j++){
            if (photo[i][j] in info){
                now+=info[photo[i][j]]
            }
        }
        answer.push(now)
    }
    return answer;
}