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
        [q[loc],q[left]]=[q[left],q[loc]]
      }
      break
    }
    const Min=isSmall(q[left],q[right])?left:right
    if (isSmall(q[Min],q[loc])){
      [q[loc],q[Min]]=[q[Min],q[loc]]
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
  const impossible={}
  for(let i=0;i<M;i++){
    const small=Number(input[iter++])
    impossible[small-1]=true
  }

  const l=[...new Array(N)].map(item=>{return{}})
  l[0][0]=0
  for(let i=0;i<N-1;i++){
    const jumps=Object.keys(l[i]).map(item=>Number(item))
    for(let j=0;j<jumps.length;j++){
      const jump=jumps[j]
      const cnt=l[i][jump]
      for(let k=jump-1;k<=jump+1;k++){
        if (k<=0 || i+k>=N || i+k in impossible) continue
        if (k in l[i+k]) l[i+k][k]=Math.min(l[i+k][k],cnt+1)
        else l[i+k][k]=cnt+1
      }
    }
  }

  let answer=-1
  const keys=Object.keys(l[N-1])
  for(let i=0;i<keys.length;i++){
    const now=l[N-1][keys[i]]
    if (answer===-1 || answer>now) answer=now
  }
  console.log(answer)
  process.exit()
})
