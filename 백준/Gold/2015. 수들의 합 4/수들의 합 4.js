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
  const [N,K]=input[iter++].split(' ').map(item=>Number(item))
  const A=input[iter++].split(' ').map(item=>Number(item))

  const total=[...new Array(N)].map(item=>0)
  total[0]=A[0]
  for(let i=1;i<N;i++){
    total[i]+=total[i-1]+A[i]
  }

  const info={}
  let answer=0
  for(let i=0;i<N;i++){
    if (total[i]===K) answer+=1
    if (total[i]-K in info) answer+=info[total[i]-K]
    if (total[i] in info) info[total[i]]+=1
    else info[total[i]]=1
  }

  console.log(answer)
  process.exit()
})
