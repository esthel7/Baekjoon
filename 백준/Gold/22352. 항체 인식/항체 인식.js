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
    l.push(input[iter++].split(' ').map(item=>Number(item)))
  }
  const last=[]
  for(let i=0;i<N;i++){
    last.push(input[iter++].split(' ').map(item=>Number(item)))
  }

  const xbox=[-1,1,0,0]
  const ybox=[0,0,-1,1]

  let cnt=0

  function find(x,y,flag){
    const now=l[x][y]
    const diff=last[x][y]
    if (now!==diff){
      cnt+=1
      if (cnt>1){
        console.log('NO')
        process.exit()
      }
    }
    const q=[[x,y]]
    while(q.length){
      const [x,y]=q.shift()
      for(let i=0;i<4;i++){
        const newX=x+xbox[i]
        const newY=y+ybox[i]
        if (0<=newX && newX<N && 0<=newY && newY<M && !visit[newX][newY] && l[newX][newY]===now){
          visit[newX][newY]=true
          if (last[newX][newY]===diff){
            q.push([newX,newY])
          } else {
            console.log('NO')
            process.exit()
          }
        }
      }
    }
  }

  const visit=[...new Array(N)].map(item=>[...new Array(M)].map(item=>false))
  for(let i=0;i<N;i++){
    for(let j=0;j<M;j++){
      if (!visit[i][j]){
        visit[i][j]=true
        find(i,j)
      }
    }
  }
  console.log('YES')
  process.exit()
})
