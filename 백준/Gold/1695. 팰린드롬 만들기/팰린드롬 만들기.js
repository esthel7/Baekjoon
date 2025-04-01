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
  const N=Number(input[iter++])
  const l=input[iter++].split(' ')
  const rl=[...l]
  rl.reverse()

  const dp=[...new Array(2)].map(item=>[...new Array(N)].map(item=>0))
  let Max=0
  for(let i=0;i<N;i++){
    for(let j=0;j<N;j++){
      if (i!==0&&j!==0) dp[1][j]=dp[0][j-1]
      if (l[i]===rl[j]) dp[1][j]+=1
      if (i!==0&&dp[0][j]>dp[1][j]) dp[1][j]=dp[0][j]
      if (j!==0&&dp[1][j-1]>dp[1][j]) dp[1][j]=dp[1][j-1]
      if (Max<dp[1][j]) Max=dp[1][j]
    }
    dp[0]=[...dp[1]]
    dp[1]=[...new Array(N)].map(item=>0)
  }

  console.log(N-Max)
  process.exit()
})
