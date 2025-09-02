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
  const [N,R]=input[iter++].split(' ').map(item=>Number(item))
  const info=[...new Array(N+1)].map(item=>[])
  for(let i=0;i<N-1;i++){
    const [a,b,d]=input[iter++].split(' ').map(item=>Number(item))
    info[a].push([b,d])
    info[b].push([a,d])
  }

  let len=0
  let start=R
  let giga=-1
  const visited=[...new Array(N+1)].map(item=>false)
  visited[R]=true
  while (true){
    const child=info[start]
    let cnt=0
    let nextStart=-1
    let possibleLen=0
    for(let i=0;i<child.length;i++){
      const [node,far]=child[i]
      if (visited[node]) continue
      nextStart=node
      possibleLen+=far
      cnt+=1
      if (cnt>1) {
        giga=start
        break
      }
    }
    if (cnt>1) break
    len+=possibleLen
    if (nextStart===-1) break
    start=nextStart
    visited[nextStart]=true
  }

  if (giga===-1) {
    console.log(len,0)
    process.exit()
  }

  let Max=0
  function find(start,now){
    Max=Math.max(Max,now)
    const child=info[start]
    for(let i=0;i<child.length;i++){
      const [node,far]=child[i]
      if (visited[node]) continue
      visited[node]=true
      find(node,now+far)
    }
  }
  find(giga,0)
  console.log(len,Max)
  process.exit()
})

// 기가노드는 루트노드에서 처음으로 자식노드 2개 이상
// 리프가 한개라면(계속 한 줄기라면), 리프노드가 기가노드도 됨
// 루트가 기가노드일수도 있음
// 기둥은 루트부터 기가까지
// 가지는 기가에서 임의 리프까지

// 기둥과 가장 긴 가지
