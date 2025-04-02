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
  const [N,C]=input[iter++].split(' ').map(item=>Number(item))
  const M=Number(input[iter++])
  const send=[...new Array(N+1)].map(item=>{return {}})
  const receive=[...new Array(N+1)].map(item=>{return{}})
  for(let i=0;i<M;i++){
    const [s,r,t]=input[iter++].split(' ').map(item=>Number(item))
    if (r in send[s]) send[s][r]+=t
    else send[s][r]=t
    if (s in receive[r]) receive[r][s]+=t
    else receive[r][s]=t
  }
  // 가장 짧게 이동하는 택배 선택, 

  function possible(start,end,plus){
    let cnt=plus
    for(let i=start;i<end;i++){
      if (dp[i]+plus>C) cnt=Math.min(cnt,C-dp[i])
    }
    return cnt
  }

  let answer=0
  const dp=[...new Array(N+1)].map(item=>0)
  for(let i=1;i<=N;i++){
    const keys=Object.keys(receive[i]).map(item=>Number(item)).sort((a,b)=>b-a)
    for(let j=0;j<keys.length;j++){
      const plus=possible(keys[j],i,receive[i][keys[j]])
      answer+=plus
      if (plus===0) break
      for(let k=keys[j];k<i;k++){
        dp[k]+=plus
      }
    }
  }

  console.log(answer)
  process.exit()
})
