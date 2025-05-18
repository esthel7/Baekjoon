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
  const answer=[]
  while(true){
    const N=Number(input[iter++])
    if (N===0) break
    const dp=[...new Array(N+1)].map(item=>[...new Array(N+1)].map(item=>0))
    dp[N][0]=1
    for(let i=N;i>=0;i--){
      for(let j=N;j>=0;j--){
        if (dp[i][j]===0) continue
        if (i===0){
          if (j===0) continue
          dp[i][j-1]+=dp[i][j]
        } else {
          dp[i-1][j+1]+=dp[i][j]
          if (j===0) continue
          dp[i][j-1]+=dp[i][j]
        }
      }
    }
    answer.push(dp[0][0])
  }

  console.log(answer.join('\n'))
  process.exit()
})
