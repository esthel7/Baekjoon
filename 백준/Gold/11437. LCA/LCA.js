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

  const link=[...new Array(N+1)].map(item=>{return {}})
  for(let i=0;i<N-1;i++){
    let [a,b]=input[iter++].split(' ').map(item=>Number(item))
    link[a][b]=true
    link[b][a]=true
  }

  const parent=[...new Array(N+1)].map(item=>[-1,-1])
  parent[1]=[1,0]
  let q=[[1,0]]
  while(q.length>0){
    const [node,depth]=q.shift()
    const keys=Object.keys(link[node]).map(item=>Number(item))
    for(let i=0;i<keys.length;i++){
      if (parent[keys[i]][0]!==-1) continue
      parent[keys[i]]=[node,depth+1]
      q.push([keys[i],depth+1])
    }
  }

  const answer=[]
  const M=Number(input[iter++])
  for(let i=0;i<M;i++){
    const [a,b]=input[iter++].split(' ').map(item=>Number(item))
    if (a===b){
      answer.push(a)
      continue
    }
    let moveA=a
    let moveB=b
    let flag=false
    while (parent[moveA][1]!==parent[moveB][1]){
      if (parent[moveA][0]===b){
        answer.push(b)
        flag=true
        break
      } else if (parent[moveB][0]===a){
        answer.push(a)
        flag=true
        break
      }
      if(parent[moveA][1]>parent[moveB][1]) moveA=parent[moveA][0]
      else moveB=parent[moveB][0]
    }
    if (flag) continue
    while (parent[moveA][0]!==parent[moveB][0]){
      moveA=parent[moveA][0]
      moveB=parent[moveB][0]
    }
    answer.push(parent[moveA][0])
  }

  console.log(answer.join('\n'))
  process.exit()
})
