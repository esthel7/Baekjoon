const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function isSmall(a,b){
  if (a[0]<b[0]) return true
  return false
}

function heappush(q,item){
  q.push(item)
  let loc=q.length-1
  while(loc>1){
    const parent=Math.floor(loc/2)
    if (isSmall(q[loc],q[parent])){
      [q[loc],q[parent]]=[q[parent],q[loc]]
      loc=parent
    } else break
  }
}

function heappop(q){
  const value=q[1]
  if (q.length===2){
    q.pop()
    return value
  }
  q.splice(1,1,q.pop())
  let loc=1
  const last=q.length
  while(loc<last){
    const left=loc*2
    const right=left+1
    if (left>=last) break
    else if (right>=last){
      if (isSmall(q[left],q[loc])){
        [q[left],q[loc]]=[q[loc],q[left]]
      }
      break
    }
    const Min=isSmall(q[left],q[right])?left:right
    if (isSmall(q[Min],q[loc])){
      [q[Min],q[loc]]=[q[loc],q[Min]]
      loc=Min
    } else break
  }
  return value
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))
  const l=input[iter++].split(' ')

  const q=[]
  for(let i=0;i<M;i++){
    let [u,v,d]=input[iter++].split(' ').map(item=>Number(item))
    u-=1
    v-=1
    if (l[u]===l[v]) continue
    q.push([d,u,v])
  }
  q.sort((a,b)=>a[0]-b[0])

  const root=[...new Array(N)].map(item=>-1)
  let answer=0
  for(let i=0;i<q.length;i++){
    const [d,u,v]=q[i]
    if (root[u]===root[v] && root[u]!==-1) continue
    answer+=d
    if (root[u]===-1){
      if (root[v]===-1){
        const Min=Math.min(u,v)
        root[u]=Min
        root[v]=Min
      } else {
        root[u]=root[v]
      }
    } else {
      if (root[v]===-1){
        root[v]=root[u]
      } else {
        const Min=Math.min(root[u],root[v])
        const Max=Math.max(root[u],root[v])
        for(let j=0;j<N;j++){
          if (root[j]===Max) root[j]=Min
        }
      }
    }
  }

  const first=root[0]
  if (first===-1) {
    console.log(-1)
    process.exit()
  }

  for(let i=1;i<N;i++){
    if (root[i]!==first){
      console.log(-1)
      process.exit()
    }
  }
  console.log(answer)
  process.exit()
})
