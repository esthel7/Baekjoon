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
