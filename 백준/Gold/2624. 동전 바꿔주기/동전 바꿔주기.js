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
  const T=Number(input[iter++])
  const K=Number(input[iter++])
  const dp=[...new Array(T+1)].map(item=>0)
  for(let i=0;i<K;i++){
    const [p,n]=input[iter++].split(' ').map(item=>Number(item))
    for(let j=T-1;j>0;j--){
      if (dp[j]>0){
        for(let k=1;k<=n;k++){
          if (j+p*k>T) break
          dp[j+p*k]+=dp[j]
        }
      }
    }
    for(let j=1;j<=n;j++){
      if (p*j>T) break
      dp[p*j]+=1
    }
  }

  console.log(dp[T])
  process.exit()
})
