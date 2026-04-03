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
  const parent=Math.floor(now/2)
  while(parent>=1){
    if (isSmall(q[now],q[parent])){
      [q[now],q[parent]]=[q[parent],q[now]]
      now=parent
    } else break
  }
}

function heappop(q){
  const item=q[1]
  q.splice(1,1)
  let now=1
  while(true){
    const left=now*2
    const right=now*2+1
    if (q.length<=left) break
    if (q.length<=right){
      if (isSmall(q[left],q[now])){
        [q[left],q[now]]=[q[now],q[left]]
        now=left
        continue
      } else break
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
  const N=Number(input[iter++])
  const M=Number(input[iter++])

  const graph={}

  for(let i=3;i<=M+2;i++){
    const [start,end,cost]=input[iter++].split(' ').map(Number)
    if (start in graph){
      if (end in graph[start]){
        if (graph[start][end]>cost) graph[start][end]=cost
      } else {
        graph[start][end]=cost
      }
    } else {
      graph[start]={}
      graph[start][end]=cost
    }
  }

  const [start,end]=input[iter++].split(' ').map(Number)
  if (start===end){
    console.log(0)
    process.exit()
  }
  const answer=[...new Array(N+1)].map(item=>'INF')
  answer[start]=0

  const arr=Object.keys(graph[start]).map(item=>[item,graph[start][item]])
  const q=[0]
  for(let i=0;i<arr.length;i++){
    heappush(q,arr[i])
    const [node,cost]=arr[i]
    answer[node]=cost
  }

  while(q.length>1){
    const [node,cost]=heappop(q)
    const arr=node in graph?Object.keys(graph[node]).map(item=>[item,cost+graph[node][item]]):[]
    for(let i=0;i<arr.length;i++){
      const [nextnode,nextcost]=arr[i]
      if (answer[nextnode]==='INF' || answer[nextnode]>nextcost){
        answer[nextnode]=nextcost
        heappush(q,arr[i])
      }
    }
  }

  console.log(answer[end])
  process.exit()
})
