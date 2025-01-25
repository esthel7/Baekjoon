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
  const graph={}
  for (let i=0;i<M;i++){
    const [A,B]=input[iter++].split(' ')
    if (B in graph) graph[B][A]=true
    else graph[B]={[A]:true}
  }
  const visited=[...new Array(N+1)].map(item=>false)
  const X=input[iter++]
  if (!(X in graph)){
    console.log(0)
    process.exit()
  }
  let answer=-1
  function find(node){
    if (visited[Number(node)]) return
    answer+=1
    visited[Number(node)]=true
    if (!(node in graph)) return
    const l=Object.keys(graph[node])
    for (let i=0;i<l.length;i++){
      find(l[i])
    }
  }
  find(X)

  console.log(answer)
  process.exit()
})
