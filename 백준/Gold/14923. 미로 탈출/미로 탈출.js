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
  let [Hx,Hy]=input[iter++].split(' ').map(item=>Number(item))
  Hx-=1
  Hy-=1
  let [Ex,Ey]=input[iter++].split(' ').map(item=>Number(item))
  Ex-=1
  Ey-=1
  const l=[]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split(' ').map(item=>Number(item)))
  }

  const xbox=[-1,1,0,0]
  const ybox=[0,0,-1,1]

  const visit=[...new Array(2)].map(item=>[...new Array(N)].map(item=>[...new Array(M)].map(item=>false)))
  const q=[]
  if (l[Hx][Hy]===1){
    visit[1][Hx][Hy]=true
    q.push([1,Hx,Hy,0])
  } else {
    visit[0][Hx][Hy]=true
    q.push([0,Hx,Hy,0])
  }
  let idx=0
  while(q.length>idx){
    const [z,x,y,time]=q[idx]
    idx+=1
    for(let i=0;i<4;i++){
      const newX=x+xbox[i]
      const newY=y+ybox[i]
      if (0<=newX && newX<N && 0<=newY && newY<M){
        if (l[newX][newY]===0){
          if (newX===Ex && newY===Ey){
            console.log(time+1)
            process.exit()
          }
          if (visit[z][newX][newY]) continue
          visit[z][newX][newY]=true
          q.push([z,newX,newY,time+1])
        } else {
          if (z===1 || visit[1][newX][newY]) continue
          if (newX===Ex && newY===Ey){
            console.log(time+1)
            process.exit()
          }
          visit[1][newX][newY]=true
          q.push([1,newX,newY,time+1])
        }
      }
    }
  }
  console.log(-1)
  process.exit()
})
