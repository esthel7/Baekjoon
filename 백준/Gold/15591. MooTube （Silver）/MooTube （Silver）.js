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
    const right=loc*2+1
    if (left>=last) break
    if (right>=last){
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
  const [N,Q]=input[iter++].split(' ').map(item=>Number(item))
  const link=[...new Array(N+1)].map(item=>[])
  for(let i=0;i<N-1;i++){
    const [p,q,r]=input[iter++].split(' ').map(item=>Number(item))
    link[p].push([q,r])
    link[q].push([p,r])
  }

  const answer=[]
  for(let i=0;i<Q;i++){
    const [k,v]=input[iter++].split(' ').map(item=>Number(item))
    const visit=[...new Array(N+1)].map(item=>false)
    visit[v]=true
    let cnt=0
    const q=[v]
    while(q.length>0){
      const node=q.shift()
      for(let j=0;j<link[node].length;j++){
        const [nextNode,r]=link[node][j]
        if (r<k|| visit[nextNode]) continue
        visit[nextNode]=true
        cnt+=1
        q.push(nextNode)
      }
    }
    answer.push(cnt)
  }

  console.log(answer.join('\n'))
  process.exit()
})
