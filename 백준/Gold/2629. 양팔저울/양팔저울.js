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
  const w=input[iter++].split(' ').map(item=>Number(item))

  const info={}
  for(let i=0;i<N;i++){
    const keys=Object.keys(info).map(item=>Number(item))
    for(let j=0;j<keys.length;j++){
      info[keys[j]+w[i]]=true
      info[Math.abs(keys[j]-w[i])]=true
    }
    info[w[i]]=true
  }

  const M=Number(input[iter++])
  const l=input[iter++].split(' ').map(item=>Number(item))
  const answer=[]

  for(let i=0;i<M;i++){
    if (l[i] in info) answer.push('Y')
    else answer.push('N')
  }

  console.log(answer.join(' '))
  process.exit()
})
