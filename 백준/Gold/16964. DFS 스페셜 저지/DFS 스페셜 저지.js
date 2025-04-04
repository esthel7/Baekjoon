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
  const l=[...new Array(N+1)].map(item=>{return{}})
  for(let i=0;i<N-1;i++){
    const [a,b]=input[iter++].split(' ').map(item=>Number(item))
    l[a][b]=true
    l[b][a]=true
  }

  const f=input[iter++].split(' ').map(item=>Number(item))
  if (f[0]!==1){
    console.log(0)
    process.exit()
  }
  let point=1

  const visit=[...new Array(N+1)].map(item=>false)
  function find(idx){
    visit[idx]=true
    let Len=Object.keys(l[idx]).length
    if (Len===0) return
    while(Len>0){
      const nextNode=f[point]
      if (nextNode in l[idx]) {
        Len-=1
        point+=1
        find(nextNode)
        delete(l[idx][nextNode])
      } else {
        const keys=Object.keys(l[idx])
        for(let i=0;i<keys.length;i++){
          if (visit[keys[i]]) continue
          else {
            console.log(0)
            process.exit()
          }
        }
        break
      }
    }
  }
  find(1)

  console.log(1)
  process.exit()
})
