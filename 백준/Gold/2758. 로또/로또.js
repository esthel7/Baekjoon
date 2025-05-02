const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

// 로또 

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const T=Number(input[iter++])
  const answer=[]
  const last=2001
  // const last=11
  const dp=[...new Array(11)].map(item=>[...new Array(last)].map(item=>0))
  for(let i=1;i<last;i++){
    for(let j=1;j<=10;j++){
      if (j===1) dp[j][i]+=1
      if (j+1<=10 && dp[j][i]>0) {
        for(let k=i*2;k<last;k++){
          dp[j+1][k]+=dp[j][i]
        }
      }
      dp[j][i]+=dp[j][i-1]
    }
  }

  // console.log(dp)

  for(let _=0;_<T;_++){
    const [n,m]=input[iter++].split(' ').map(item=>Number(item))
    answer.push(dp[n][m])
  }
  console.log(answer.join('\n'))
  process.exit()
})
