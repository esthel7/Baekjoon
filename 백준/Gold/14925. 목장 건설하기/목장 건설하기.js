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
  const [M,N]=input[iter++].split(' ').map(item=>Number(item))
  const l=[]
  for(let i=0;i<M;i++){
    l.push(input[iter++].split(' '))
  }
  
  let answer=0
  const visit=[...new Array(M+1)].map(item=>[...new Array(N+1)].map(item=>0))
  for(let i=1;i<M+1;i++){
    for(let j=1;j<N+1;j++){
      if (l[i-1][j-1]==='0') {
        visit[i][j]=Math.min(visit[i][j-1],visit[i-1][j],visit[i-1][j-1])+1
        answer=Math.max(answer,visit[i][j])
      }
    }
  }
  console.log(answer)
  process.exit()
})
