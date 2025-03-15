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
  while(loc>0){
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
  const last=q.length-1
  while(loc<last){
    const left=loc*2
    const right=loc*2+1
    if (left>last) break
    else if (right>last){
      if (isSmall(q[left],q[loc])) [q[left],q[loc]]=[q[loc],q[left]]
      break
    } else {
      const Min=isSmall(q[left],q[right])?left:right
      if (isSmall(q[Min],q[loc])) {
        [q[Min],q[loc]]=[q[loc],q[Min]]
        loc=Min
      } else break
    }
  }
  return value
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,A,B]=input[iter++].split(' ').map(item=>Number(item))
  const link=[...new Array(N+1)].map(item=>{return {}})
  const keys=[...new Array(N+1)].map(item=>[])
  for(let i=0;i<N-1;i++){
    const [s,e,c]=input[iter++].split(' ').map(item=>Number(item))
    link[s][e]=c
    link[e][s]=c
    keys[s].push(e)
    keys[e].push(s)
  }

  const visit=[...new Array(N+1)].map(item=>-1)
  visit[A]=0

  const q=[0,[0,0,0,A]]
  while(q.length>1){
    let [c,total,Max,s]=heappop(q)
    if (s===B){
      console.log(c)
      process.exit()
    }
    for(let i=0;i<keys[s].length;i++){
      const node=keys[s][i]
      if (visit[node]!==-1 && visit[node]<total+link[s][node]) continue
      visit[node]=total+link[s][node]
      let newMax=Max<link[s][node]?link[s][node]:Max
      heappush(q,[total+link[s][node]-newMax,total+link[s][node],newMax,node])
    }
  }

  process.exit()
})
