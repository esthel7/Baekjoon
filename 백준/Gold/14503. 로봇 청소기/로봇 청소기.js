const readline=require('readline');
const rl=readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

const input=[]
let iter=0
rl.on('line',(line)=>{
  input.push(line)
}).on('close',()=>{
  const [N,M]=input[iter++].split(' ').map(Number)
  const [r,c,d]=input[iter++].split(' ').map(Number)

  const l=[]
  for(let i=0;i<N;i++){
    l.push(input[iter++].split(' ').map(Number))
  }

  const mx=[-1,1,0,0]
  const my=[0,0,-1,1]

  let nowx=r
  let nowy=c
  let dir=d

  let answer=0
  while (true){
    if (l[nowx][nowy]===0){
      answer+=1
      l[nowx][nowy]=2
    }

    let cleanflag=false
    for(let i=0;i<4;i++){
      const newx=nowx+mx[i]
      const newy=nowy+my[i]
      if (0<=newx && newx<N && 0<=newy && newy<M){
        if (l[newx][newy]===0) {
          cleanflag=true
          break
        }
      }
    }

    if (cleanflag){
      dir=(dir+4-1)%4
      if (dir===0) {
        if (l[nowx-1][nowy]===0){
          l[nowx-1][nowy]=2
          answer+=1
          nowx-=1
        }
      } else if (dir===1){
        if (l[nowx][nowy+1]===0){
          l[nowx][nowy+1]=2
          answer+=1
          nowy+=1
        }
      } else if (dir===2){
        if (l[nowx+1][nowy]===0){
          l[nowx+1][nowy]=2
          answer+=1
          nowx+=1
        }
      } else {
        if (l[nowx][nowy-1]===0){
          l[nowx][nowy-1]=2
          answer+=1
          nowy-=1
        }
      }
    } else {
      if (dir===0) {
        if (l[nowx+1][nowy]!==1){
          if (l[nowx+1][nowy]!==2) answer+=1
          l[nowx+1][nowy]=2
          nowx+=1
        } else break
      } else if (dir===1){
        if (l[nowx][nowy-1]!==1){
          if (l[nowx][nowy-1]!==2) answer+=1
          l[nowx][nowy-1]=2
          nowy-=1
        } else break
      } else if (dir===2){
        if (l[nowx-1][nowy]!==1){
          if (l[nowx-1][nowy]!==2) answer+=1
          l[nowx-1][nowy]=2
          nowx-=1
        } else break
      } else {
        if (l[nowx][nowy+1]!==1){
          if (l[nowx][nowy+1]!==2) answer+=1
          l[nowx][nowy+1]=2
          nowy+=1
        } else break
      }
    }
  }

  console.log(answer)
  process.exit()
})

// 0이면 빈칸
// 1이면 벽
