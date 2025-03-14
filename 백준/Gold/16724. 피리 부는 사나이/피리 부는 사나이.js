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
  const l=[]
  for(let i=0;i<N;i++){
    l.push([...input[iter++]])
  }

  function move(x,y){
    if (visit[x][y]===cnt){
      // console.log('roof,make safezone',x,y)
      answer+=1
      return
    }
    if (visit[x][y]>-1 && visit[x][y]<cnt) return
    visit[x][y]=cnt
    if (l[x][y]==='U'){
      if (x-1<0) {
        // console.log('u,make safezone',x,y)
        answer+=1
        return
      }
      return move(x-1,y)
    } else if (l[x][y]==='D'){
      if (x+1>=N) {
        // console.log('d,make safezone',x,y)
        answer+=1
        return
      }
      return move(x+1,y)
    } else if (l[x][y]==='L'){
      if (y-1<0) {
        // console.log('l,make safezone',x,y)
        answer+=1
        return
      }
      return move(x,y-1)
    } else{
      if (y+1>=M) {
        // console.log('r,make safezone',x,y)
        answer+=1
        return
      }
      return move(x,y+1)
    }
  }
  
  let answer=0
  const visit=[...new Array(N)].map(item=>[...new Array(M)].map(item=>-1))
  let cnt=0
  for(let i=0;i<N;i++){
    for(let j=0;j<M;j++){
      if (visit[i][j]!==-1) continue
      // console.log('start',i,j)
      move(i,j)
      cnt+=1
    }
  }

  console.log(answer)
  process.exit()
})
