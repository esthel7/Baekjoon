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
  const [N,M,K]=input[iter++].split(' ').map(item=>Number(item))
  const graph=[...new Array(N+1)].map(item=>{return {}})
  for(let i=0;i<K;i++){
    const [a,b,c]=input[iter++].split(' ').map(item=>Number(item))
    if (a>b) continue
    if (b in graph[a]) graph[a][b]=Math.max(graph[a][b],c)
    else graph[a][b]=c
  }

  const keys=[...new Array(N+1)]
  for(let i=0;i<=N;i++){
    keys[i]=Object.keys(graph[i]).map(item=>Number(item))
  }

  let answer=0
  const visit=[...new Array(M+1)].map(item=>[...new Array(N+1)].map(item=>0))
  const q=[]
  for(let i=0;i<keys[1].length;i++){
    visit[1][keys[1][i]]=graph[1][keys[1][i]]
    q.push([1,keys[1][i],graph[1][keys[1][i]]])
  }

  while(q.length>0){
    const [cnt,node,cost]=q.shift()
    if (visit[cnt][node]!==cost) continue
    if (node===N){
      answer=Math.max(answer,cost)
      continue
    }
    if (cnt===M-1) continue
    for(let i=0;i<keys[node].length;i++){
      const nextNode=keys[node][i]
      const nextCost=graph[node][nextNode]
      if (visit[cnt+1][nextNode]<cost+nextCost){
        visit[cnt+1][nextNode]=cost+nextCost
        q.push([cnt+1,nextNode,cost+nextCost])
      }
    }
  }

  console.log(answer)
  process.exit()
})
