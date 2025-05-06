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
  const [N,Q]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  for(let i=0;i<N;i++){
    const [x1,x2,y]=input[iter++].split(' ').map(item=>Number(item))
    l.push([x1,x2,y,i+1])
  }
  l.sort((a,b)=>a[0]-b[0])
  
  const match=[...new Array(N)]
  const root=[...new Array(N)].map((item,idx)=>idx)
  for(let i=0;i<N;i++){
    const [x1,x2,y,idx]=l[i]
    match[idx]=i
    for(let j=i+1;j<N;j++){
      const [nx1,nx2,ny,nidx]=l[j]
      if (nx1<=x2) root[j]=root[i]
      else break
    }
  }
  // console.log(l)
  // console.log(root)

  const answer=[]
  for(let i=0;i<Q;i++){
    let [a,b]=input[iter++].split(' ').map(item=>Number(item))
    a=match[a]
    b=match[b]
    if (root[a]===root[b]) answer.push(1)
    else answer.push(0)
  }
  console.log(answer.join('\n'))
  process.exit()
})
