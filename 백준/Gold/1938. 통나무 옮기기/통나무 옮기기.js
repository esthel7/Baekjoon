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
    l.push([...input[iter++].split('')])
  }

  let sdir=-1
  let sx=0
  let sy=0
  let edir=-1
  let ex=0
  let ey=0

  function findLoc(x,y){
    const flag=l[x][y]
    if ((x-1>=0) && l[x-1][y]===flag||(x+1<N) && l[x+1][y]===flag){
      if (x-2>=0 && l[x-2][y]===flag) return [1,x-1,y]
      if (x+2<N && l[x+2][y]===flag) return [1,x+1,y]
      return [1,x,y]
    } else {
      if (y-2>=0 && l[x][y-2]===flag) return [0,x,y-1]
      if (y+2<N && l[x][y+2]===flag) return [0,x,y+1]
      return [0,x,y]
    }
  }

  for(let i=0;i<N;i++){
    for(let j=0;j<N;j++){
      if (l[i][j]==='B'&&sdir===-1) [sdir,sx,sy]=findLoc(i,j)
      if (l[i][j]==='E'&&edir===-1) [edir,ex,ey]=findLoc(i,j)
    }
  }

  const visit=[...new Array(2)].map(item=>[...new Array(N)].map(item=>[...new Array(N)].map(item=>-1))) // 가로, 세로
  visit[sdir][sx][sy]=0

  function canMove(dir,x,y){
    if (dir===0){
      if (l[x][y-1]!=='1' && l[x][y]!=='1' && l[x][y+1]!=='1') return true
      return false
    } else {
      if (l[x-1][y]!=='1' && l[x][y]!=='1' && l[x+1][y]!=='1') return true
      return false
    }
  }

  const q=[[sdir,sx,sy]]
  while(q.length>0){
    const [dir,x,y]=q.shift()
    const cnt=visit[dir][x][y]
    if (dir===edir && x===ex && y===ey) {
      console.log(cnt)
      process.exit()
    }
    if (dir===0){ // 가로 
      if (x-1>=0 && visit[dir][x-1][y]===-1 && canMove(dir,x-1,y)){
        visit[dir][x-1][y]=cnt+1
        q.push([dir,x-1,y])
      }
      if (x+1<N && visit[dir][x+1][y]===-1 && canMove(dir,x+1,y)){
        visit[dir][x+1][y]=cnt+1
        q.push([dir,x+1,y])
      }
      if (y-1>0 && visit[dir][x][y-1]===-1 && canMove(dir,x,y-1)){
        visit[dir][x][y-1]=cnt+1
        q.push([dir,x,y-1])
      }
      if (y+1<N-1 && visit[dir][x][y+1]===-1 && canMove(dir,x,y+1)){
        visit[dir][x][y+1]=cnt+1
        q.push([dir,x,y+1])
      }
      if (x-1>=0 && x+1<N && visit[1][x][y]===-1 && canMove(dir,x-1,y) && canMove(dir,x+1,y)){
        visit[1][x][y]=cnt+1
        q.push([1,x,y,cnt+1])
      }
    } else { // 세로
      if (x-1>0 && visit[dir][x-1][y]===-1 && canMove(dir,x-1,y)){
        visit[dir][x-1][y]=cnt+1
        q.push([dir,x-1,y])
      }
      if (x+1<N-1 && visit[dir][x+1][y]===-1 && canMove(dir,x+1,y)){
        visit[dir][x+1][y]=cnt+1
        q.push([dir,x+1,y])
      }
      if (y-1>=0 && visit[dir][x][y-1]===-1 && canMove(dir,x,y-1)){
        visit[dir][x][y-1]=cnt+1
        q.push([dir,x,y-1])
      }
      if (y+1<N && visit[dir][x][y+1]===-1 && canMove(dir,x,y+1)){
        visit[dir][x][y+1]=cnt+1
        q.push([dir,x,y+1])
      }
      if (y-1>=0 && y+1<N && visit[0][x][y]===-1 && canMove(dir,x,y-1) && canMove(dir,x,y+1)){
        visit[0][x][y]=cnt+1
        q.push([0,x,y])
      }
    }
  }

  console.log(0)
  process.exit()
})
