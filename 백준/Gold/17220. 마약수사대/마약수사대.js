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

  function match(item){
    return item.charCodeAt()-'A'.charCodeAt()
  }

  const root={}
  for(let i=0;i<N;i++){
    root[i]=true
  }
  const parent=[...new Array(N)].map(item=>{return{}})
  const child=[...new Array(N)].map(item=>{return{}})
  for(let i=0;i<M;i++){
    let [A,B]=input[iter++].split(' ')
    A=match(A)
    B=match(B)
    parent[B][A]=true
    child[A][B]=true
    if (B in root) delete(root[B])
  }

  const l=input[iter++].split(' ')
  for(let i=1;i<l.length;i++){
    const item=match(l[i])
    if (item in root) {
      delete(root[item])
      child[root]={}
      continue
    }
    const parents=Object.keys(parent[item]).map(item=>Number(item))
    for(let j=0;j<parents.length;j++){
      const p=parents[j]
      if (item in child[p]) delete(child[p][item])
    }
  }

  let answer=0
  const visit=[...new Array(N)].map(item=>false)

  function find(item){
    const childs=Object.keys(child[item])
    for(let i=0;i<childs.length;i++){
      const now=childs[i]
      if (visit[now]) continue
      visit[now]=true
      answer+=1
      find(now)
    }
  }

  const rootKeys=Object.keys(root).map(item=>Number(item))
  for(let i=0;i<rootKeys.length;i++){
    find(rootKeys[i])
  }

  console.log(answer)
  process.exit()
})
