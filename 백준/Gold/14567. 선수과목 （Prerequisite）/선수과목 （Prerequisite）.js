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
  const answer=[...new Array(N)].map(item=>0)
  const child=[...new Array(N)].map(item=>[])
  const cnt=[...new Array(N)].map(item=>0)

  for(let i=0;i<M;i++){
    let [A,B]=input[iter++].split(' ').map(item=>Number(item))
    A-=1
    B-=1
    child[A].push(B)
    cnt[B]+=1
  }

  const q=[]
  for(let i=0;i<N;i++){
    if (cnt[i]===0) {
      answer[i]=1
      q.push(i)
    }
  }

  while(q.length>0){
    const node=q.shift()
    const time=answer[node]
    for(let i=0;i<child[node].length;i++){
      const now=child[node][i]
      cnt[now]-=1
      if (cnt[now]===0) {
        q.push(now)
        answer[now]=time+1
      }
    }
  }
  
  console.log(answer.join(' '))
  process.exit()
})
