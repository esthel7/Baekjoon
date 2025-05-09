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
  const [N,L,R,X]=input[iter++].split(' ').map(item=>Number(item))
  const A=input[iter++].split(' ').map(item=>Number(item))
  A.sort((a,b)=>a-b)

  let answer=0
  function calculate(now){
    if (now.length<2) return
    if (now[now.length-1]-now[0]<X) return
    const total=now.reduce((a,b)=>a+b)
    if (L<=total && total<=R) {
      answer+=1
    }
  }
  
  function make(now,start){
    for(let i=start;i<N;i++){
      now.push(A[i])
      calculate(now)
      make(now,i+1)
      now.pop()
    }
  }

  for(let i=0;i<N;i++){
    make([A[i]],i+1)
  }

  console.log(answer)
  process.exit()
})
