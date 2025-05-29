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
  const [L,N,K]=input[iter++].split(' ').map(item=>Number(item))
  const A=input[iter++].split(' ').map(item=>Number(item))
  const answer=[]
  const visit=[...new Array(L+1)].map(item=>false)
  let diff=0
  while(true){
    for(let i=0;i<N;i++){
      const now=A[i]
      if (diff===0){
        if (!visit[now]){
          visit[now]=true
          answer.push(diff)
          if (answer.length===K) break
        }
        continue
      }
      if (now-diff>=0 && !visit[now-diff]){
        visit[now-diff]=true
        answer.push(diff)
        if (answer.length===K) break
      }
      if (now+diff<=L && !visit[now+diff]){
        visit[now+diff]=true
        answer.push(diff)
        if (answer.length===K) break
      }
    }
    if (answer.length===K) break
    diff+=1
  }

  console.log(answer.join('\n'))
  process.exit()
})
