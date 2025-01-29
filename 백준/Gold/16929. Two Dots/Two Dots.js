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
  const board=[]
  for (let i=0;i<N;i++){
    board.push(input[iter++].split(''))
  }
  
  const xbox=[-1,1,0,0]
  const ybox=[0,0,-1,1]

  const visit=[...new Array(N)].map(item=>[...new Array(M)].map(item=>[-1,false]))

  function find(x,y){
    for (let i=0;i<4;i++){
      const newX=x+xbox[i]
      const newY=y+ybox[i]
      if (0<=newX && newX<N && 0<=newY&& newY<M && board[x][y]===board[newX][newY]){
          visit[newX][newY][1]=true
          if (visit[newX][newY][0]===-1){
            visit[newX][newY][0]=visit[x][y][0]+1
            find(newX,newY)
            visit[newX][newY][0]=-1
          } else {
            if (visit[x][y][0]-visit[newX][newY][0]>=3) {
              console.log('Yes')
              process.exit()
            }
          }
        }
    }
  }
  for(let i=0;i<N;i++){
    for(let j=0;j<M;j++){
      if (!visit[i][j][1]){
        visit[i][j][0]=1
        visit[i][j][1]=true
        find(i,j)
        visit[i][j][0]=-1
      }
    }
  }
  console.log('No')
  process.exit()
})
