const readline=require('readline')
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const West=1
const North=2
const East=4
const South=8

function wall(num){
  const now=[]
  if (num&West) now.push(West)
  if (num&North) now.push(North)
  if (num&East) now.push(East)
  if (num&South) now.push(South)
  return now
}

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M]=input[iter++].split(' ').map(item=>Number(item))

  const l=[]
  for (let i=0;i<M;i++){
    l[i]=[]
    const now=input[iter++].split(' ').map(item=>Number(item))
    for(let j=0;j<N;j++){
      l[i][j]=wall(now[j])
    }
  }
  
  const answer=[]
  
  let room=-1
  const rooms=[]
  let Max=0
  const visit=[...new Array(M)].map(item=>[...new Array(N)].map(item=>false))
  const meet={}

  function connect(a,b){
    if (a===b) return
    if (a in meet) meet[a][b]=true
    else meet[a]={[b]:true}
  }

  function findRoom(x,y,cnt){
    const q=[[x,y]]
    visit[x][y]=room
    while (q.length){
      const [x,y]=q.shift()
      cnt+=1
      if (!(l[x][y].includes(West)) && y-1>=0 && visit[x][y-1]===false) {
        visit[x][y-1]=room
        q.push([x,y-1])
      } else if (l[x][y].includes(West) && y-1>=0 && visit[x][y-1]!==false) connect(room,visit[x][y-1])
      if (!(l[x][y].includes(North)) && x-1>=0 && visit[x-1][y]===false) {
        visit[x-1][y]=room
        q.push([x-1,y])
      } else if (l[x][y].includes(North) && x-1>=0 && visit[x-1][y]!==false) connect(room,visit[x-1][y])
      if (!(l[x][y].includes(East)) && y+1<N && visit[x][y+1]===false) {
        visit[x][y+1]=room
        q.push([x,y+1])
      } else if (l[x][y].includes(East) && y+1<N && visit[x][y+1]!==false) connect(room,visit[x][y+1])
      if (!(l[x][y].includes(South)) && x+1<M && visit[x+1][y]===false) {
        visit[x+1][y]=room
        q.push([x+1,y])
      } else if (l[x][y].includes(East) && x+1<M && visit[x+1][y]!==false) connect(room,visit[x+1][y])
    }
    if (cnt>Max) Max=cnt
    rooms.push(cnt)
  }

  for(let i=0;i<M;i++){
    for (let j=0;j<N;j++){
      if (visit[i][j]!==false) continue
      room+=1
      findRoom(i,j,0)
    }
  }
  answer.push(room+1)
  answer.push(Max)

  let removeRoom=0
  Object.keys(meet).map(item=>{
    const to=Number(item)
    Object.keys(meet[item]).map(iitem=>{
      const from=Number(iitem)
      removeRoom=Math.max(removeRoom,rooms[to]+rooms[from])
    })
  })
  answer.push(removeRoom)

  console.log(answer.join('\n'))
  process.exit()
})
