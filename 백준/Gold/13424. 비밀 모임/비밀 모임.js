const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function isSmall(a,b){
  if (a[0]<b[0]) return true
  return false
}

function heeappush(q,item){
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
  const last=q.length-1
  while(loc<last){
    const left=loc*2
    const right=loc*2+1
    if (left>=last) break
    else if (right>=last){
      if (isSmall(q[left],q[loc])){
        [q[left],q[loc]]=[q[loc],q[left]]
      }
      break
    } else {
      const Min=isSmall(q[left],q[right])?left:right
      if (isSmall(q[Min],q[loc])){
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
  const T=Number(input[iter++])
  const answer=[]

  for(let _=0;_<T;_++){
    const [N,M]=input[iter++].split(' ').map(item=>Number(item))
    const graph=[...new Array(N+1)].map(item=>[])
    for(let i=0;i<M;i++){
      const [a,b,c]=input[iter++].split(' ').map(item=>Number(item))
      graph[a].push([b,c])
      graph[b].push([a,c])
    }

    const K=Number(input[iter++])
    const locs=input[iter++].split(' ').map(item=>Number(item))
    const loc={}
    for(let i=0;i<locs.length;i++){
      loc[locs[i]]=true
    }

    function find(start){
      const visit=[...new Array(N+1)].map(item=>-1)
      visit[start]=0
      const q=[0,[0,start]]
      while(q.length>1){
        const [cost,node]=heappop(q)
        if (visit[node]!==cost) continue
        for(let i=0;i<graph[node].length;i++){
          const [nextNode,plus]=graph[node][i]
          if (visit[nextNode]===-1||visit[nextNode]>cost+plus){
            visit[nextNode]=cost+plus
            heeappush(q,[visit[nextNode],nextNode])
          }
        }
      }
      let now=0
      for(let i=0;i<K;i++){
        now+=visit[locs[i]]
      }
      return now
    }

    let now=[-1,0]
    for(let i=1;i<=N;i++){
      const value=find(i)
      if (now[0]===-1||now[0]>value) now=[value,i]
    }
    answer.push(now[1])
  }

  console.log(answer.join('\n'))
  process.exit()
})

// N개의 방, M개의 통로, K명의 학생
