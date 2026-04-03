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
  const l=[]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split('').map(Number))
  }

  const visited=[...new Array(N)].map(item=>[...new Array(N)].map(item=>false))
  const xbox=[0,0,-1,1]
  const ybox=[-1,1,0,0]

  function grouping(x,y,cnt){
    for(let i=0;i<4;i++){
      const newx=x+xbox[i]
      const newy=y+ybox[i]
      if (0<=newx && newx<N && 0<=newy && newy<N){
        if (visited[newx][newy]) continue
        visited[newx][newy]=true
        if (l[newx][newy]!==0) {
          cnt=grouping(newx,newy,cnt+1)
        }
      }
    }
    return cnt
  }

  const answer=[]
  for(let i=0;i<N;i++){
    for(let j=0;j<N;j++){
      if (visited[i][j]) continue
      visited[i][j]=true
      let now=0
      if (l[i][j]!==0) {
        now=grouping(i,j,1)
        answer.push(now)
      }
    }
  }
  answer.sort((a,b)=>a-b)
  console.log(answer.length)
  console.log(answer.join('\n'))
  process.exit()
})
