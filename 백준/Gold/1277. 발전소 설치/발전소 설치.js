const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

function heappush(q,item){
  q.push(item)
  let idx=q.length-1
  while (idx>=1){
    const parent=Math.floor(idx/2)
    if (q[parent][0]>q[idx][0]) {
      [q[parent],q[idx]]=[q[idx],q[parent]]
      idx=parent
    }
    else break
  }
}

function heappop(q){
  const item=q[1]
  const lastitem=q.pop()
  let idx=1
  q[1]=lastitem
  const last=q.length
  while (idx<last){
    const left=idx*2
    const right=idx*2+1
    if (left>=last) break
    else if (right>=last){
      if (q[idx][0]>q[left][0]) [q[left],q[idx]]=[q[idx],q[left]]
      break
    }
    const smaller=q[left][0]>q[right][0]?right:left
    if (q[idx][0]>q[smaller][0]) {
      [q[smaller],q[idx]]=[q[idx],q[smaller]]
      idx=smaller
    }
    else break
  }
  return item
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,W]=input[iter++].split(' ').map(item=>Number(item))
  const M=Number(input[iter++])
  const info=[[]]
  for(let i=1;i<=N;i++){
    const [x,y]=input[iter++].split(' ').map(item=>Number(item))
    info.push([x,y])
  }

  function diff(x,y,newX,newY){
    const value=((x-newX)**2+(y-newY)**2)**0.5
    if (value<=M) return value
    return -1
  }

  const connect=[...new Array(N+1)].map(item=>[])
  for(let i=1;i<=N;i++){
    for(let j=i+1;j<=N;j++){
      const value=diff(info[i][0],info[i][1],info[j][0],info[j][1])
      if (value===-1) continue
      connect[i].push([value,j])
      connect[j].push([value,i])
    }
  }

  for(let i=0;i<W;i++){
    const [a,b]=input[iter++].split(' ').map(item=>Number(item))
    connect[a].push([0,b])
    connect[b].push([0,a])
  }

  const distance=[...new Array(N+1)].map(item=>-1)
  distance[1]=0
  let answer=-1
  const qq=[[]]
  for(let i=0;i<connect[1].length;i++){
    heappush(qq,connect[1][i])
  }
  while (qq.length>1){
    const [value,node]=heappop(qq)
    if (node===N) {
      answer=value
      break
    }
    if (distance[node]===-1 || distance[node]>value){
      distance[node]=value
      for(let i=0;i<connect[node].length;i++){
        heappush(qq,[connect[node][i][0]+value,connect[node][i][1]])
      }
    }
  }

  console.log(Math.floor(answer*1000))
  process.exit()
})
