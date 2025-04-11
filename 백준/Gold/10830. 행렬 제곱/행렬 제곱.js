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
  const [N,B]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  let answer=[]
  for(let i=0;i<N;i++){
    const now=input[iter++].split(' ').map(item=>Number(item))
    for(let j=0;j<N;j++){
      if (now[j]>=1000) now[j]%=1000
    }
    l.push(now)
    answer.push(now)
  }

  let left=B
  let num=1
  let idx=1
  let Max=1
  const info={}
  while(left!==0){
    if (left<0) break
    if (num*2<=left){
      num*=2
      idx+=1
    } else {
      Max=Math.max(Max,idx)
      info[idx]=true
      left-=num
      if (left===1){
        Max=Math.max(Max,1)
        info[1]=true
        break
      }
      num=1
      idx=1
    }
  }

  function calculate(f,s){
    const u=[...new Array(N)].map(item=>[...new Array(N)])
    for(let i=0;i<N;i++){
      for(let j=0;j<N;j++){
        let now=0
        for(let k=0;k<N;k++){
          now+=f[i][k]*s[k][j]
        }
        u[i][j]=now%1000
      }
    }
    return u
  }

  for(let i=1;i<=Max;i++){
    if (i in info){
      const copy=[]
      for(let j=0;j<N;j++){
        copy.push([...answer[j]])
      }
      info[i]=copy
      if (i===Max) break
    }
    answer=calculate(answer,answer)
  }

  const keys=Object.keys(info).sort((a,b)=>a-b)
  answer=info[keys[0]]
  for(let i=1;i<keys.length;i++){
    answer=calculate(answer,info[keys[i]])
  }

  const last=[]
  for(let i=0;i<N;i++){
    last.push(answer[i].join(' '))
  }
  console.log(last.join('\n'))
  process.exit()
})
