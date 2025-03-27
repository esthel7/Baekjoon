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
  const N=Number(input[iter++])
  if (N===2){
    console.log('1 2')
    process.exit()
  }
  const root=[...new Array(N+1)].map(item=>-1)
  const info={}

  function update(value,idx){
    if (value in info) info[value].push(idx)
    else info[value]=[idx]
  }

  for(let i=0;i<N-2;i++){
    const [a,b]=input[iter++].split(' ').map(item=>Number(item))
    if (root[a]===-1){
      if (root[b]===-1){
        const Min=Math.min(a,b)
        root[a]=Min
        root[b]=Min
        update(Min,a)
        update(Min,b)
      } else {
        root[a]=root[b]
        update(root[b],a)
      }
    } else {
      if (root[b]===-1){
        root[b]=root[a]
        update(root[a],b)
      } else {
        if (root[a]===root[b]) continue
        const Min=Math.min(root[a],root[b])
        const Max=Math.max(root[a],root[b])
        for(let i=0;i<info[Max].length;i++){
          const idx=info[Max][i]
          root[idx]=Min
          update(Min,idx)
        }
      }
    }
  }

  const first=root[1]
  for(let i=2;i<=N;i++){
    if (first!==root[i]){
      console.log(`${1} ${i}`)
      break
    }
  }
  process.exit()
})
