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
  const [N,M,T]=input[iter++].split(' ').map(item=>Number(item))
  const board=[]
  for(let i=0;i<N;i++){
    board.push(input[iter++].split(' '))
  }

  const xbox=[-1,1,0,0]
  const ybox=[0,0,-1,1]
  const l=[...new Array(N)].map(item=>[...new Array(M)].map(item=>-1))
  l[0][0]=0

  function bfs(){
    const q=[[0,0]]
    let ktime=0
    while(q.length>0){
      const [x,y]=q.shift()
      const time=l[x][y]
      if (x===N-1 && y===M-1){
        if (ktime!==0) return Math.min(ktime,l[x][y])
        return l[x][y]
      }
      for(let i=0;i<4;i++){
        const newX=x+xbox[i]
        const newY=y+ybox[i]
        if (!(0<=newX && newX<N && 0<=newY && newY<M)) continue
        if (board[newX][newY]==='1' || l[newX][newY]>-1) continue
        l[newX][newY]=time+1
        q.push([newX,newY])
        if (board[newX][newY]==='2') ktime=time+1+N-1-newX+M-1-newY
      }
    }
    if (ktime!==0) return ktime
    return T+1
  }

  const answer=bfs()
  if (answer<=T) console.log(answer)
  else console.log('Fail')
  process.exit()
})
