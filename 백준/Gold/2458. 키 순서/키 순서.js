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
  const taller=[...new Array(N+1)].map(item=>[])
  const smaller=[...new Array(N+1)].map(item=>[])
  for(let i=0;i<M;i++){
    const [a,b]=input[iter++].split(' ').map(item=>Number(item))
    taller[a].push(b)
    smaller[b].push(a)
  }

  let answer=0

  function find(idx){
    let s=0
    const visit=[...new Array(N+1)].map(item=>false)
    visit[idx]=true
    const sq=[idx]
    while(sq.length){
      const now=sq.pop()
      for(let i=0;i<smaller[now].length;i++){
        const node=smaller[now][i]
        if (!visit[node]){
          visit[node]=true
          sq.push(node)
          s+=1
        }
      }
    }

    let t=0
    const tq=[idx]
    while(tq.length){
      const now=tq.pop()
      for(let i=0;i<taller[now].length;i++){
        const node=taller[now][i]
        if (!visit[node]){
          visit[node]=true
          tq.push(node)
          t+=1
        }
      }
    }

    if (s+t===N-1) answer+=1
  }

  for(let i=1;i<=N;i++){
    find(i)
  }
  console.log(answer)
  process.exit()
})
