const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function isSmall(a,b){
  if (a[1]<b[1]) return true
  return false
}

function heappush(q,item){
  q.push(item)
  let now=q.length-1
  let parent=Math.floor(now/2)
  while(parent>=1){
    if (isSmall(q[now],q[parent])){
      [q[now],q[parent]]=[q[parent],q[now]]
      now=parent
      parent=Math.floor(parent/2)
    } else break
  }
}

function heappop(q){
  const item=[...q[1]]
  q.splice(1,1)
  let now=1
  while(true){
    const left=now*2
    const right=now*2+1
    if (q.length<=left) break
    if (q.length<=right){
      if (isSmall(q[left],q[now])){
        [q[now],q[left]]=[q[left],q[now]]
        now=left
        continue
      }
      break
    }
    const Min=isSmall(q[left],q[right])?left:right
    if (isSmall(q[Min],q[now])){
      [q[now],q[Min]]=[q[Min],q[now]]
      now=Min
      continue
    } else break
  }
  return item
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [V,E]=input[iter++].split(' ').map(Number)
  const K=Number(input[iter++])

  const graph={}

  for(let i=0;i<E;i++){
    const [u,v,w]=input[iter++].split(' ').map(Number)
    if (u in graph){
      if (v in graph[u]){
        if (graph[u][v]>w) graph[u][v]=w
      } else graph[u][v]=w
    } else {
      graph[u]={[v]:w}
    }
  }

  const answer=[...new Array(V+1)].map(item=>'INF')
  answer[K]=0

  const q=[0]
  const arr=Object.keys(graph[K]).map(item=>[item,graph[K][item]])
  for(let i=0;i<arr.length;i++){
    heappush(q,arr[i])
    const [nextnode,cost]=arr[i]
    if (answer[nextnode]==='INF') answer[nextnode]=cost
  }

  while(q.length>1){
    const [node,cost]=heappop(q)
    const nextkeys=node in graph?Object.keys(graph[node]):[]
    for(let i=0;i<nextkeys.length;i++){
      const nextnode=nextkeys[i]
      if (answer[nextnode]==='INF' || answer[nextnode]>cost+graph[node][nextnode]){
        answer[nextnode]=cost+graph[node][nextnode]
        heappush(q,[nextnode,cost+graph[node][nextnode]])
      }
    }
  }

  answer.shift()
  console.log(answer.join('\n'))
  process.exit()
})
