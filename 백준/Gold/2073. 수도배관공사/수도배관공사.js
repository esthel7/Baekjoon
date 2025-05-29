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
  const [D,P]=input[iter++].split(' ').map(item=>Number(item))
  const dp=[...new Array(D+1)].map(item=>0)
  for(let i=0;i<P;i++){
    const [L,C]=input[iter++].split(' ').map(item=>Number(item))
    for(let j=D-L;j>=0;j--){
      if (dp[j]===0) continue
      dp[j+L]=Math.max(dp[j+L],Math.min(dp[j],C))
    }
    if (dp[L]<C) dp[L]=C
  }
  console.log(dp[D])
  process.exit()
})
