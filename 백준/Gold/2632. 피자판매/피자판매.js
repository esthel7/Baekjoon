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
  const h=Number(input[iter++])
  const [m,n]=input[iter++].split(' ').map(item=>Number(item))
  let A=[]
  for(let i=0;i<m;i++){
    A.push(Number(input[iter++]))
  }
  A=[...A,...A]
  let B=[]
  for(let i=0;i<n;i++){
    B.push(Number(input[iter++]))
  }
  B=[...B,...B]

  const infoA={}
  let totalA=0
  for(let i=0;i<m;i++){
    let now=0
    for(let j=i;j<i+m;j++){
      now+=A[j]
      if (j===i+m-1) totalA=now
      if (now in infoA) infoA[now]+=1
      else infoA[now]=1
    }
  }
  infoA[totalA]=1

  const infoB={}
  let totalB=0
  for(let i=0;i<n;i++){
    let now=0
    for(let j=i;j<i+n;j++){
      now+=B[j]
      if (j===i+n-1) totalB=now
      if (now in infoB) infoB[now]+=1
      else infoB[now]=1
    }
  }
  infoB[totalB]=1

  let answer=0
  const keys=Object.keys(infoA)
  for(let i=0;i<keys.length;i++){
    const left=h-Number(keys[i])
    if (left<0) continue
    else if (left===0) {
      answer+=infoA[keys[i]]
      continue
    }
    else if (!(left in infoB)) continue
    answer+=infoA[keys[i]]*infoB[left]
  }
  if (h in infoB) answer+=infoB[h]

  console.log(answer)
  process.exit()
})
