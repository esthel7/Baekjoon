const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,T]=input[iter++].split(' ').map(item=>Number(item))

  const dp=[...new Array(T+1)].map(item=>0)
  let answer=0
  for(let i=0;i<N;i++){
    const [K,S]=input[iter++].split(' ').map(item=>Number(item))
    for(let j=T-K;j>=0;j--){
      if (dp[j+K]<dp[j]+S) {
        dp[j+K]=dp[j]+S
        answer=Math.max(answer,dp[j+K])
      }
    }
    if (dp[K]<S) {
      dp[K]=S
      answer=Math.max(answer,S)
    }
  }

  console.log(answer)
  process.exit()
})
