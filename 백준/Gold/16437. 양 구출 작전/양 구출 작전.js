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
  const wolf=[...new Array(N+1)].map(item=>0)
  const sheep=[...new Array(N+1)].map(item=>0)
  const parent=[...new Array(N+1)].map(item=>0)
  const child=[...new Array(N+1)].map(item=>0)
  for(let i=2;i<=N;i++){
    let [t,a,p]=input[iter++].split(' ')
    a=Number(a)
    p=Number(p)
    if (t==='W') wolf[i]=a
    else sheep[i]=a
    parent[i]=p
    child[p]+=1
  }

  const q=[]
  for(let i=2;i<=N;i++){
    if (child[i]===0) {
      q.push(i)
    }
  }

  let answer=0
  while (q.length>0){
    const now=q.shift()
    if (now===1) {
      answer+=sheep[now]
      continue
    }

    const parentnode=parent[now]
    sheep[parentnode]+=sheep[now]
    if (wolf[parentnode]>0) {
      if (sheep[parentnode]>=wolf[parentnode]){
        sheep[parentnode]-=wolf[parentnode]
        wolf[parentnode]=0
      } else {
        wolf[parentnode]-=sheep[parentnode]
        sheep[parentnode]=0
      }
    }

    child[parentnode]-=1
    if (child[parentnode]===0) {
      q.push(parentnode)
    }
  }

  console.log(answer)
  process.exit()
})
