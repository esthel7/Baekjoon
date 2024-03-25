function solution(sequence, k) {
    var answer = [];
    n=sequence.length
    total=[]
    total.push(0)
    for (let i=0;i<n;i++){
        total.push(total[i]+sequence[i])
    }
    Min=0
    answerBet=-1
    for (let i=1;i<n+1;i++){
        if (total[i]==k){
            answerBet=i-1
            answer=[0,i-1]
        }
        else if (total[i]>k){
            for (let j=Min;j<i;j++){
                if (total[i]-total[j]>k) continue
                else if (total[i]-total[j]<k){
                    Min=j
                    break
                }
                else{
                    Min=j
                    if (answerBet==-1 || answerBet>i-j-1){
                        answerBet=i-j-1
                        answer=[j,i-1]
                    }
                    break
                }
            }
        }
    }
    return answer;
}