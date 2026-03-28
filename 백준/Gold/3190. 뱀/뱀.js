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
  const K=Number(input[iter++])

  // 0은 빈칸, 1은 뱀, 2는 사과
  const l=[...new Array(N)].map(item=>[...new Array(N)].map(item=>0))
  l[0][0]=1
  const snail=[[0,0]]
  let headx=0
  let heady=0
  let dir=1 // 위 오 아 왼

  for(let i=0;i<K;i++){
    const [x,y]=input[iter++].split(' ').map(item=>Number(item)-1)
    l[x][y]=2
  }

  let answer=1
  const L=Number(input[iter++])
  let prev=0
  for(let i=0;i<L;i++){
    const [X,C]=input[iter++].split(' ')
    const x=Number(X)-prev
    prev=Number(X)


    for(let j=0;j<x;j++){
      let newx=headx
      let newy=heady
      if (dir===0){
        newx=headx-1
      } else if (dir===1){
        newy=heady+1
      } else if (dir===2){
        newx=headx+1
      } else {
        newy=heady-1
      }
      headx=newx
      heady=newy

      if (0<=newx && newx<N && 0<=newy && newy<N){
        if (l[newx][newy]===1){
          console.log(answer)
          process.exit()
        }
        if (l[newx][newy]===0){
          const [popx,popy]=snail.shift()
          l[popx][popy]=0
        }
        l[newx][newy]=1
        snail.push([newx,newy])
      } else {
        console.log(answer)
        process.exit()
      }

      answer+=1
    }

    if (C==='L') dir=(dir+4-1)%4
    else dir=(dir+1)%4
  }

  while (true){
    let newx=headx
    let newy=heady
    if (dir===0){
      newx=headx-1
    } else if (dir===1){
      newy=heady+1
    } else if (dir===2){
      newx=headx+1
    } else {
      newy=heady-1
    }
    headx=newx
    heady=newy

    if (0<=newx && newx<N && 0<=newy && newy<N){
      if (l[newx][newy]===1){
        console.log(answer)
        process.exit()
      }
      if (l[newx][newy]===0){
        const [popx,popy]=snail.shift()
        l[popx][popy]=0
      }
      l[newx][newy]=1
      snail.push([newx,newy])
    } else {
      console.log(answer)
      process.exit()
    }

    answer+=1
  }
  process.exit()
})
