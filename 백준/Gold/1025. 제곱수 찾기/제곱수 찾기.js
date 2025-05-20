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
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split('').map(item=>Number(item)))
  }

  const Max=10**Math.max(N,M)
  const possible={}
  let cnt=0
  while(true){
    possible[cnt*cnt]=true
    if (cnt*cnt/Max>=1) break
    cnt+=1
  }

  let answer=-1

  function calculate(x,y){
    let now=0
    for(let i=0;i<x.length;i++){
      now*=10
      now+=l[x[i]][y[i]]
    }
    // console.log(x,y,now)
    if (now in possible){
      if (answer<now) answer=now
    }
  }

  function make(diffx,diffy){
    for(let i=0;i<N;i++){
      for(let j=0;j<M;j++){
        const x=[i]
        const y=[j]
        let nowx=i+diffx
        let nowy=j+diffy
        while(0<=nowx && nowx<N && 0<=nowy && nowy<M){
          x.push(nowx)
          y.push(nowy)
          calculate(x,y)
          nowx+=diffx
          nowy+=diffy
        }
      }
    }
  }

  for(let i=-N+1;i<N;i++){
    for(let j=-M+1;j<M;j++){
      if (i>=0 && j>=0) calculate([i],[j])
      if (i===0 && j===0) continue
      make(i,j)
    }
  }

  console.log(answer)
  process.exit()
})
